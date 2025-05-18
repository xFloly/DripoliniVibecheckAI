import streamlit as st
from steps import (
    step1_upload,
    step2_emotion,
    step3_color,
    step4_context,
    step5_suggestions,
    step6_virtual_tryon,
)

# Inicjalizacja stanu sesji
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'user_image' not in st.session_state:
    st.session_state.user_image = None
if 'emotion' not in st.session_state:
    st.session_state.emotion = None
if 'color_palette' not in st.session_state:
    st.session_state.color_palette = None
if 'context' not in st.session_state:
    st.session_state.context = None
if 'suggested_clothes' not in st.session_state:
    st.session_state.suggested_clothes = []
if 'selected_cloth' not in st.session_state:
    st.session_state.selected_cloth = None
if 'result_image' not in st.session_state:
    st.session_state.result_image = None

st.title("👗 Wirtualna Przymierzalnia z CatVTON")

# Przepływ aplikacji
if st.session_state.step == 1:
    step1_upload.run()
elif st.session_state.step == 2:
    step2_emotion.run()
elif st.session_state.step == 3:
    step3_color.run()
elif st.session_state.step == 4:
    step4_context.run()
elif st.session_state.step == 5:
    step5_suggestions.run()
elif st.session_state.step == 6:
    step6_virtual_tryon.run()
