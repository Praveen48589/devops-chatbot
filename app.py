import streamlit as st
from chatbot import devops_chatbot

st.set_page_config(page_title="DevOps Chatbot", page_icon="🤖")
st.title("🤖 DevOps Chatbot")

user_input = st.text_input("Ask me something:")

if st.button("Send"):
    response = devops_chatbot(user_input)
    st.text_area("Bot:", response, height=200)
