import streamlit as st
from components.navigation import navigation_controls
# from utils.gemini_api import describe_emotion
from utils.emotion import analyze_emotion

if 'emotion' not in st.session_state:
    st.session_state['emotion'] = None

def render():
    st.subheader("Step 3: Emotion Detection")
    st.image(st.session_state.image_path)

    if st.session_state.emotion is None:
        with st.spinner("Analyzing emotion..."):
            st.session_state.emotion = analyze_emotion(st.session_state.image_path)

    st.markdown(f"😊 Emotion: {st.session_state.emotion}")

    navigation_controls(
        current_step='emotion',
        back_step='describe_outfit',
        next_step='colors' if st.session_state.emotion else None
    )
