import streamlit as st
from utils.emotion import analyze_emotion
from steps.step1_upload import display_user_image

def run():
    st.header("Krok 2: Analiza emocji")
    display_user_image()
    if st.session_state.user_image is not None:
        emotion = analyze_emotion(st.session_state.user_image)
        st.session_state.emotion = emotion
        st.write(f"Rozpoznana emocja: {emotion}")
        if st.button("Dalej"):
            st.session_state.step = 3
    else:
        st.warning("Proszę wczytać zdjęcie w poprzednim kroku.")
