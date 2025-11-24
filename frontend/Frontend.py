import time
import numpy as np
from datetime import datetime
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import database.db as db
import streamlit as st
import streamlit_authenticator as stauth
import backend
import result

users = db.fetch_all_users()

credentials = {"usernames": {}}

for user in users:
    credentials["usernames"][user["_id"]] = {
        "name": user["name"],
        "password": user["hashed_password"],  
        "gemini_api_key": user["gemini_api_key"],
        "ollama_base_url": user["ollama_base_url"]
    }

authenticator = stauth.Authenticate(credentials, "Repo-Agent","abcdef",cookie_expiry_days=30
)

authenticator.login("main", key="Login")


if st.session_state["authentication_status"]==False:
    st.error("Username/password is incorrect")
elif st.session_state["authentication_status"]==None:
    st.warning("Please enter your username and password")
if st.session_state["authentication_status"]:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    report_path = os.path.join(BASE_DIR, "..", "result", 
        "report_24_11_2025_11-58-47_Helper_gemini-2.0-flash-lite_MainLLM_gemini-2.5-pro.md"
    )

    with open(report_path, "r", encoding="utf-8") as f:
        response = f.read()


    load_dotenv()
    MONGO_KEY = os.getenv("MONGO_KEY")
    client=MongoClient(MONGO_KEY)
    dbex = client.AI4AA.exchanges

    # login 


    # chats initialisierung 
    if "chats" not in st.session_state:
        st.session_state.chats = {"Chat 1": {"exchanges": []}}
    if "active_chat" not in st.session_state:
        st.session_state.active_chat = "Chat 1"



    # sidebar
    if st.sidebar.button("➕ New Chat "):
        new_name= f"Chat {len(st.session_state.chats)+1}"     
        st.session_state.chats[new_name] = {"exchanges": []}
        st.session_state.active_chat = new_name

    st.sidebar.markdown("---")
    st.sidebar.title("💬 Chats")

    for chat_name in st.session_state.chats:
        if st.sidebar.button(chat_name, key=f"btn_{chat_name}"):
            st.session_state.active_chat=chat_name

    st.sidebar.markdown("---")

    st.sidebar.write(f"Active Chat: **{st.session_state.active_chat}**")

    st.sidebar.markdown("---")  
    sbhelp= st.sidebar.selectbox("Select Model for Helper LLM", 
        ("gemini-2.0-flash-lite","gemini-flash-latest","gemini-2.5-pro","gemini-2.0-flash","gemini-2.5-flash-lite", "llama3",),     
    )
    sbmain=st.sidebar.selectbox("Select Model for Main LLM", 
        ("gemini-2.0-flash-lite","gemini-flash-latest","gemini-2.5-pro","gemini-2.0-flash","gemini-2.5-flash-lite", "llama3"),
    )
    if sbhelp==sbmain and sbmain=="llama3":
        st.sidebar.text_input("Set Llama 3 Base URL",)
    elif sbhelp==sbmain and sbmain!="llama3":
        st.sidebar.text_input("Set Gemini API Key",)
    else:
        st.sidebar.text_input("Set Gemini API Key",)
        st.sidebar.text_input("Set Llama 3 Base URL",)




    # aktueller chat
    active = st.session_state.active_chat
    chat= st.session_state.chats[active]
    st.title(st.session_state.active_chat)


    # Exchanges anzeigen
    for ex in chat["exchanges"]:
        st.chat_message("user").write(ex["question"])
        st.chat_message("assistant").write(ex["answer"])

        if np.isnan(ex["feedback"]):
            col1, col2 = st.columns([0.1, 0.1], gap=None)  # sehr schmale Spalten
            with col1:
                if st.button("👍", key=f"up_{ex['id']}"):
                    ex["feedback"] = 1
                    st.rerun()
            with col2:
                if st.button("👎", key=f"down_{ex['id']}"):
                    ex["feedback"] = 0
                    st.rerun()   
            
            



    # React to user input
    if prompt := st.chat_input("Put in Link of Repository"):
        #print message and store it in chats
        st.chat_message("user").write(prompt)
        # Statusanzeige
        status= st.status("⏳ Generiere Antwort...", expanded=True)

        # Import backend.main only when needed to avoid import-time failures
        """try:
            from backend.main import main_workflow
        except Exception as e:
            st.chat_message("assistant").write(f"Import error: {e}")
            raise

        try:
            response = main_workflow(prompt)
        except Exception as e:
            response = f"Fehler bei der Verarbeitung: {e}"""
        with st.chat_message("assistant"):
             a = st.container(height=500)
             a.markdown(response)

        new_id = len(chat["exchanges"])+1
        chat["exchanges"].append({
            "id": new_id,
            "question": prompt,
            "answer":response,
            "feedback": np.nan,
            'datetime': datetime.now()
        })

        st.rerun()

    "session_state" , st.session_state

    if "saved_exchanges" not in st.session_state:
        st.session_state.saved_exchanges = set() 


    all_rated = [
        ex
        for chat_name, chat in st.session_state.chats.items()
        for ex in chat["exchanges"]
        if not np.isnan(ex["feedback"])
    ]

    for ex in all_rated:
        key = f"{ex['question']}_{ex['datetime']}"
        if key not in st.session_state.saved_exchanges:
            dbex.insert_one(ex)
            st.session_state.saved_exchanges.add(key)

        

    print(all_rated)