import streamlit as st

def render():
    # Styl aplikacji – stały jasny motyw
    st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
            background-color: #ffffff;
            color: #222;
        }

        section[data-testid="stSidebar"] > div:first-child {
            padding-top: 2rem;
        }

        .stButton > button {
            background-color: #9b59b6;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 0.6em 1em;
            font-size: 1rem;
            font-weight: 600;
            width: 100%;
            margin-bottom: 0.8rem;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
            transition: all 0.2s ease-in-out;
        }

        .stButton > button:hover {
            background-color: #f1c40f;
            color: black;
            transform: translateY(-2px);
        }

        .main-title {
            font-size: 2.5rem;
            font-weight: 700;
            color: #5e60ce;
            margin-bottom: 0.2rem;
        }

        .subtitle {
            font-size: 1.1rem;
            color: #555;
            margin-bottom: 2rem;
        }
    </style>
    """, unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.markdown("## 🔧 Moduły")
        if st.button("👕 Przymierzanie"):
            st.session_state.page = "tryon"
            st.rerun()
        if st.button("😊 Emocje"):
            st.session_state.page = "emotion"
            st.rerun()
        if st.button("🎨 Kolory"):
            st.session_state.page = "color"
            st.rerun()

    # Główna sekcja – tytuł i opis
    st.markdown('<div class="main-title">🧠 Informatyka Afektywna</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Interaktywna aplikacja łącząca emocje, styl i kolorystykę.</div>', unsafe_allow_html=True)
    st.markdown("Wybierz jeden z modułów z menu bocznego po lewej stronie.")
