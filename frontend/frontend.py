import uuid
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

# ========================================
# RESPONSIVE CSS & VIEWPORT CONFIGURATION
# ========================================

# Viewport Meta Tag für Mobile
st.set_page_config(
    page_title="Repo Agent", 
    layout="wide", 
    page_icon="🤖",
    initial_sidebar_state="auto"
)

# Comprehensive CSS für responsive Design

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
    "Standard": ["STANDARD"],
    "Google Gemini": ["gemini"],
    "Meta Llama": ["llama"],
    "Alias Tools": ["alias"],
    "DeepSeek/Qwen": ["deepseek", "qwen"],
    "GPT & Andere": ["gpt", "teuken", "openai"],
    "Alle anzeigen": [""]
}

def get_filtered_models(source_list, category_name):
    """Filtert eine Liste basierend auf der gewählten Kategorie."""
    keywords = CATEGORY_KEYWORDS.get(category_name, [""])
    
    if "STANDARD" in keywords:
        return [m for m in source_list if m in STANDARD_MODELS]
    
    filtered = []
    for model in source_list:
        if any(k in model.lower() for k in keywords):
            filtered.append(model)
            
    return filtered if filtered else source_list

# --- NEU: INITIALISIERUNG FÜR ABBRUCH-LOGIK ---
if "is_running" not in st.session_state:
    st.session_state.is_running = False
if "abort_requested" not in st.session_state:
    st.session_state.abort_requested = False

def handle_abort():
    st.session_state.abort_requested = True
    st.toast("🛑 Abbruch wird verarbeitet...")

# ----------------------------------------
# 1. Page Config
# ----------------------------------------

load_dotenv()
SCADSLLM_KEY=os.getenv("SCADSLLM_KEY")
SCADSLLM_HOST=os.getenv("SCADSLLM_HOST")

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

def get_last_activity(chat_name):
    """Ermittelt den Zeitstempel der letzten Nachricht in einem Chat."""
    chat_data = st.session_state.chats.get(chat_name, {})
    exchanges = chat_data.get("exchanges", [])
    
    creation_dt = chat_data.get("created_at", datetime.min)

    if not exchanges:
        return creation_dt
    last_ex = exchanges[-1]
    dt = last_ex.get("datetime", datetime.min)
    if isinstance(dt, str):
        try: 
            dt = datetime.fromisoformat(dt)
        except: 
            dt = datetime.min
    return dt

