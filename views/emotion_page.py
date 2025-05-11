import streamlit as st
from utils.emotion_recognition import run_emotion_detection_streamlit

def render():
    if st.button("↩️ Wróć do menu"):
        st.session_state.page = "main"
        st.rerun()
        st.stop() 

    st.header("😊 Analiza emocji w czasie rzeczywistym")
    st.markdown("System analizuje Twoją mimikę i rozpoznaje dominującą emocję co sekundę.")

    if st.button("▶️ Uruchom kamerę"):
        run_emotion_detection_streamlit()