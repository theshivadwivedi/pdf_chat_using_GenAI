import os
import streamlit as st

def get_google_api_key():
    # Streamlit Cloud
    if "GOOGLE_API_KEY" in st.secrets:
        return st.secrets["GOOGLE_API_KEY"]

    # Local development (.env)
    return os.getenv("GOOGLE_API_KEY")
