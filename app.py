import streamlit as st
from views import upload_view, outfit_view, emotion_view, color_view, context_view, summary_view

# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 'start'

st.title("👗 AI Stylist: Virtual Fashion Assistant")

if st.session_state.step == 'start':
    st.subheader("Welcome to your AI Styling Assistant")
    if st.button("🚀 Begin Styling"):
        st.session_state.step = 'upload'
        st.experimental_rerun()

elif st.session_state.step == 'upload':
    upload_view.render()

elif st.session_state.step == 'describe_outfit':
    outfit_view.render()

elif st.session_state.step == 'emotion':
    emotion_view.render()

elif st.session_state.step == 'colors':
    color_view.render()

elif st.session_state.step == 'context':
    context_view.render()

elif st.session_state.step == 'done':
    summary_view.render()