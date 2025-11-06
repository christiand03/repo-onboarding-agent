import streamlit as st

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
    chat["messages"].append({"role":"user", "content":prompt})
    response = f"Echo: {prompt}" #platzhalter
    # print response and store it in chats
    chat["messages"].append({"role":"assistant", "content":prompt})
    st.rerun()

"st.session_state object:", st.session_state