def load_data_from_db(username: str):
    if "loaded_user" not in st.session_state or st.session_state.loaded_user != username:
        st.session_state.chats = {}
        db_chats = db.fetch_chats_by_user(username)
        for c in db_chats:
            c_name = c.get("chat_name")
            if c_name:
                st.session_state.chats[c_name] = {
                    "exchanges": [],
                    "created_at": c.get("created_at", datetime.min)
                }

        db_exchanges = db.fetch_exchanges_by_user(username)
        for ex in db_exchanges:
            c_name = ex.get("chat_name", "Unbenannt")
            if c_name not in st.session_state.chats:
                st.session_state.chats[c_name] = {"exchanges": []}
            if "feedback" not in ex or ex["feedback"] is None:
                ex["feedback"] = np.nan
            st.session_state.chats[c_name]["exchanges"].append(ex)

        if not st.session_state.chats:
            initial_name = "Chat 1"
            db.insert_chat(username, initial_name)
            st.session_state.chats[initial_name] = {"exchanges": []}
            st.session_state.active_chat = initial_name
        else:
            sorted_names = sorted(st.session_state.chats.keys(), key=get_last_activity, reverse=True)
            if "active_chat" not in st.session_state or st.session_state.active_chat not in st.session_state.chats:
                st.session_state.active_chat = sorted_names[0]
        
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
    db.delete_full_chat(username, chat_name)
    
    if chat_name in st.session_state.chats:
        del st.session_state.chats[chat_name]
    
    if len(st.session_state.chats) > 0:
        st.session_state.active_chat = list(st.session_state.chats.keys())[0]
    else:
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
    
    answer_text = ex.get("answer", "")
    is_error = answer_text.startswith("Fehler") or answer_text.startswith("Error")

    if is_error:
        st.error(answer_text)
        if st.button("🗑️ Fehler-Nachricht löschen", key=f"del_err_hist_{ex['_id']}", type="secondary"):
            handle_delete_exchange(current_chat_name, ex)
    else:
        with st.chat_message("assistant"):
            with st.container(horizontal=True, horizontal_alignment="right"):
                st.write("hier die Antwort:")
                if ex.get("feedback") == 1:
                    st.caption("✅ Hilfreich")
                elif ex.get("feedback") == 0:
                    st.caption("❌ Nicht hilfreich")
                
                if st.button("👍", key=f"up_{ex['_id']}", type="primary" if ex.get("feedback") == 1 else "secondary"):
                    handle_feedback_change(ex, 1)
                if st.button("👎", key=f"down_{ex['_id']}", type="primary" if ex.get("feedback") == 0 else "secondary"):
                    handle_feedback_change(ex, 0)
                
                with st.popover("💬"):
                    msg = st.text_area("Notiz:", value=ex.get("feedback_message", ""), key=f"txt_{ex['_id']}")
                    if st.button("Speichern", key=f"save_{ex['_id']}"):
                        db.update_exchange_feedback_message(ex["_id"], msg)
                        st.rerun()

                st.download_button("📥", data=ex["answer"], file_name="response.md", key=f"dl_{ex['_id']}")
                if st.button("🗑️", key=f"del_{ex['_id']}"):
                    handle_delete_exchange(current_chat_name, ex)

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
        chat_names = list(st.session_state.chats.keys())
        if st.session_state.active_chat not in chat_names:
             if chat_names:
                 st.session_state.active_chat = chat_names[0]
             else:
                 st.session_state.active_chat = "Chat 1" 

        with st.container(border=None, gap=None):
            if st.button("➕ Neuer Chat", use_container_width=True, type="tertiary", key="btn_new_chat"):
                base_name = "Chat"
                i = 1
                while True:
                    candidate = f"{base_name} {i}"
                    if candidate not in st.session_state.chats:
                        new_name = candidate
                        break
                    i += 1
                db.insert_chat(current_user, new_name)
                st.session_state.chats[new_name] = {
                    "exchanges": [],
                    "created_at": datetime.now()
                }
                st.session_state.active_chat = new_name
                st.rerun()

            if st.button("🗑️ Löschen", use_container_width=True, type="tertiary", key="btn_delete_chat"):
                handle_delete_chat(current_user, st.session_state.active_chat)   
        with st.container(border=None, gap=None,height=400):
            sorted_chat_names = sorted(
                st.session_state.chats.keys(), 
                key=get_last_activity, 
                reverse=True
            )

            for chat_name in sorted_chat_names:
                is_active = (chat_name == st.session_state.active_chat)
                label = f" {chat_name}" if not is_active else f" {chat_name}"
                if st.button(label, key=f"btn_{chat_name}", width="stretch", 
                            type="secondary" if is_active else "tertiary"):
                    st.session_state.active_chat = chat_name
                    st.rerun()

        with st.container(border=None, gap=None, horizontal_alignment="left"):
            st.toggle(
                "Notebook Modus", key="notebook_mode", 
                help=(
                    "Aktiviert können Jupyter Notebooks (.ipynb) ausgewertet werden, "
                    "deaktiviert werden Python (.py) files ausgewertet"
                ), 
                value=False,
                width="stretch"
            )  
            with st.popover("⚙️ Einstellungen", type="tertiary", ):
                gemini_key, ollama_url, gpt_key, opensrc_key, opensrc_url = db.get_decrypted_api_keys(current_user)
                has_gemini, has_ollama, has_gpt = bool(gemini_key), bool(ollama_url), bool(gpt_key)
                has_opensrc_url, has_opensrc_key = bool(opensrc_url), bool(opensrc_key)

                def get_provider(model_name):
                    if not model_name or model_name == "None": 
                        return None
                    if model_name.startswith("gemini"): 
                        return "Google Gemini"
                    if model_name == "llama3": 
                        return "ollama"
                    if model_name.startswith("gpt-5"): 
                        return "gpt"
                    return "Open Source LLM"

                def render_config_form(model_name):
                    provider = get_provider(model_name)
                    if provider == "Google Gemini":
                        status_icon = "✅" if has_gemini else "❌"
                        st.markdown(f"**Gemini Key**: {status_icon} {'Gesetzt' if has_gemini else 'Fehlt'}")
                        with st.form(f"form_gemini_{model_name}"):
                            new_gemini = st.text_input("Gemini Key ändern", type="password")
                            if st.form_submit_button("Speichern") and new_gemini:
                                db.update_gemini_key(current_user, new_gemini)
                                st.success("Gespeichert!")
                                time.sleep(0.5)
                                st.rerun()
                            if st.form_submit_button("Löschen"):
                                db.update_gemini_key(current_user, "")
                                st.rerun()

                    elif provider == "ollama":
                        status_icon = "✅" if has_ollama else "❌"
                        st.markdown(f"**Llama URL**: {status_icon} {'Gesetzt' if has_ollama else 'Fehlt'}")
                        with st.form(f"form_ollama_{model_name}"):
                            new_ollama = st.text_input("Llama Base URL ändern", value=ollama_url if ollama_url else "")
                            if st.form_submit_button("Speichern"):
                                db.update_ollama_url(current_user, new_ollama)
                                st.success("Gespeichert!")
                                time.sleep(0.5)
                                st.rerun()
                            if st.form_submit_button("Löschen"):
                                db.update_ollama_url(current_user, "")
                                st.rerun()

                    elif provider == "gpt":
                        status_icon = "✅" if has_gpt else "❌"
                        st.markdown(f"**GPT Key**: {status_icon} {'Gesetzt' if has_gpt else 'Fehlt'}")
                        with st.form(f"form_gpt_{model_name}"):
                            new_gpt = st.text_input("GPT Key ändern", type="password")
                            
                            if st.form_submit_button("Speichern") and new_gpt:
                                db.update_gpt_key(current_user, new_gpt)
                                st.success("Gespeichert!")
                                time.sleep(0.5)
                                st.rerun()
                            if st.form_submit_button("Löschen"):
                                db.update_gpt_key(current_user, "")
                                st.rerun()
                    
                    elif provider == "Open Source LLM":
                        status_icon = "✅" if has_opensrc_key else "❌"
                        st.markdown(f"**OS Key**: {status_icon} | **URL**: {'✅' if has_opensrc_url else '❌'}")
                        with st.form(f"form_os_{model_name}"):
                            n_key = st.text_input("Open Source Key", type="password")
                            n_url = st.text_input("Open Source URL", value=opensrc_url if opensrc_url else "")
                            if st.form_submit_button("Speichern"):
                                if n_key: 
                                    db.update_opensrc_key(current_user, n_key)
                                db.update_opensrc_url(current_user, n_url)
                                st.success("Gespeichert!")
                                time.sleep(0.5)
                                st.rerun()
                            if st.form_submit_button("Löschen"):
                                db.update_opensrc_key(current_user, "")
                                db.update_opensrc_url(current_user, "")
                                st.rerun()

                # 3. Layout: Basis-Spalten (Links: Modelle, Rechts: Platz für Keys)
                base_col_left, base_col_right = st.columns([1, 2])

                with base_col_left:
                    st.caption("🤖 Modellauswahl")
                    sbhelp = "None"
                    if not st.session_state.notebook_mode:
                        cat_h = st.selectbox("Kategorie Helper:", list(CATEGORY_KEYWORDS.keys()), index=0, key="cat_h")
                        sbhelp = st.selectbox("Helper LLM", get_filtered_models(ALL_HELPER_MODELS, cat_h), index=0)
                    
                    cat_m = st.selectbox("Kategorie Main:", list(CATEGORY_KEYWORDS.keys()), index=0, key="cat_m")
                    sbmain = st.selectbox("Main LLM", get_filtered_models(ALL_MAIN_MODELS, cat_m), index=2)

                    if not st.session_state.notebook_mode:
                        st.caption(f"Gewählt: Python Modus mit: \n\n {sbhelp} -> {sbmain}")
                    else:
                        st.caption(f"Gewählt: Notebook Modus mit: \n\n {sbmain}")

                # 4. Dynamische Config-Spalten in base_col_right
                p_help = get_provider(sbhelp)
                p_main = get_provider(sbmain)

                with base_col_right:
                    # Fall: Zwei verschiedene Provider im Python Modus -> 2 Config Spalten
                    if not st.session_state.notebook_mode and p_help != p_main:
                        st.caption("🔑 API Konfiguration")
                        sub_col1, sub_col2 = st.columns(2)
                        with sub_col1:
                            st.caption(f"Helper: {p_help}")
                            render_config_form(sbhelp)
                        with sub_col2:
                            st.caption(f"Main: {p_main}")
                            render_config_form(sbmain)
                    
                    # Fall: Notebook Modus ODER gleiche Provider -> 1 Config Spalte
                    else:
                        st.caption("🔑 API Konfiguration")
                        if st.session_state.notebook_mode:
                            st.caption(f"Modell: {p_main}")
                        else:
                            st.caption(f"Gemeinsamer Provider: {p_main}")
                        render_config_form(sbmain)
            
            with st.container():
                st.write(f"👤 **{current_name}**")
                authenticator.logout("Abmelden", "sidebar")
                

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
    # Input Handling
    # Input Handling
    # ----------------------------------------
    # CHAT AREA - INPUT & ANALYSIS
    # ----------------------------------------
    if prompt := st.chat_input("Link zum Git Repository..."):
        # --- 0. FEHLER-CLEANUP ---
        current_chat_name = st.session_state.active_chat

        st.chat_message("user").write(prompt)
        
        # --- 1. SOFORTIGE UMBENENNUNG ---
        repo_name = extract_repo_name(prompt)
        working_chat_name = current_chat_name
        is_generic_name = current_chat_name.startswith("Neuer Chat") or current_chat_name.startswith("Chat ")

        if is_generic_name and repo_name:
            new_name = repo_name
            counter = 1
            while new_name in st.session_state.chats and new_name != current_chat_name:
                counter += 1
                new_name = f"{repo_name} ({counter})"
            
            if new_name != current_chat_name:
                db.rename_chat_fully(current_user, current_chat_name, new_name)
                chat_content = st.session_state.chats.pop(current_chat_name)
                st.session_state.chats[new_name] = chat_content
                st.session_state.active_chat = new_name
                working_chat_name = new_name
                st.toast(f"📂 Chat umbenannt zu: **{new_name}**")

        # --- 2. ANALYSE KONFIGURATION ---
        st.session_state.is_running = True
        st.session_state.abort_requested = False
        
        # --- HIER FEHLTE DIE DEFINITION ---
        def check_stop_callback():
            """Diese Funktion wird vom Backend aufgerufen, um zu prüfen ob der User Stop gedrückt hat."""
            return st.session_state.get("abort_requested", False)

        # Stop-Button anzeigen
        stop_col1, _ = st.columns([1, 4])
        with stop_col1:
            st.button("Analyse abbrechen", on_click=handle_abort, type="primary", use_container_width=True)
        
        status = st.status(f"⏳ Analysiere Repository in '{working_chat_name}'...", expanded=True)

        # API Keys zusammenstellen
        dec_gemini, dec_ollama, dec_gpt, user_opensrc_key, user_opensrc_url = db.get_decrypted_api_keys(current_user)
        api_keys = {
            "gemini": dec_gemini, 
            "ollama": dec_ollama, 
            "gpt": dec_gpt, 
            "opensrc_key": user_opensrc_key,
            "opensrc_url": user_opensrc_url,
            "scadsllm": SCADSLLM_KEY, 
            "scadsllm_base_url": SCADSLLM_HOST
        }
        model_config = {"helper": sbhelp, "main": sbmain}

        workflow_success = False
        response = ""
        metrics = {}
        
        # --- 3. WORKFLOW STARTEN ---
        try:
            if not st.session_state.notebook_mode: 
                result_data = main.main_workflow(
                    user_input=prompt, 
                    api_keys=api_keys, 
                    model_names=model_config,
                    status_callback=status.write,
                    check_stop=check_stop_callback 
                )
            else:  
                result_data = main.notebook_workflow(
                    input=prompt, 
                    api_keys=api_keys, 
                    model=model_config["main"],
                    status_callback=status.write,
                    check_stop=check_stop_callback 
                )  
            
            response = result_data["report"]
            metrics = result_data["metrics"]
            workflow_success = not (response.startswith("Error:") or response.startswith("Fehler"))
            
            if workflow_success:
                status.update(label="Analyse abgeschlossen!", state="complete", expanded=False)
            else:
                status.update(label="Analyse fehlgeschlagen", state="error", expanded=False)

        except InterruptedError:
            response = "Fehler: Die Analyse wurde vom Benutzer abgebrochen."
            status.update(label="❌ Abgebrochen", state="error", expanded=False)
            workflow_success = False
        except Exception as e:
            logging.error(f"CRITICAL ERROR: {traceback.format_exc()}")
            response = f"Fehler bei der Verarbeitung: {e}"
            status.update(label="⚠️ Fehler aufgetreten", state="error", expanded=False)
            workflow_success = False
        finally:
            st.session_state.is_running = False
            st.session_state.abort_requested = False

        # --- 4. ANZEIGE & SPEICHERN ---
        if workflow_success:
            # NUR bei Erfolg wird die Assistant-Bubble und der Container geöffnet
            with st.chat_message("assistant"):
                st.write("Antwort generiert:")
                with st.container(height=500):
                    render_text_with_mermaid(response, should_stream=False)
                new_id = db.insert_exchange(
                    question=prompt,
                    answer=response,
                    feedback=np.nan,
                    username=current_user,
                    chat_name=working_chat_name, 
                    helper_used=metrics.get("helper_model", sbhelp),
                    main_used=metrics.get("main_model", sbmain),
                    total_time=str(metrics.get("total_time", "0")),
                    helper_time=str(metrics.get("helper_time", "0")),
                    main_time=str(metrics.get("main_time", "0")),
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
                    "datetime": datetime.now() 
                }
                if working_chat_name in st.session_state.chats:
                    st.session_state.chats[working_chat_name]["exchanges"].append(new_ex)  
        else:
            # Im Fehlerfall wird NUR die Error-Box außerhalb der Assistant-Bubble angezeigt
            st.error(response)
            new_id = f"session_{uuid.uuid4()}"
            new_ex = {
                    "_id": new_id, 
                    "question": prompt,
                    "answer": response,
                    "feedback": np.nan,
                    "feedback_message": "",
                    "chat_name": working_chat_name,
                    "username": current_user,
                    "datetime": datetime.now() 
                }
            if working_chat_name in st.session_state.chats:
                    st.session_state.chats[working_chat_name]["exchanges"].append(new_ex)
        st.rerun()
