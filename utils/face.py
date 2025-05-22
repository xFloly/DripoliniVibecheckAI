from deepface import DeepFace

def analyze_face(image_path):
    analysis = DeepFace.analyze(img_path=image_path, actions=['emotion', 'age', 'gender'], model_name='Facenet')
    result = analysis[0]

    return {
        'emotion': result['dominant_emotion'],
        'age': result['age'],
        'gender': result['dominant_gender']
    }
