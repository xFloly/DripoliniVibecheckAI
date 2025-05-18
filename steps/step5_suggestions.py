import streamlit as st
from utils.clothing_db import get_clothing_suggestions
from steps.step1_upload import display_user_image

def run():
    st.header("Krok 5: Propozycje ubrań")
    display_user_image()
    if all([st.session_state.emotion, st.session_state.color_palette, st.session_state.context]):
        suggestions = get_clothing_suggestions(
            st.session_state.emotion,
            st.session_state.color_palette,
            st.session_state.context
        )
        st.session_state.suggested_clothes = suggestions
        for idx, cloth in enumerate(suggestions):
            st.image(cloth['image'], caption=cloth['description'], use_container_width=True)
            if st.button(f"Wybierz {idx+1}"):
                st.session_state.selected_cloth = cloth
                st.session_state.step = 6
                break
    else:
        st.warning("Proszę przejść przez poprzednie kroki.")
