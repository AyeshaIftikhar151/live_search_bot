"""
webui.py
--------
Streamlit interface for the high-accuracy live search chatbot.
"""

import streamlit as st
from search_bot import live_search_chatbot

st.set_page_config(page_title="Live Search Chatbot", page_icon="🤖", layout="wide")
st.title("🤖 Live Search Chatbot")
st.write("Ask any question. The bot searches Google + Gemini and explains contradictions with sources.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display previous messages
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
if prompt := st.chat_input("Type your question here..."):
    # Add user message
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Bot response with spinner
    with st.chat_message("assistant"):
        with st.spinner("Searching and thinking..."):
            response = live_search_chatbot(prompt)
            st.markdown(response)

    # Save bot reply
    st.session_state["messages"].append({"role": "assistant", "content": response})
