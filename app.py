from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

st.set_page_config(page_title="Chatbot", page_icon="🤖")
st.title("🤖 Chatbot")
st.write("----Welcome type 0 to exit nahi, ab UI hai----")

model = ChatGroq(model="openai/gpt-oss-20b")

if "message" not in st.session_state:
    st.session_state.message = [SystemMessage(content="You are a helpful ai agent")]

# purane messages dikhana
for msg in st.session_state.message:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").write(msg.content)

prompt = st.chat_input("you:")

if prompt:
    if prompt == "0":
        st.write("Application closed")
        st.stop()
    
    st.session_state.message.append(HumanMessage(content=prompt))
    st.chat_message("user").write(prompt)

    response = model.invoke(st.session_state.message)
    st.session_state.message.append(AIMessage(content=response.content))
    st.chat_message("assistant").write(response.content)

# last me tera wala print(message) ka kaam
with st.expander("Full message history"):
    st.write(st.session_state.message)