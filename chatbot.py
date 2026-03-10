import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
st.set_page_config(
    page_title="Groq Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Groq AI Chatbot")
model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.5
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


prompt = st.chat_input("Ask anything...")

if prompt:


    st.chat_message("user").write(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })


    response = model.invoke(prompt)

    with st.chat_message("assistant"):
        st.write(response.content)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response.content
    })