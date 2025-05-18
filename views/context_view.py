import streamlit as st
from components.navigation import navigation_controls

if 'context' not in st.session_state:
    st.session_state['context'] = None

def render():
    st.subheader("Step 5: Event / Context")
    st.image(st.session_state.image_path)

    context = st.text_input("Where is the person going? (e.g., conference, party, office)", value=st.session_state.context or "")
    if context:
        st.session_state.context = context

    navigation_controls(
        current_step='context',
        back_step='colors',
        next_step='done' if st.session_state.context else None
    )
