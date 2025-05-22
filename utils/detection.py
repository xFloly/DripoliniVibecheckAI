# detection.py
from ultralytics import YOLO
import cv2

def detect_face_body(image_path, model_path='yolov8n.pt'):
    model = YOLO(model_path)
    results = model(image_path)
    detections = results[0]
    return detections

def crop_person_from_image(image_path):
    detections = detect_face_body(image_path)
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    for box in detections.boxes:
        if int(box.cls[0]) == 0:  # person
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            return image_rgb[y1:y2, x1:x2]

    return image_rgb