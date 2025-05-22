import streamlit as st
from components.navigation import navigation_controls
from utils.gemini_api import propose_clothes

if 'propose' not in st.session_state:
    st.session_state['propose'] = None

if 'selected_item_id' not in st.session_state:
    st.session_state['selected_item_id'] = None

if 'clothing_catalog' not in st.session_state:
    st.session_state['clothing_catalog'] = None


def render():
    st.subheader("Step 5: Propose Outfit")
    st.markdown("---")

    if st.session_state.propose is None:
        with st.spinner("Proposing new outfit..."):
            st.session_state.propose = propose_clothes(
                st.session_state.image_path,
                st.session_state.describe_outfit,
                st.session_state.face,
                st.session_state.colors,
                st.session_state.context
            )


    # Prepare options
    options = []
    id_to_item = {}

    for item in st.session_state.propose:
        cloth_id = item.get_cloth_id()
        desc = item.get_cloth_description()
        img_path = item.get_cloth_path()
        label = f"ID {cloth_id}: {desc}"
        options.append(label)
        id_to_item[label] = {
            "id": cloth_id,
            "path": img_path,
            "description": desc
        }

    # Layout: left = original image, right = choices + preview
    left_col, right_col = st.columns([2, 3], gap="large")

    with left_col:
        st.image(
            st.session_state.image_path,
            width=250
        )

    with right_col:
        st.markdown("### 👗 Proposed Clothing Items")
        st.markdown("#### Select one item to try on:")
        selected_label = st.radio("options", options)
        selected_id = id_to_item[selected_label]["id"]
        st.session_state['selected_item_id'] = selected_id

        st.image(
            id_to_item[selected_label]["path"],
            caption=f"Selected: {id_to_item[selected_label]['description']}",
            width=320
        )

        st.success(f"You selected item ID: {selected_id}")

    navigation_controls(
        current_step='propose',
        back_step='done',
        next_step='try_on' if st.session_state['selected_item_id'] else None
    )
