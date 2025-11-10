import streamlit as st
import time

# chats initialisierung 
if "chats" not in st.session_state:
    st.session_state.chats = {"Chat 1": {"messages": []}}
if "active_chat" not in st.session_state:
    st.session_state.active_chat = "Chat 1"



# sidebar
if st.sidebar.button("➕ New Chat "):
    new_name= f"Chat {len(st.session_state.chats)+1}"     
    st.session_state.chats[new_name] = {"messages": []}
    st.session_state.active_chat = new_name
st.sidebar.markdown("---")
st.sidebar.title("💬 Chats")
# liste Chats
for chat_name in st.session_state.chats:
    if st.sidebar.button(chat_name, key=f"btn_{chat_name}"):
        st.session_state.active_chat=chat_name

st.sidebar.markdown("---")

st.sidebar.write(f"Active Chat: **{st.session_state.active_chat}**")


# aktueller chat
active = st.session_state.active_chat
chat= st.session_state.chats[active]
st.title(st.session_state.active_chat)


for message in chat["messages"]:
   st.chat_message(message["role"]).write(message["content"])

# React to user input
if prompt := st.chat_input("Put in Link of Repository"):
    #print message and store it in chats
    st.chat_message("user").write(prompt)
    chat["messages"].append({"role":"user", "content":prompt})
    
    # Statusanzeige
    status= st.status("⏳ Generiere Antwort...", expanded=True)
    time.sleep(2)  # Delay simulieren
    
    response = f"Echo: {prompt}"
    st.chat_message("assistant").write(response)
    chat["messages"].append({"role":"assistant", "content":response})

    st.rerun()

#"session_state" , st.session_state

