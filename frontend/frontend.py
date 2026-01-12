import numpy as np
from datetime import datetime
import time
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import sys
from urllib.parse import urlparse
import logging
import traceback
import re
from streamlit_mermaid import st_mermaid

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Annahme: Backend Import bleibt gleich
from backend import main 
import database.db as db
import streamlit as st
import streamlit_authenticator as stauth

# ----------------------------------------
# MODEL CONFIGURATION
# ----------------------------------------
# 1. Rohdaten definieren
RAW_MAIN_MODELS = [
    # Google Gemini
    "gemini-2.5-flash", "gemini-2.5-flash-lite",
    # Alias
    "alias-reasoning", "alias-ha", "alias-code",
    # Llama
    "meta-llama/Llama-3.3-70B-Instruct", "meta-llama/Llama-3.1-8B-Instruct", "meta-llama/Llama-4-Scout-17B-16E-Instruct", "llama3",
    # DeepSeek
    "deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct", "deepseek-ai/DeepSeek-R1", "deepseek-ai/DeepSeek-V3.2-Exp",
    # Qwen
    "Qwen/Qwen3-Coder-30B-A3B-Instruct", "Qwen/Qwen2-VL-7B-Instruct",
    # Andere
    "openGPT-X/Teuken-7B-instruct-research-v0.4", "openai/gpt-oss-120b", 
]

RAW_HELPER_MODELS = [
    # Alias
    "alias-reasoning", "alias-ha", "alias-code",
    # Llama
    "meta-llama/Llama-3.3-70B-Instruct", "meta-llama/Llama-3.1-8B-Instruct", "meta-llama/Llama-4-Scout-17B-16E-Instruct", "llama3",
    # DeepSeek
    "deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct", "deepseek-ai/DeepSeek-R1", "deepseek-ai/DeepSeek-V3.2-Exp",
    # Qwen
    "Qwen/Qwen3-Coder-30B-A3B-Instruct", "Qwen/Qwen2-VL-7B-Instruct",
    # Andere
    "openGPT-X/Teuken-7B-instruct-research-v0.4", "openai/gpt-oss-120b",   
]

# 2. Bereinigung und Listen-Erstellung
def clean_names(model_list):
    return [m.split("/")[-1] for m in model_list]

HELPER_MODELS = clean_names(RAW_HELPER_MODELS)
MAIN_MODELS = clean_names(RAW_MAIN_MODELS)

STANDARD_MODELS = [
    "gemini-2.5-flash-lite",
    "gemini-2.5-pro",
    "gemini-2.5-flash",
    "gemini-3-flash",
    "gpt-5.1",
    "gpt-5-mini",

]


# Alle Modelle kombiniert
ALL_HELPER_MODELS = sorted(list(set(STANDARD_MODELS + HELPER_MODELS)))
ALL_MAIN_MODELS = sorted(list(set(STANDARD_MODELS + MAIN_MODELS)))
ALL_MODELS = sorted(list(set(ALL_HELPER_MODELS + ALL_MAIN_MODELS)))

CATEGORY_KEYWORDS = {
    "Favoriten": ["STANDARD"], # Zeigt nur STANDARD_MODELS
    "Google Gemini": ["gemini"],
    "Meta Llama": ["llama"],
    "Alias Tools": ["alias"],
    "DeepSeek/Qwen": ["deepseek", "qwen"],
    "GPT & Andere": ["gpt", "teuken", "openai"],
    "Alle anzeigen": [""] # Zeigt alles
}

def get_filtered_models(source_list, category_name):
    """Filtert eine Liste basierend auf der gewählten Kategorie."""
    keywords = CATEGORY_KEYWORDS.get(category_name, [""])
    
    if "STANDARD" in keywords:
        # Nur Modelle zurückgeben, die auch in der Standard-Liste sind
        return [m for m in source_list if m in STANDARD_MODELS]
    
    filtered = []
    for model in source_list:
        # Prüfen ob ein Keyword im Namen steckt
        if any(k in model.lower() for k in keywords):
            filtered.append(model)
            
    return filtered if filtered else source_list # Fallback falls leer


