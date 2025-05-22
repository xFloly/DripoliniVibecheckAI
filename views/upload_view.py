import streamlit as st
import tempfile
from PIL import Image

from utils.detection import detect_face_body
from components.navigation import navigation_controls

def render():
    st.subheader("Step 1: Upload your photo")
    st.markdown("---")

    uploaded_file = st.file_uploader("Upload an image with a person", type=['png', 'jpg', 'jpeg'])

    # Initialize detection state if not present
    if 'person_detected' not in st.session_state:
        st.session_state.person_detected = False

    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmp_file:
            tmp_file.write(uploaded_file.read())
            st.session_state.image_path = tmp_file.name
            st.session_state.person_detected = False  # Reset state on new upload

        st.image(st.session_state.image_path, caption="Uploaded Photo", width=250)
        
        detections = detect_face_body(st.session_state.image_path)

        if len(detections.boxes) > 0:
            st.success("✅ Human detected in the image!")
            st.session_state.person_detected = True
        else:
            st.error("❌ No person detected. Please try a different image.")
            st.session_state.person_detected = False

    navigation_controls(
        current_step='upload',
        back_step=None,
        next_step='describe_outfit' if st.session_state.person_detected else None
    )
