import numpy as np
from datetime import datetime
import time
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import sys
import logging
import traceback
import re
from streamlit_mermaid import st_mermaid

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend import main
import database.db as db
import streamlit as st
import streamlit_authenticator as stauth


load_dotenv()
MONGO_KEY = os.getenv("MONGO_KEY")
client=MongoClient(MONGO_KEY)

# --- load data from db ---
def load_data_from_db(username: str):
    """Lädt existierende Chats aus der DB in den Session State"""
    if "data_loaded" not in st.session_state:
        st.session_state.chats = {}
        db_exchanges = db.fetch_exchanges_by_user(username)
        for ex in db_exchanges:
            c_name = ex.get("chat_name", "Unbenannt")
            if c_name not in st.session_state.chats:
                st.session_state.chats[c_name] = {"exchanges": []}
            if "feedback" not in ex or ex["feedback"] is None:
                ex["feedback"] = np.nan
            st.session_state.chats[c_name]["exchanges"].append(ex)
            
        if not st.session_state.chats:
            st.session_state.chats["Chat 1"] = {"exchanges": []}
            st.session_state.active_chat = "Chat 1"
        else:
            first_chat = list(st.session_state.chats.keys())[0]
            if "active_chat" not in st.session_state:
                st.session_state.active_chat = first_chat
        
        st.session_state.data_loaded = True
    
# --- handle feedback changes ---
def handle_feedback_change(ex, val):
    """Update Feedback in State und DB"""
    ex["feedback"] = val
    # DB Update
    db.update_exchange_feedback(ex["_id"], val)
    st.rerun()


def handle_delete_exchange(chat_name, ex):
    """Löscht Exchange aus State und DB"""
    # DB Delete
    db.delete_exchange_by_id(ex["_id"])
    # State Delete
    st.session_state.chats[chat_name]["exchanges"].remove(ex)
    st.rerun()

def handle_delete_chat(username, chat_name):
    """Löscht kompletten Chat"""
    # DB Delete
    db.delete_chats_by_user(username, chat_name)
    # State Delete
    del st.session_state.chats[chat_name]
    
    # Neuen aktiven Chat setzen oder Default erstellen
    if len(st.session_state.chats) > 0:
        st.session_state.active_chat = list(st.session_state.chats.keys())[0]
    else:
        st.session_state.chats["Chat 1"] = {"exchanges": []}
        st.session_state.active_chat = "Chat 1"
    st.rerun()

# --- Render Mermaid Diagram ---
def render_text_with_mermaid(markdown_text):
    """
    Splittet den Text bei ```mermaid Blöcken und rendert Diagramme grafisch.
    """
    if not markdown_text:
        return

    # Regex: Findet alles zwischen ```mermaid und ```
    parts = re.split(r"```mermaid\s+(.*?)\s+```", markdown_text, flags=re.DOTALL)

    for i, part in enumerate(parts):
        # Gerade Indizes = Text
        if i % 2 == 0:
            if part.strip():
                st.markdown(part)
        # Ungerade Indizes = Mermaid Code
        else:
            try:
                st_mermaid(part, key=f"mermaid_{hash(part)}_{i}")
            except Exception:
                st.code(part, language="mermaid")

