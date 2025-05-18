import os
import google.generativeai as genai
from PIL import Image

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