import os
import google.generativeai as genai
from PIL import Image
import utils.prompt
import streamlit as st


# Initialize Gemini with API key
genai.configure(api_key='AIzaSyDNam5AtruOM5K3VviHIUj9FpOtaZcp8Cs')

# Load the Gemini Pro Vision model
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")


def describe_outfit(image_path, extra_prompt=None):
    """Send image to Gemini and return a clothing description."""
    image = Image.open(image_path)
    
    base_prompt = "Describe in detail what the person is wearing: clothing type, color, and style. But keep it short in max 7 plain-text sentences "
    full_prompt = base_prompt if not extra_prompt else f"{base_prompt} {extra_prompt}"

    response = model.generate_content([full_prompt, image])
    return response.text


def propose_clothes(image_path, outfit_desc,face_data, colors, context):

    image = Image.open(image_path)

    full_prompt, catalog = utils.prompt.build_prompt(
        outfit_desc=outfit_desc,
        face_data=face_data,
        colors=colors,
        context=context
    )
    response = model.generate_content([full_prompt, image])
    print("Response from Gemini:", response.text)
    # Decode the clothing output
    propose_clothes = utils.prompt.decode_clothing_output(response.text, catalog)
    
    return propose_clothes