import cv2
from deepface import DeepFace
from fer import FER
import streamlit as st
import time
from PIL import Image

def run_emotion_detection_streamlit():
    st.markdown("### Wybierz model rozpoznawania emocji")
    mode = st.radio("Metoda analizy:", ["DeepFace", "FER+"], horizontal=True)

    stframe = st.empty()

    if "stop_emotion" not in st.session_state:
        st.session_state["stop_emotion"] = False

    if st.button("🛑 Zatrzymaj", key="stop_button"):
        st.session_state["stop_emotion"] = True

    # Kamera
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    if not cap.isOpened():
        st.warning("⚠️ Kamera niedostępna. Pokazuję obraz zastępczy.")
        img = cv2.imread("img/image.png")
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        st.image(Image.fromarray(img_rgb), caption="Obraz zastępczy", use_column_width=True)
        return

    last_time = time.time()
    if mode == "FER+":
        detector = FER(mtcnn=True)

    while cap.isOpened() and not st.session_state["stop_emotion"]:
        ret, frame = cap.read()
        if not ret:
            break

        # Przetwarzanie co 1 sek
        if time.time() - last_time > 1.0:
            if mode == "DeepFace":
                frame_rgb = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2RGB)
                try:
                    result = DeepFace.analyze(frame_rgb, actions=['emotion'], detector_backend='mediapipe', enforce_detection=True)
                    emotion = result[0]['dominant_emotion']
                    region = result[0]['region']
                    x, y, w, h = region['x'], region['y'], region['w'], region['h']
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)
                except:
                    cv2.putText(frame, "Brak twarzy", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (150, 150, 150), 2)

            elif mode == "FER+":
                results = detector.detect_emotions(frame)
                if results:
                    face = results[0]
                    x, y, w, h = face["box"]
                    emotions = face["emotions"]
                    emotion = max(emotions, key=emotions.get)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 128, 255), 2)
                    cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 128, 255), 2)
                else:
                    cv2.putText(frame, "Brak twarzy", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (150, 150, 150), 2)

            last_time = time.time()

        # Wyświetl obraz
        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        stframe.image(img, channels="RGB", use_column_width=True)

    cap.release()
    st.session_state["stop_emotion"] = False
