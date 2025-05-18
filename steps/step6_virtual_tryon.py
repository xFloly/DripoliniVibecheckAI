import streamlit as st
from gradio_client import Client, handle_file

def run():
    st.header("Krok 6: Wirtualne przymierzanie")
    if st.session_state.user_image and st.session_state.selected_cloth:
        client = Client("zhengchong/CatVTON")
        print(st.session_state.selected_cloth)
        print(st.session_state.user_image)
        person_image = {
            "background": handle_file(st.session_state.user_image.name),
            "layers": [],
            "composite": None
        }
        cloth_image = handle_file(st.session_state.selected_cloth['image'])
        result = client.predict(
            person_image=person_image,
            cloth_image=cloth_image,
            num_inference_steps=50,
            guidance_scale=2.5,
            seed=42,
            api_name="/submit_function_p2p"
        )
        st.session_state.result_image = result
        st.image(result, caption="Wynik wirtualnego przymierzania", use_container_width=True)
    else:
        st.warning("Proszę przejść przez poprzednie kroki.")
