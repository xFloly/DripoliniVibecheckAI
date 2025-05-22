import streamlit as st

from components.navigation import navigation_controls
from utils.try_on import run_try_on

if 'fitted_person' not in st.session_state:
    st.session_state.fitted_person = None


def render():
    st.subheader("Step 6: Try on the outfit")

    st.session_state.fitted_person = None
    if st.session_state.fitted_person is None:
        with st.spinner("Generating your outfit..."):
            dress_path= st.session_state.clothing_catalog.get(st.session_state['selected_item_id'],0).get_cloth_path()
            st.session_state.fitted_person = run_try_on(st.session_state.image_path, dress_path)
            print(st.session_state.fitted_person)
    st.markdown("### 👗 Your outfit")
    st.image(st.session_state.fitted_person, caption="Your outfit", use_container_width=True)



    navigation_controls(
        current_step='try_on',
        back_step='summary',
    )
