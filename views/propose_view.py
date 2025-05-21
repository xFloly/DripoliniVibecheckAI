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
    st.image(st.session_state.image_path)

    if st.session_state.propose is None:
        with st.spinner("Proposing new outfit..."):
            st.session_state.propose = propose_clothes(st.session_state.image_path, st.session_state.outfit_desc, st.session_state.emotion, st.session_state.colors, st.session_state.context)
                    
    st.markdown("### 👗 Proposed Clothing Items:")

    # Prepare display and radio options
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

    # Show the selection radio
    selected_label = st.radio("Select one item to try on:", options)

    selected_id = id_to_item[selected_label]["id"]
    st.session_state['selected_item_id'] = selected_id

    # Visualize selected image
    st.image(id_to_item[selected_label]["path"], caption=f"Selected: {id_to_item[selected_label]['description']}", use_container_width=True)

    st.success(f"You selected item ID: {selected_id}")

    navigation_controls(
        current_step='propose',
        back_step='done',
        next_step='try_on' if st.session_state['selected_item_id'] else None
    )
