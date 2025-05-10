import cv2
from deepface import DeepFace
import streamlit as st
import time
from PIL import Image
import numpy as np

def run_emotion_detection_streamlit():
    stframe = st.empty()  # placeholder na kamerę
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        st.error("❌ Nie udało się uruchomić kamery.")
        return

    last_time = time.time()
    dominant_emotion = "Wczytywanie..."

    while True:
        ret, frame = cap.read()
        if not ret:
            st.warning("❌ Nie można pobrać obrazu z kamery.")
            break

        # Co 1 sekundę aktualizujemy emocję
        if time.time() - last_time > 1.0:
            try:
                result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                dominant_emotion = result[0]['dominant_emotion']
                face_rect = result[0]['region']

                # Bounding box
                x, y, w, h = face_rect['x'], face_rect['y'], face_rect['w'], face_rect['h']
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(frame, f"{dominant_emotion}", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)
            except Exception as e:
                dominant_emotion = "Brak twarzy"
                # (Nie przerywaj — po prostu nie rysuj)

            last_time = time.time()

        # Konwersja BGR -> RGB -> PIL -> Streamlit
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)
        stframe.image(img, channels="RGB")

        # Przycisk zatrzymania
        if st.button("🛑 Zatrzymaj"):
            break

    cap.release()
