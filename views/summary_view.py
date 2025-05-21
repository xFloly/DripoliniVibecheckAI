import streamlit as st
from components.navigation import navigation_controls

def render():
    st.subheader("✅ Summary")
    st.image(st.session_state.image_path)

    st.markdown(f"**Outfit:** {st.session_state.outfit_desc}")
    st.markdown(f"**Emotion:** {st.session_state.emotion}")
    st.markdown(f"**Color Palette:** {', '.join(st.session_state.colors)}")
    st.markdown(f"**Context:** {st.session_state.context}")

    navigation_controls(
        current_step='done',
        back_step='context',
        next_step='propose'
    )
