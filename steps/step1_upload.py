import streamlit as st
def display_user_image():
    if 'user_image' in st.session_state:
        st.image(st.session_state['user_image'], caption="Twoje zdjęcie", use_container_width=True)

def run():
    
    st.header("Krok 1: Wczytaj swoje zdjęcie")
    uploaded_file = st.file_uploader("Wybierz obraz", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        st.session_state.user_image = uploaded_file
        st.image(uploaded_file, caption="Twoje zdjęcie", use_container_width=True)
        if st.button("Dalej"):
            st.session_state.step = 2