# ----------------------------------------
# 1. Page Config
# ----------------------------------------
st.set_page_config(page_title="Repo Agent", layout="wide", page_icon="🤖")

load_dotenv()
SCADSLLM_KEY=os.getenv("SCADSLLM_KEY")
SCADSLLM_HOST=os.getenv("SCADSLLM_HOST")
# ----------------------------------------
# CSS: SIDEBAR STICKY FOOTER (FINAL FIX)
# ----------------------------------------
st.markdown("""
    <style>
        /* 1. Der Bereich für User-Content in der Sidebar */
        [data-testid="stSidebarUserContent"] {
            display: flex;
            flex-direction: column;
            height: 100vh; /* Volle Höhe */
            justify-content: flex-start; /* WICHTIG: Alles fängt oben an! */
        }
        
        /* 2. Alle Container außer dem letzten verhalten sich normal */
        [data-testid="stSidebarUserContent"] > div {
            width: 100%; /* Sicherstellen, dass sie die Breite füllen */
        }

        /* 3. NUR das letzte Element (Einstellungen) wird nach unten gedrückt */
        [data-testid="stSidebarUserContent"] > div:last-of-type {
            margin-top: auto; /* Das schiebt es an den Boden */
            padding-bottom: 20px; /* Abstand zum Rand */
            padding-top: 10px; /* Kleiner Abstand zum Inhalt darüber */
            border-top: 1px solid rgba(255, 255, 255, 0.1); /* Optional: Trennlinie */
        }
    </style>
""", unsafe_allow_html=True)

# ----------------------------------------
# CALLBACKS
# ----------------------------------------

def save_gemini_cb():
    new_key = st.session_state.get("in_gemini_key", "")
    if new_key:
        db.update_gemini_key(st.session_state["username"], new_key)
        st.session_state["in_gemini_key"] = ""
        st.toast("Gemini Key erfolgreich gespeichert! ✅")

def save_ollama_cb():
    new_url = st.session_state.get("in_ollama_url", "")
    if new_url:
        db.update_ollama_url(st.session_state["username"], new_url)
        st.toast("Ollama URL gespeichert! ✅")

# ----------------------------------------
# DATA LOADING (CONSISTENT)
# ----------------------------------------

def load_data_from_db(username: str):
    """Lädt Chats und Exchanges konsistent aus der DB."""
    
    # Nur laden, wenn neuer User oder noch nicht geladen
    if "loaded_user" not in st.session_state or st.session_state.loaded_user != username:
        st.session_state.chats = {}
        
        # 1. Erst die definierten Chats laden (damit auch leere Chats da sind)
        db_chats = db.fetch_chats_by_user(username)
        for c in db_chats:
            c_name = c.get("chat_name")
            if c_name:
                st.session_state.chats[c_name] = {"exchanges": []}

        # 2. Dann die Exchanges laden und einsortieren
        db_exchanges = db.fetch_exchanges_by_user(username)
        for ex in db_exchanges:
            c_name = ex.get("chat_name", "Unbenannt")
            
            # Falls Exchanges existieren für Chats, die nicht in dbchats sind (Legacy Support)
            if c_name not in st.session_state.chats:
                st.session_state.chats[c_name] = {"exchanges": []}
            
            if "feedback" not in ex or ex["feedback"] is None:
                ex["feedback"] = np.nan
            
            st.session_state.chats[c_name]["exchanges"].append(ex)

        # 3. Default Chat erstellen, falls gar nichts existiert
        if not st.session_state.chats:
            initial_name = "Chat 1"
            # Konsistent in DB anlegen
            db.insert_chat(username, initial_name)
            st.session_state.chats[initial_name] = {"exchanges": []}
            st.session_state.active_chat = initial_name
        else:
            # Active Chat setzen, falls nötig
            if "active_chat" not in st.session_state or st.session_state.active_chat not in st.session_state.chats:
                # Nimm den ersten verfügbaren Chat
                st.session_state.active_chat = list(st.session_state.chats.keys())[0]
        
        st.session_state.loaded_user = username

# ----------------------------------------
# ACTION HANDLERS
# ----------------------------------------

def handle_feedback_change(ex, val):
    ex["feedback"] = val
    db.update_exchange_feedback(ex["_id"], val)
    st.rerun()

