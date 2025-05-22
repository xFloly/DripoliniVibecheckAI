import cv2
import numpy as np
from sklearn.cluster import KMeans
from utils.detection import crop_person_from_image

def extract_dominant_colors(image_path, k=3):
    person_crop = crop_person_from_image(image_path)
    reshaped = person_crop.reshape((-1, 3))

    kmeans = KMeans(n_clusters=k)
    kmeans.fit(reshaped)

    colors = kmeans.cluster_centers_.astype(int)
    hex_colors = ['#%02x%02x%02x' % tuple(color) for color in colors]
    return hex_colors