"""
chatbot_app.py

Streamlit web version of the DecodeLabs Project 1 rule-based chatbot.
Run with: streamlit run chatbot_app.py
"""

import streamlit as st

from chatbot_logic import get_response, is_exit_command

st.set_page_config(page_title="Rule-Based Chatbot", page_icon="🤖")

st.title("🤖 Rule-Based Chatbot — DecodeLabs Project 1")
st.caption("A simple if-else / dictionary-based chatbot. Type 'help' to see available commands.")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.chat_input("Type your message...")

if user_input:
    reply = get_response(user_input)
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Chatbot", reply))

for sender, msg in st.session_state.history:
    role = "user" if sender == "You" else "assistant"
    with st.chat_message(role):
        st.write(msg)