def handle_delete_exchange(chat_name, ex):
    db.delete_exchange_by_id(ex["_id"])
    if chat_name in st.session_state.chats:
        if ex in st.session_state.chats[chat_name]["exchanges"]:
            st.session_state.chats[chat_name]["exchanges"].remove(ex)
    st.rerun()

def handle_delete_chat(username, chat_name):
    # KONSISTENZ: Ruft jetzt delete_full_chat in DB auf
    db.delete_full_chat(username, chat_name)
    
    # State bereinigen
    if chat_name in st.session_state.chats:
        del st.session_state.chats[chat_name]
    
    # Active Chat neu setzen
    if len(st.session_state.chats) > 0:
        st.session_state.active_chat = list(st.session_state.chats.keys())[0]
    else:
        # Wenn alles weg ist, neuen leeren Chat anlegen
        new_name = "Chat 1"
        db.insert_chat(username, new_name)
        st.session_state.chats[new_name] = {"exchanges": []}
        st.session_state.active_chat = new_name
        
    st.rerun()

# ----------------------------------------
# HELPER: GENERATOR, EXTRACTOR & MERMAID
# ----------------------------------------

def extract_repo_name(text):
    url_match = re.search(r'(https?://[^\s]+)', text)
    if url_match:
        url = url_match.group(0)
        parsed = urlparse(url)
        path = parsed.path.strip("/")
        if path:
            repo_name = path.split("/")[-1]
            if repo_name.endswith(".git"):
                repo_name = repo_name[:-4]
            return repo_name
    return None

def stream_text_generator(text):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.01)

def render_text_with_mermaid(markdown_text, should_stream=False):
    if not markdown_text:
        return

    parts = re.split(r"```mermaid\s+(.*?)\s+```", markdown_text, flags=re.DOTALL)

    for i, part in enumerate(parts):
        if i % 2 == 0:
            if part.strip():
                if should_stream:
                    st.write_stream(stream_text_generator(part))
                else:
                    st.markdown(part)
        else:
            try:
                st_mermaid(part, key=f"mermaid_{hash(part)}_{i}")
            except Exception:
                st.code(part, language="mermaid")

# ----------------------------------------
# RENDER EXCHANGES
# ----------------------------------------

def render_exchange(ex, current_chat_name):
    st.chat_message("user").write(ex["question"])

    with st.chat_message("assistant"):
        answer_text = ex.get("answer", "")
        is_error = answer_text.startswith("Fehler") or answer_text.startswith("Error")

        # --- 1. TOOLBAR CONTAINER ---
        # Nutzt die neuen Parameter horizontal=True und alignment
        # border=True rahmt die Toolbar ein
        # horizontal_alignment="right" schiebt alles nach rechts
        with st.container(horizontal=True, horizontal_alignment="right"):
            
            if not is_error:
                # 1. Status Text (wird jetzt links von den Buttons angezeigt, aber rechtsbündig im Container)
                st.write("hier die Antwort:")
                if ex.get("feedback") == 1:
                    st.caption("✅ Hilfreich")
                elif ex.get("feedback") == 0:
                    st.caption("❌ Nicht hilfreich")
                
                # 2. Die Buttons (einfach untereinander im Code, erscheinen nebeneinander im UI)
                
                # Like
                type_primary_up = ex.get("feedback") == 1
                if st.button("👍", key=f"up_{ex['_id']}", type="primary" if type_primary_up else "secondary", help="Hilfreich"):
                    handle_feedback_change(ex, 1)

                # Dislike
                type_primary_down = ex.get("feedback") == 0
                if st.button("👎", key=f"down_{ex['_id']}", type="primary" if type_primary_down else "secondary", help="Nicht hilfreich"):
                    handle_feedback_change(ex, 0)

                # Comment Popover
                with st.popover("💬", help="Notiz hinzufügen"):
                    msg = st.text_area("Notiz:", value=ex.get("feedback_message", ""), key=f"txt_{ex['_id']}")
                    if st.button("Speichern", key=f"save_{ex['_id']}"):
                        ex["feedback_message"] = msg
                        db.update_exchange_feedback_message(ex["_id"], msg)
                        st.success("Gespeichert!")
                        time.sleep(0.5)
                        st.rerun()

                # Download
                st.download_button(
                    label="📥",
                    data=ex["answer"],
                    file_name=f"response_{ex['_id']}.md",
                    mime="text/markdown",
                    key=f"dl_{ex['_id']}",
                    help="Als Markdown herunterladen"
                )

                # Delete
                if st.button("🗑️", key=f"del_{ex['_id']}", help="Nachricht löschen", type="secondary"):
                    handle_delete_exchange(current_chat_name, ex)

            else:
                # Fehlerfall
                st.error("⚠️ Fehler")
                if st.button("🗑️ Löschen", key=f"del_err_{ex['_id']}"):
                    handle_delete_exchange(current_chat_name, ex)

        # --- 2. CONTENT (Antwort) ---
        with st.container(height=500, border=True):
             render_text_with_mermaid(ex["answer"], should_stream=False)

