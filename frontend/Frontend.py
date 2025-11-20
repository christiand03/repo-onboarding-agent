import streamlit as st
import time
import numpy as np
from datetime import datetime
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_KEY = os.getenv("MONGO_KEY")
client=MongoClient(MONGO_KEY)
dbex = client.AI4AA.exchanges

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
    time.sleep(2)  # Delay simulieren
    
    response = f"Echo: {prompt}"
    st.chat_message("assistant").write(response)

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