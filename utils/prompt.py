import csv
from utils.cloth import Cloth
import streamlit as st
# prompt.py

def load_clothing_catalog(csv_path):
    catalog = dict()
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # store entire row keyed by id
            catalog[row['id']] = Cloth(
                id=row['id'],
                path=row['path'],
                description=row['description']
            )
    return catalog

def decode_clothing_output(output, clothing_catalog):
    selected_ids = [id_.strip() for id_ in output.split(',') if id_.strip().isdigit()]

    # Retrieve corresponding items from the catalog
    selected_items = []
    for item_id in selected_ids:
        item = clothing_catalog.get(item_id)
        if item:
            selected_items.append(item)
        else:
            print(f"Warning: ID {item_id} not found in clothing catalog.")

    return selected_items
    


def build_prompt(outfit_desc, face_data, colors, context):
    color_str = ', '.join(colors)
    # return f"The person is {emotion}. Their color palette includes {color_str}. They are going to {context}."

    emotion = face_data['emotion']
    age = face_data['age']
    gender = face_data['gender']

    prompt = (
        f"The person appears to be {emotion}, around {age} years old, and presents as {gender}. "
        f"Their color palette includes: {color_str}. "
        f"They are going to {context}. "
        f"Currently, they are wearing: {outfit_desc}.\n\n"
        
        "Based on the above information:\n"
        "1. Determine whether the current outfit is appropriate for the specified context.\n"
        "2. If not, suggest improvements in clothing type, color, or style.\n"
        "3. Recommend exactly **three** new clothing items from the dataset below that match the emotional tone and context.\n"
    )

    # Load catalog and add to session
    clothing_catalog = load_clothing_catalog('clothes.csv')
    st.session_state.clothing_catalog = clothing_catalog

    # Append dataset descriptions
    prompt += "\nAvailable clothing items in the dataset include:\n"
    for item_id, item in clothing_catalog.items():
        prompt += f"- {item.get_cloth_description()} (ID: {item.get_cloth_id()})\n"

    # Final strict instruction
    prompt += (
        "\nRespond with exactly **three clothing IDs**, separated by commas, and NOTHING else.\n"
        "Example response: `3,7,12`\n"
        "**No explanations. No extra text. Just the numbers.**"
    )

    return prompt, clothing_catalog