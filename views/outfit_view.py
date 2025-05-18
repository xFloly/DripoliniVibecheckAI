import streamlit as st
from components.navigation import navigation_controls
from utils.gemini_api import describe_outfit

if 'outfit_desc' not in st.session_state:
    st.session_state['outfit_desc'] = None

def render():
    st.subheader("Step 2: Outfit Description")
    st.image(st.session_state.image_path)

    if st.session_state.outfit_desc is None:
        with st.spinner("Describing outfit..."):
            st.session_state.outfit_desc = describe_outfit(st.session_state.image_path)

    st.markdown(f"🧥 Outfit: {st.session_state.outfit_desc}")

    navigation_controls(
        current_step='describe_outfit',
        back_step='upload',
        next_step='emotion' if st.session_state.outfit_desc else None
    )
