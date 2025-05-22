import streamlit as st
from utils.color import extract_dominant_colors
from components.navigation import navigation_controls

if 'colors' not in st.session_state:
    st.session_state['colors'] = None
    

def render():
    st.subheader("Step 4: Color Palette")

    st.markdown("---") 

    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        st.image(
            st.session_state.image_path,
            caption="Your Photo",
            width=250
        )

    with col2:
        if st.session_state.colors is None:
            with st.spinner("Extracting colors..."):
                st.session_state.colors = extract_dominant_colors(st.session_state.image_path)

        st.markdown("#### 🎨 Dominant Colors")

        if st.session_state.colors:
            # Render color swatches
            swatch_html = "".join([
                f"""
                <div style='
                    display:inline-block;
                    width:60px;
                    height:60px;
                    background-color:{color};
                    border-radius:6px;
                    margin-right:10px;
                    border:1px solid #aaa;
                ' title='{color}'></div>
                """ for color in st.session_state.colors
            ])

            st.markdown(swatch_html, unsafe_allow_html=True)
        else:
            st.warning("Please wait for color extraction before continuing.")


    # "Next" only available if colors are set
    navigation_controls(
        current_step='colors',
        back_step='face',
        next_step='context' if st.session_state.colors else None
    )
