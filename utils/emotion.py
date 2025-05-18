# emotion.py
from deepface import DeepFace

def analyze_emotion(image_path):
    analysis = DeepFace.analyze(img_path=image_path, actions=['emotion'])
    return analysis[0]['dominant_emotion']
