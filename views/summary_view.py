import streamlit as st
from components.navigation import navigation_controls

def render():
    st.subheader("✅ Summary")
    
    st.markdown("---")

    left_col, right_col = st.columns([1, 2], gap="large")

    with left_col:
        st.image(
            st.session_state.image_path,
            caption="Your Photo",
            width=250
        )

    with right_col:
        face_data = st.session_state.face
        colors = st.session_state.colors or []

        swatches = "".join([
            f"<div style='display:inline-block;width:30px;height:30px;background-color:{color};"
            f"border-radius:4px;margin-right:6px;border:1px solid #ccc;' title='{color}'></div>"
            for color in colors
        ])

        # Style block for info
        st.markdown("#### Summary Details")
        st.markdown(
            f"""
            <div style='
                padding: 15px;
                border-radius: 8px;
                font-size: 16px;
                line-height: 1.6;
            '>
                <strong>Outfit:</strong> {st.session_state.describe_outfit}<br><br>
                <strong>Emotion:</strong> {face_data['emotion']}<br>
                <strong>Age:</strong> {face_data['age']}<br>
                <strong>Gender:</strong> {face_data['gender']}<br><br>
                <strong>Color Palette:</strong><br>{swatches}<br><br>
                <strong>Context:</strong> {st.session_state.context}
            </div>
            """,
            unsafe_allow_html=True
        )

    navigation_controls(
        current_step='summary',
        back_step='context',
        next_step='propose'
    )