# ----------------------------------------
# AUTH SETUP
# ----------------------------------------

users_data = db.fetch_all_users()
credentials = {"usernames": {}}

for user in users_data:
    credentials["usernames"][user["_id"]] = {
        "name": user["name"],
        "password": user["hashed_password"],
    }

authenticator = stauth.Authenticate(
    credentials,
    "Repo-Agent",
    "abcdef",
    cookie_expiry_days=30
)

# ----------------------------------------
# LOGIN / REGISTER
# ----------------------------------------

if st.session_state["authentication_status"] is not True:
    keys_to_clear = ["chats", "loaded_user", "data_loaded", "active_chat"]
    for key in keys_to_clear:
        if key in st.session_state:
            del st.session_state[key]

    authenticator.login("main", key="Login")

    if st.session_state["authentication_status"] is False:
        st.error("Username/password is incorrect")
    elif st.session_state["authentication_status"] is None:
        st.warning("Please enter your username and password")

    st.markdown("---")
    with st.expander("🆕 Neuen Account erstellen"):
        with st.form("register_form"):
            new_user = st.text_input("Username (bitte nur kleinbuchstaben und zahlen)")
            new_name = st.text_input("Display Name")
            new_pass = st.text_input("Passwort", type="password")
            new_pass_confirm = st.text_input("Passwort wiederholen", type="password")
            
            if st.form_submit_button("Registrieren"):
                if new_pass != new_pass_confirm:
                    st.error("Passwörter stimmen nicht überein.")
                elif not new_user or not new_pass:
                    st.error("Bitte alle Felder ausfüllen.")
                elif new_user in credentials["usernames"]:
                    st.error("Username existiert bereits.")
                else:
                    try:
                        db.insert_user(new_user, new_name, new_pass)
                        st.success("Account erstellt! Bitte einloggen.")
                    except Exception as e:
                        st.error(f"Fehler: {e}")

# ----------------------------------------
# HAUPT APP
# ----------------------------------------

