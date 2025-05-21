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
    


def build_prompt(outfit_desc, emotion, colors, context):
    color_str = ', '.join(colors)
    # return f"The person is {emotion}. Their color palette includes {color_str}. They are going to {context}."


    prompt = (
        f"The person is {emotion}. "
        f"Their color palette includes: {color_str}. "
        f"They are going to {context}. "
        f"Currently, they are wearing: {outfit_desc}.\n\n"
        
        "Based on the above information:\n"
        "1. Determine whether the current outfit is appropriate for the specified context.\n"
        "2. If it is not appropriate, suggest specific improvements (e.g., change in style, garment type, color).\n"
        "3. Recommend exactly three new clothing items that better match the context and emotional tone.\n"
        "4. Select appropriate items from the following dataset catalog to replace or enhance the outfit.\n"
    )
    # load the clothing inventory tags
        
    clothing_catalog = load_clothing_catalog('clothes.csv')
    st.session_state.clothing_catalog = clothing_catalog
    prompt += f"\nAvailable clothing items in the dataset include:\n"
    for item_id, item in clothing_catalog.items():
        prompt += f"- {item.get_cloth_description()} (ID: {item.get_cloth_id()})\n"

    prompt += "\nRespond clearly with a justification and item references that could be used in a virtual try-on., provide 3 numbers id, only seperated by common, and no other text.\n"
    prompt += "The response should be like '10,16,2' Nothing more!!!! Just a 3 numbers id!!!! Even if they not fit\n"
    return prompt, clothing_catalog