# --- Render Exchanges ---
def render_exchange(ex, current_chat_name):
    """
    Anzeige einer Nachricht mit Toolbar für Feedback, Download, Nachricht und Löschen.
    """
    st.chat_message("user").write(ex["question"])
    
    with st.chat_message("assistant"):
        # Layout: Buttons kompakt links
        cols = st.columns([3, 3, 3, 3, 3, 15])
        
        with cols[0]:
            type_primary = ex.get("feedback") == 1
            if st.button("👍", key=f"up_{ex['_id']}", type="primary" if type_primary else "secondary", help="Positiv"):
                handle_feedback_change(ex, 1)

        with cols[1]:
            type_primary = ex.get("feedback") == 0
            if st.button("👎", key=f"down_{ex['_id']}", type="primary" if type_primary else "secondary", help="Negativ"):
                handle_feedback_change(ex, 0)

        with cols[2]:
            with st.popover("💬", help="Feedback schreiben"):
                msg = st.text_area("Feedback Nachricht:", value=ex.get("feedback_message", ""), key=f"txt_{ex['_id']}")
                if st.button("Speichern", key=f"save_{ex['_id']}"):
                    ex["feedback_message"] = msg
                    db.update_exchange_feedback_message(ex["_id"], msg)
                    st.success("Gespeichert!")
                    time.sleep(1)
                    st.rerun()

        with cols[3]:
            st.download_button(
                label="📥",
                data=ex["answer"],
                file_name=f"response_{ex['_id']}.md",
                mime="text/markdown",
                key=f"dl_{ex['_id']}",
                help="Download Markdown"
            )

        with cols[4]:
            if st.button("🗑️", key=f"del_{ex['_id']}", help="Nachricht löschen"):
                handle_delete_exchange(current_chat_name, ex)

        with cols[5]:
             if ex.get("feedback") == 1:
                 st.caption("Positiv bewertet")
             elif ex.get("feedback") == 0:
                 st.caption("Negativ bewertet")

        # Inhalt Scrollbar
        with st.container(height=500):
             render_text_with_mermaid(ex["answer"])

# --- Login ---
users = db.fetch_all_users()
credentials = {"usernames": {}}

for user in users:
    credentials["usernames"][user["_id"]] = {
        "name": user["name"],
        "password": user["hashed_password"],  
        "gemini_api_key": user.get("gemini_api_key", ""),
        "ollama_base_url": user.get("ollama_base_url", "")
    }

authenticator = stauth.Authenticate(
    credentials, 
    "Repo-Agent",
    "abcdef",
    cookie_expiry_days=30
)

authenticator.login("main", key="Login")


if st.session_state["authentication_status"]==False:
    st.error("Username/password is incorrect")
elif st.session_state["authentication_status"]==None:
    st.warning("Please enter your username and password")

