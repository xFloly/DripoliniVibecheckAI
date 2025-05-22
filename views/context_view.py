import streamlit as st

from components.navigation import navigation_controls



def render():
    if 'context' not in st.session_state:
        st.session_state['context'] = None

    st.subheader("Step 5: Event / Context")
    
    st.markdown("---")

    left_col, right_col = st.columns([1, 2], gap="large")

    with left_col:
        st.image(
            st.session_state.image_path,
            caption="Your Photo",
            width=250
        )

    with right_col:
        st.markdown("#### Where is the person going?")
        context_input = st.text_input(
            label="",
            value=st.session_state.context or "",
            placeholder="e.g., conference, party, office"
        )

        if context_input:
            st.session_state.context = context_input

    navigation_controls(
        current_step='context',
        back_step='colors',
        next_step='summary' if st.session_state.context else None
    )
