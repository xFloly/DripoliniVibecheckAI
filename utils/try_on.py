import streamlit as st
from gradio_client import Client, handle_file

def run_try_on(person_image, cloth_image):
    client = Client("zhengchong/CatVTON")
    person_image = {
        "background": handle_file(person_image),
        "layers": [],
        "composite": None
    }
    cloth_image = handle_file(cloth_image)
    result = client.predict(
        person_image=person_image,
        cloth_image=cloth_image,
        num_inference_steps=5,
        guidance_scale=2.5,
        seed=42,
        api_name="/submit_function_p2p"
    )
    return result
    
