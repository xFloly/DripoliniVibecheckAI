import streamlit as st
from utils.context import analyze_context
from steps.step1_upload import display_user_image

def run():
    st.header("Krok 4: Analiza kontekstu zdjęcia i nastroju")
    display_user_image()
    if st.session_state.user_image is not None:
        context = analyze_context(st.session_state.user_image)
        st.session_state.context = context
        st.write(f"Kontekst zdjęcia: {context}")
        if st.button("Dalej"):
            st.session_state.step = 5
    else:
        st.warning("Proszę wczytać zdjęcie w poprzednim kroku.")
