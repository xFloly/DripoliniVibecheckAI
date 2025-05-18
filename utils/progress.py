import streamlit as st

def is_step_complete(step_key):
    """
    Returns True if the given session state key is not None (or not empty if string).
    """
    value = st.session_state.get(step_key, None)
    if isinstance(value, str):
        return value.strip() != ""
    return value is not None