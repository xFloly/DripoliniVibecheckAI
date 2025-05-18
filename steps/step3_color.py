import streamlit as st
from utils.color import analyze_color
from steps.step1_upload import display_user_image

def run():
    st.header("Krok 3: Analiza kolorystyki ubrań")
    display_user_image()
    if st.session_state.user_image is not None:
        color_palette = analyze_color(st.session_state.user_image)
        st.session_state.color_palette = color_palette
        st.write(f"Dominujące kolory: {', '.join(color_palette)}")
        if st.button("Dalej"):
            st.session_state.step = 4
    else:
        st.warning("Proszę wczytać zdjęcie w poprzednim kroku.")
