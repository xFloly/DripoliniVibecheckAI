# detection.py
from ultralytics import YOLO
import cv2

def detect_face_body(image_path, model_path='yolov8n.pt'):
    model = YOLO(model_path)
    results = model(image_path)
    detections = results[0]
    return detections
