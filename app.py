import streamlit as st
from views import main_menu, emotion_page, tryon_page, color_page

st.set_page_config(page_title="Informatyka Afektywna", layout="centered")

# Inicjalizacja widoku
if "page" not in st.session_state:
    st.session_state.page = "main"

# Routing
if st.session_state.page == "main":
    main_menu.render()
elif st.session_state.page == "emotion":
    emotion_page.render()
elif st.session_state.page == "tryon":
    tryon_page.render()
elif st.session_state.page == "color":
    color_page.render()
