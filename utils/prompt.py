# prompt.py
def build_prompt(emotion, colors, context):
    color_str = ', '.join(colors)
    return f"The person is {emotion}. Their color palette includes {color_str}. They are going to {context}."


    prompt = (
        f"The person is {emotion}. "
        f"Their color palette includes: {color_str}. "
        f"They are going to {context}. "
        f"Currently, they are wearing: {outfit_desc}.\n\n"
        
        "Based on the above information:\n"
        "1. Determine whether the current outfit is appropriate for the specified context.\n"
        "2. If it is not appropriate, suggest specific improvements (e.g., change in style, garment type, color).\n"
        "3. Recommend one or more new clothing items that better match the context and emotional tone.\n"
        "4. Select appropriate items from the following dataset catalog to replace or enhance the outfit.\n"
    )

    if cloth_inventory_tags:
        cloth_str = "\n".join(f"- {tag}" for tag in cloth_inventory_tags)
        prompt += f"\nAvailable clothing items in the dataset include:\n{cloth_str}\n"

    prompt += "\nRespond clearly with a justification and item references that could be used in a virtual try-on."

    return prompt
