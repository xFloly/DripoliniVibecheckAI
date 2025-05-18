import streamlit as st

def navigation_controls(current_step, back_step=None,next_step=None):
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if back_step and st.button("⬅️ Back"):
            st.session_state.step = back_step
            st.experimental_rerun()

    with col2:
        if st.button("🔁 Restart"):
            for key in ['step', 'image_path', 'outfit_desc', 'emotion', 'colors', 'context']:
                st.session_state[key] = None
            st.session_state.step = 'start'
            st.experimental_rerun()
    
    with col3:
        if next_step and st.button("➡️ Next"):
            st.session_state.step = next_step
            st.experimental_rerun()