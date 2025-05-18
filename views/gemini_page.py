import streamlit as st
from utils.gemini_assistant import get_gemini_response

def render():
    if st.button("↩️ Wróć do menu"):
        st.session_state.page = "main"
        st.rerun()
        st.stop() 

    st.header("😊 Twój asystent AI")
    st.markdown("System pomagający w ocenie twojego ubrania.")

    if st.button("▶️ Uruchom asystenta"):
        get_gemini_response()