if st.session_state["authentication_status"]:

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    current_user = st.session_state["username"]
    current_name = st.session_state["name"]

    # Initial Data Load
    load_data_from_db(current_user)

    # ----------------------------------------
    # SIDEBAR
    # ----------------------------------------
    with st.sidebar:
        with st.container():
            st.write(f"👤 **{current_name}**")
            authenticator.logout("Abmelden", "sidebar",)
            
        
        
        # Sicherstellen, dass Active Chat gültig ist
        chat_names = list(st.session_state.chats.keys())
        if st.session_state.active_chat not in chat_names:
             if chat_names:
                 st.session_state.active_chat = chat_names[0]
             else:
                 # Fallback (sollte durch load_data abgefangen sein)
                 st.session_state.active_chat = "Chat 1" 

        with st.container(border=None, gap=None,height=400):
            # --- CHAT MANAGEMENT ---
            if st.button("➕ Neuer Chat", width="content", type="tertiary"):
                # Namen generieren
                base_name = "Chat"
                i = 1
                while True:
                    candidate = f"{base_name} {i}"
                    if candidate not in st.session_state.chats:
                        new_name = candidate
                        break
                    i += 1
                # KONSISTENZ: Sofort in DB schreiben
                db.insert_chat(current_user, new_name)
                # In Session State
                st.session_state.chats[new_name] = {"exchanges": []}
                st.session_state.active_chat = new_name
                st.rerun()

            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            st.caption("*Chats:*")
            for chat_name in list(st.session_state.chats.keys()):
                label = chat_name
                # Optional: Anzeigen wie viele Nachrichten drin sind
                # count = len(st.session_state.chats[chat_name]["exchanges"])
                # label = f"{chat_name} ({count})"

                if st.button(label, key=f"btn_{chat_name}", width="content", 
                            type="tertiary"):
                    st.session_state.active_chat = chat_name
                    st.rerun()

        

        with st.container(border=None, gap=None):
            if st.button("🗑️ aktuellen Chat löschen", width="content", type="tertiary"):
                handle_delete_chat(current_user, st.session_state.active_chat)        
            
            with st.popover("⚙️ Einstellungen", type="tertiary"):
                st.toggle("Notebook Modus", key="notebook_mode", help="ermöglicht wenn aktiviert die Dokumentation von Jupyter Notebooks, deaktiviert werden .py files ausgewertet", value=False)
                st.caption("🤖 Modelle")
                
                

                sbhelp = "None"
                # Helper LLM Auswahl
                if  not st.session_state.notebook_mode:
                    cat_helper = st.selectbox(
                    "Kategorie (Helper):", 
                    list(CATEGORY_KEYWORDS.keys()), 
                    index=0, 
                    key="cat_helper"
                    )
                    filtered_helpers = get_filtered_models(ALL_HELPER_MODELS, cat_helper)

                    sbhelp = st.selectbox(
                        "Helper LLM", 
                        filtered_helpers,
                        index=0, # Standard auf das erste Element (gemini-2.0-flash-lite)
                        label_visibility="collapsed"
                    )
                
                cat_main = st.selectbox(
                    "Kategorie (Main):", 
                    list(CATEGORY_KEYWORDS.keys()), 
                    index=0, # Default: Favoriten
                    key="cat_main"
                )
                filtered_mains = get_filtered_models(ALL_MAIN_MODELS, cat_main)

                # Main LLM Auswahl
                sbmain = st.selectbox(
                    "Main LLM", 
                    filtered_mains,
                    index=2, # Standard z.B. auf gemini-2.5-pro
                    label_visibility="collapsed"
                )
                
                if not st.session_state.notebook_mode:
                    st.caption(f"Gewählt: Python Modus mit: \n\n {sbhelp} -> {sbmain}")
                else:
                    st.caption(f"Gewählt: Notebook Modus mit: \n\n {sbmain}")
                st.markdown("---")

                # API Keys holen
                gemini_key, ollama_url, gpt_key , opensrc_key, opensrc_url = db.get_decrypted_api_keys(current_user)
                has_gemini = bool(gemini_key)
                has_ollama = bool(ollama_url)
                has_gpt = bool(gpt_key)
                has_opensrc_url = bool(opensrc_url)
                has_opensrc_key = bool(opensrc_key)

                st.caption("API Keys Configuration")
                
                # Logik: Zeige Inputs nur für Modelle, die User-Keys brauchen
                
                # 1. Check für Gemini
                if sbhelp.startswith("gemini") or sbmain.startswith("gemini"):
                    status_icon = "✅" if has_gemini else "❌"
                    st.markdown(f"**Gemini Key**: {status_icon} {'Gesetzt' if has_gemini else 'Fehlt'}")
                    with st.form("gemini_form"):
                        new_gemini = st.text_input("Gemini Key ändern", type="password")
                        if st.form_submit_button("Speichern") and new_gemini:
                            db.update_gemini_key(current_user, new_gemini)
                            st.success("Gespeichert!")
                            time.sleep(0.5)
                            st.rerun() 

                # 2. Check für Ollama (Lokal)
                if sbhelp == "llama3" or sbmain == "llama3":
                    status_icon = "✅" if has_ollama else "❌"
                    st.markdown(f"**Llama URL**: {status_icon} {'Gesetzt' if has_ollama else 'Fehlt'}")
                    current_url_val = ollama_url if ollama_url else ""
                    with st.form("ollama_form"):
                        new_ollama = st.text_input("Llama Base URL ändern", value=current_url_val)
                        if st.form_submit_button("Speichern"):
                            if new_ollama != current_url_val:
                                db.update_ollama_url(current_user, new_ollama)
                                st.success("Gespeichert!")
                                time.sleep(0.5)
                                st.rerun()

                # 3. Check für GPT (OpenAI)
                if sbhelp.startswith("gpt-5") or sbmain.startswith("gpt-5"):
                    
                    status_icon = "✅" if has_gpt else "❌"
                    st.markdown(f"**GPT Key**: {status_icon} {'Gesetzt' if has_gpt else 'Fehlt'}")
                    with st.form("gpt_form"):
                        new_gpt = st.text_input("GPT Key ändern", type="password")
                        if st.form_submit_button("Speichern") and new_gpt:
                            db.update_gpt_key(current_user, new_gpt)
                            st.success("Gespeichert!")
                            time.sleep(0.5)
                            st.rerun()

                else:
                    status_icon = "✅" if has_opensrc_key else "❌"  
                    st.markdown(f"**Open Source LLM Key**: {status_icon} {'Gesetzt' if has_opensrc_key else 'Fehlt'}")
                    status_icon_url = "✅" if has_opensrc_url else "❌"
                    st.markdown(f"**Open Source LLM URL**: {status_icon_url} {'Gesetzt' if has_opensrc_url else 'Fehlt'}")
                    with st.form("opensrc_form"):
                        new_opensrc_key = st.text_input("Open Source LLM Key ändern", type="password")
                        new_opensrc_url = st.text_input("Open Source LLM URL ändern")
                        if st.form_submit_button("Speichern"):
                            if new_opensrc_key:
                                db.update_opensrc_key(current_user, new_opensrc_key)
                            if new_opensrc_url:
                                db.update_opensrc_url(current_user, new_opensrc_url)
                            st.success("Gespeichert!")
                            time.sleep(0.5)
                            st.rerun()    
                
               

    # ----------------------------------------
    # CHAT AREA
    # ----------------------------------------
    active_chat_name = st.session_state.active_chat
    # Safety Check
    if active_chat_name not in st.session_state.chats:
         st.error("Fehler beim Laden des Chats.")
         st.stop()

    chat_data = st.session_state.chats[active_chat_name]

    st.title(f"👋 Hallo, {current_name}!")
    st.caption(f"Aktueller Chat: **{active_chat_name}**")
    st.markdown("---")

    # Render History
    for ex in chat_data["exchanges"]:
        render_exchange(ex, active_chat_name)

    # Input Handling
    if prompt := st.chat_input("Link zum Git Repository..."):
        st.chat_message("user").write(prompt)
        
        # --- 1. SOFORTIGE UMBENENNUNG (VOR DER ANALYSE) ---
        current_chat_name = st.session_state.active_chat
        
        # Prüfen, ob der aktuelle Name generisch ist (startet mit "Neuer Chat" oder "Chat")
        # Damit überschreiben wir keine vom User manuell gewählten Namen (falls du das später einbaust)
        is_generic_name = current_chat_name.startswith("Neuer Chat") or current_chat_name.startswith("Chat ")
        
        repo_name = extract_repo_name(prompt)
        
        # Wir arbeiten mit einer lokalen Variable für den Namen, falls er sich ändert
        working_chat_name = current_chat_name

        if is_generic_name and repo_name:
            # Namen kollisionsfrei machen (falls "react" schon existiert -> "react (2)")
            new_name = repo_name
            counter = 1
            existing_chats = list(st.session_state.chats.keys())
            
            while new_name in existing_chats:
                # Sicherheit: Falls der Chat schon so heißt wie das Repo (z.B. User postet Link nochmal), nichts tun
                if new_name == current_chat_name:
                    break 
                counter += 1
                new_name = f"{repo_name} ({counter})"
            
            if new_name != current_chat_name:
                # A) In der Datenbank umbenennen
                db.rename_chat_fully(current_user, current_chat_name, new_name)
                
                # B) Im Frontend Session State verschieben
                chat_content = st.session_state.chats.pop(current_chat_name)
                st.session_state.chats[new_name] = chat_content
                st.session_state.active_chat = new_name
                
                # C) Arbeitsvariable aktualisieren
                working_chat_name = new_name
                
                # Kleines Feedback (Sidebar aktualisiert sich erst nach dem Rerun am Ende)
                st.toast(f"📂 Chat umbenannt zu: **{new_name}**")

        # --- 2. ANALYSE STARTEN ---
        
        status = st.status(f"⏳ Analysiere Repository in '{working_chat_name}'...", expanded=True)

        dec_gemini, dec_ollama, dec_gpt = db.get_decrypted_api_keys(current_user)
        api_keys = {"gemini": dec_gemini, "ollama": dec_ollama, "gpt": dec_gpt, "scadsllm": SCADSLLM_KEY, "scadsllm_base_url": SCADSLLM_HOST}
        model_config = {"helper": sbhelp, "main": sbmain}

        workflow_success = False
        response = ""
        metrics = {}
        
        try:
            if not st.session_state.notebook_mode: 
                # Hier läuft der Prozess (5-6 Minuten)
                result_data = main.main_workflow(
                    input=prompt, 
                    api_keys=api_keys, 
                    model_names=model_config,
                    status_callback=status.write 
                )
            elif st.session_state.notebook_mode:  
                # Hier läuft der Prozess (5-6 Minuten)
                result_data = main.notebook_workflow(
                    input=prompt, 
                    api_keys=api_keys, 
                    model=model_config["main"],
                    status_callback=status.write 
                )  
            
            logging.info(f"Workflow finished. Keys: {result_data.keys()}")
            response = result_data["report"]
            metrics = result_data["metrics"]
            
            if response.startswith("Error:") or response.startswith("Fehler"):
                workflow_success = False
            else:
                workflow_success = True
            
        except Exception as e:
            error_details = traceback.format_exc()
            logging.error(f"CRITICAL ERROR: {error_details}")
            response = f"Fehler bei der Verarbeitung: {e}"
            metrics = {
                "helper_time": "0", "main_time": "0", "total_time": "0",
                "helper_model": sbhelp, "main_model": sbmain
            }
            workflow_success = False
        
        # ... (Code davor bleibt gleich) ...

        status.update(label="Fertig!", state="complete", expanded=False)
        
        with st.chat_message("assistant"):
            if workflow_success:
                st.write("Antwort generiert:")
                with st.container(height=500):
                    # HIER GEÄNDERT: Streaming AUS für Stabilität bei großen Texten
                    render_text_with_mermaid(response, should_stream=False)
            else:
                st.error(response)

        # --- 3. SPEICHERN (UNTER DEM NEUEN NAMEN) ---
        if workflow_success:
            new_id = db.insert_exchange(
                question=prompt,
                answer=response,
                feedback=np.nan,
                username=current_user,
                chat_name=working_chat_name, 
                helper_used=metrics["helper_model"],
                main_used=metrics["main_model"],
                total_time=str(metrics["total_time"]),
                helper_time=str(metrics["helper_time"]),
                main_time=str(metrics["main_time"]),
                json_tokens=metrics.get("json_tokens", 0),
                toon_tokens=metrics.get("toon_tokens", 0),
                savings_percent=metrics.get("savings_percent", 0.0)
            )
            
            new_ex = {
                "_id": new_id, 
                "question": prompt,
                "answer": response,
                "feedback": np.nan,
                "feedback_message": "",
                "chat_name": working_chat_name,
                "username": current_user,
                "helper_used": metrics["helper_model"],
                "main_used": metrics["main_model"],
                "json_tokens": metrics.get("json_tokens", 0),
                "toon_tokens": metrics.get("toon_tokens", 0),
                "savings_percent": metrics.get("savings_percent", 0.0),
                "datetime": datetime.now()
            }
            
            if working_chat_name in st.session_state.chats:
                st.session_state.chats[working_chat_name]["exchanges"].append(new_ex)
            
            # Safe Rerun: Falls der Socket hier schon wackelt, fangen wir es ab
            try:
                st.rerun()
            except Exception:
                # Falls Rerun fehlschlägt (z.B. Connection Lost), ist das okay,
                # da die Daten in der DB gespeichert sind. Der User drückt dann F5.
                pass
