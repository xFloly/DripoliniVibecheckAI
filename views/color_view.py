import streamlit as st
from utils.color import extract_dominant_colors
from components.navigation import navigation_controls

if 'colors' not in st.session_state:
    st.session_state['colors'] = None
    

def render():
    st.subheader("Step 4: Color Palette")
    st.image(st.session_state.image_path)

    if st.session_state.colors is None:
        with st.spinner("Extracting colors..."):
            st.session_state.colors = extract_dominant_colors(st.session_state.image_path)

    st.markdown(f"🎨 Dominant colors: {', '.join(st.session_state.colors)}")

    # Only show Save button if colors were extracted
    if st.session_state.colors:
        if st.button("✅ Save & Describe Context"):
            st.session_state.step = 'context'
            st.rerun()
    else:
        st.warning("Please wait for color extraction before continuing.")

    # "Next" only available if colors are set
    navigation_controls(
        current_step='colors',
        back_step='emotion',
        next_step='context' if st.session_state.colors else None
    )
