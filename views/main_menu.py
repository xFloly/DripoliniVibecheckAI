import streamlit as st

def render():
    st.title("🧠 Informatyka Afektywna")
    st.subheader("Interaktywna aplikacja łącząca emocje i wizualną analizę stylu")
    st.markdown("---")

    # Stylizacja przycisków
    st.markdown("""
    <style>
        div.stButton > button {
            background-color: #9b59b6;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.6em 1.2em;
            font-size: 1rem;
            transition: background-color 0.3s ease;
        }

        div.stButton > button:hover {
            background-color: #f1c40f;
            color: black;
        }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("👕 Wirtualne przymierzanie"):
            st.session_state.page = "tryon"
            st.experimental_rerun()
    with col2:
        if st.button("😊 Analiza emocji"):
            st.session_state.page = "emotion"
            st.experimental_rerun()
    with col3:
        if st.button("🎨 Analiza kolorów"):
            st.session_state.page = "color"
            st.experimental_rerun()
