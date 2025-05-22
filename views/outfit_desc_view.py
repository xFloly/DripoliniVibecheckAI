import streamlit as st

from components.navigation import navigation_controls
from utils.gemini_api import describe_outfit

def render():
    if "describe_outfit" not in st.session_state:
        st.session_state.describe_outfit = None

    st.subheader("Step 2: Outfit Analysis")
    
    st.markdown("---") 

    left_col, right_col = st.columns([1, 2], gap="large")

    with left_col:
        st.image(
            st.session_state.image_path,
            caption="Your Photo",
            width=250 
        )

    with right_col:
        if st.session_state.describe_outfit is None:
            with st.spinner("👗 Analyzing your outfit..."):
                st.session_state.describe_outfit = describe_outfit(st.session_state.image_path)

        st.markdown("""
            <style>
            textarea {
                resize: none !important;
            }
            </style>
        """, unsafe_allow_html=True)


        st.markdown("#### Outfit Description")

        # Clean display without textbox
        st.markdown(
            f"""
            <div style='
                padding: 15px;
                border-radius: 8px;
                font-size: 16px;
                line-height: 1.6;
            '>
                {st.session_state.describe_outfit}
            </div>
            """,
            unsafe_allow_html=True
        )

    navigation_controls(
        current_step='describe_outfit',
        back_step='upload',
        next_step='face' if st.session_state.describe_outfit else None
    )
