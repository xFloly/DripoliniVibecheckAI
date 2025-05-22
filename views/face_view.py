import streamlit as st
from components.navigation import navigation_controls
from utils.face import analyze_face  # formerly emotion.py

# Ensure session state key exists
if 'face' not in st.session_state:
    st.session_state['face'] = None

def render():
    st.subheader("Step 3: Face Analysis")

    st.markdown("---") 


    left_col, right_col = st.columns([1, 2], gap="large")

    with left_col:
        st.image(
            st.session_state.image_path,
            caption="Your Photo",
            width=250
        )

    with right_col:
        if st.session_state.face is None:
            with st.spinner("Analyzing face..."):
                st.session_state.face = analyze_face(st.session_state.image_path)

        face_data = st.session_state.face

        st.markdown("#### 😊 Face Details")
        st.markdown(
            f"""
            <div style='
                padding: 15px;
                border-radius: 8px;
                font-size: 16px;
                line-height: 1.6;
            '>
                <strong>Emotion:</strong> {face_data['emotion']}<br>
                <strong>Age:</strong> {face_data['age']}<br>
                <strong>Gender:</strong> {face_data['gender']}
            </div>
            """,
            unsafe_allow_html=True
        )

    navigation_controls(
        current_step='face',
        back_step='describe_outfit',
        next_step='colors' if face_data else None
    )
