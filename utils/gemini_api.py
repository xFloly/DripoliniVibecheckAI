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
    
    base_prompt = "Describe in detail what the person is wearing: clothing type, color, and style."
    full_prompt = base_prompt if not extra_prompt else f"{base_prompt} {extra_prompt}"

    response = model.generate_content([full_prompt, image])
    return response.text

def describe_emotion(image_path, extra_prompt=None):
    image = Image.open(image_path)

    base_prompt = (
        "Analyze the person's facial expression and describe their likely emotional state "
        "(e.g., happy, sad, angry, surprised)."
    )
    full_prompt = base_prompt if not extra_prompt else f"{base_prompt} {extra_prompt}"

    response = model.generate_content([full_prompt, image])
    return response.text

def propose_clothes(image_path, outfit_desc,emotion, colors, context):

    image = Image.open(image_path)

    full_prompt, catalog = utils.prompt.build_prompt(
        outfit_desc=outfit_desc,
        emotion=emotion,
        colors=colors,
        context=context
    )
    response = model.generate_content([full_prompt, image])
    print("Response from Gemini:", response.text)
    # Decode the clothing output
    propose_clothes = utils.prompt.decode_clothing_output(response.text, catalog)
    
    return propose_clothes