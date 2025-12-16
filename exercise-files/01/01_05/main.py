from colorama import Fore
import streamlit as st
from pathlib import Path    
import tempfile
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

client = OpenAI()


# Custom style 
st.markdown(
    """
    <style>
    p {
        color: #3498db;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>
    div[data-testid="stElementContainer"] {
       width: auto
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Streamlit App
st.title("🤖 Multimodel Q&A Chatbot")  # Add a title

# User input
with st.form("chat_form"):
    user_input = st.text_input("Type something")
    submit_button = st.form_submit_button("▶ Send")

if submit_button:
    with st.spinner("Generating response..."):
        pass