# App Content
if st.session_state["authentication_status"]:

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    current_user = st.session_state["username"]
    current_name = st.session_state["name"]

    # 1. Daten laden (Historie)
    load_data_from_db(current_user)

    # 2. Sidebar Logic
    with st.sidebar:
        st.write(f"User: **{st.session_state['name']}**")
        authenticator.logout("Logout", "sidebar")
        st.markdown("---")

        # Chat Management
        if st.button("➕ New Chat", use_container_width=True):
            new_name = f"Chat {len(st.session_state.chats)+1}"     
            st.session_state.chats[new_name] = {"exchanges": []}
            st.session_state.active_chat = new_name
            st.rerun()

        st.markdown("### 💬 Chats")
        for chat_name in list(st.session_state.chats.keys()):
            if st.button(chat_name, key=f"btn_{chat_name}", use_container_width=True, 
                         type="primary" if st.session_state.active_chat == chat_name else "secondary"):
                st.session_state.active_chat = chat_name
                st.rerun()
        
        st.markdown("---")
        
        # Aktiven Chat löschen Button
        if st.button("🗑️ Aktuellen Chat löschen", type="primary"):
            handle_delete_chat(current_user, st.session_state.active_chat)

        st.markdown("---")  
        st.markdown("### ⚙️ Einstellungen")

        # LLM Auswahl
        sbhelp = st.selectbox("Helper LLM", 
            ("gemini-2.0-flash-lite","gemini-flash-latest","gemini-2.5-pro","llama3"),     
        )
        sbmain = st.selectbox("Main LLM", 
            ("gemini-2.0-flash-lite","gemini-flash-latest","gemini-2.5-pro","llama3"),
        )

        # API Keys & URLs Handling
        gemini_key, ollama_url = db.get_decrypted_api_keys(current_user)
        has_gemini = bool(gemini_key)
        has_ollama = bool(ollama_url)

        st.caption("API Keys Configuration")

        # --- Gemini Formular ---
        if sbhelp.startswith("gemini") or sbmain.startswith("gemini"):
            status_icon = "✅" if has_gemini else "❌"
            st.markdown(f"**Gemini Key**: {status_icon} {'Gesetzt' if has_gemini else 'Fehlt'}")
            
            with st.form("gemini_form"):
                new_gemini = st.text_input("Gemini Key ändern", type="password")
                submitted = st.form_submit_button("Speichern")
                
                if submitted and new_gemini:
                    db.update_gemini_key(current_user, new_gemini)
                    st.success("Gemini Key gespeichert!")
                    time.sleep(0.5)
                    st.rerun() 

        # --- Ollama Formular ---
        if sbhelp == "llama3" or sbmain == "llama3":
            status_icon = "✅" if has_ollama else "❌"
            st.markdown(f"**Llama URL**: {status_icon} {'Gesetzt' if has_ollama else 'Fehlt'}")
            
            # [CHANGE] Hier verwenden wir jetzt die korrekt geladene Variable ollama_url
            current_url = ollama_url if ollama_url else ""
            
            with st.form("ollama_form"):
                new_ollama = st.text_input("Llama Base URL ändern", value=current_url)
                submitted = st.form_submit_button("Speichern")
                
                if submitted:
                    if new_ollama != current_url:
                        db.update_ollama_url(current_user, new_ollama)
                        st.success("Ollama URL gespeichert!")
                        time.sleep(0.5)
                        st.rerun()


    # --- active chat ---
    active_chat_name = st.session_state.active_chat
    chat_data = st.session_state.chats[active_chat_name]
    
    # --- Main Area ---
    st.title(f"👋 Hallo, {current_name}!")
    st.caption(f"Aktueller Chat: **{active_chat_name}**")
    st.markdown("---")

    # --- Vorhandene Nachrichten rendern ---
    for ex in chat_data["exchanges"]:
        render_exchange(ex, active_chat_name)

    # --- Neue Nachricht ---
    if prompt := st.chat_input("Put in Link of Repository"):
        st.chat_message("user").write(prompt)
        
        # [CHANGE] Status wird hier erstellt
        status = st.status("⏳ Generating response...", expanded=True)

        # 1. API Keys und Modelle vorbereiten
        dec_gemini, dec_ollama = db.get_decrypted_api_keys(current_user)
        api_keys = {
            "gemini": dec_gemini,
            "ollama": dec_ollama
        }
        
        model_config = {
            "helper": sbhelp,
            "main": sbmain
        }

        try:
            # [CHANGE] Wir übergeben 'status.write' an das Backend
            result_data = main.main_workflow(
                input=prompt, 
                api_keys=api_keys, 
                model_names=model_config,
                status_callback=status.write 
            )
            
            logging.info(f"Workflow finished. Keys in result: {result_data.keys()}")
            response = result_data["report"]
            metrics = result_data["metrics"]
            
        except Exception as e:
            error_details = traceback.format_exc()
            logging.error(f"CRITICAL ERROR in Frontend: {error_details}")
            response = f"Fehler bei der Verarbeitung: {e}"
            metrics = {
                "helper_time": "0", "main_time": "0", "total_time": "0",
                "helper_model": sbhelp, "main_model": sbmain
            }
        
        # [CHANGE] Status abschließen
        status.update(label="Fertig!", state="complete", expanded=False)
        
        with st.chat_message("assistant"):
            with st.container(height=500):
                render_text_with_mermaid(response)       

        # 3. Datenbank Speichern
        new_id = db.insert_exchange(
            question=prompt,
            answer=response,
            feedback=np.nan,
            username=current_user,
            chat_name=active_chat_name,
            helper_used=metrics["helper_model"],
            main_used=metrics["main_model"],
            total_time=str(metrics["total_time"]),
            helper_time=str(metrics["helper_time"]),
            main_time=str(metrics["main_time"])
        )
        
        # 4. Session State Update
        new_ex = {
            "_id": new_id, 
            "question": prompt,
            "answer": response,
            "feedback": np.nan,
            "feedback_message": "",
            "chat_name": active_chat_name,
            "username": current_user,
            "helper_used": metrics["helper_model"],
            "main_used": metrics["main_model"],
            "datetime": datetime.now()
        }
        
        chat_data["exchanges"].append(new_ex)

        # 5. Rerun
        st.rerun()