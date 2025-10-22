import dlib
import numpy as np
import cv2
import os

# Rutas a los modelos de Dlib
BASE_PATH = os.path.dirname(os.path.dirname(__file__))
PREDICTOR_PATH = os.path.join(BASE_PATH, 'assets', 'shape_predictor_68_face_landmarks.dat')
FACE_RECOG_MODEL_PATH = os.path.join(BASE_PATH, 'assets', 'dlib_face_recognition_resnet_model_v1.dat')

# Inicializar modelos de Dlib
detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor(PREDICTOR_PATH)
face_rec_model = dlib.face_recognition_model_v1(FACE_RECOG_MODEL_PATH)

def extraer_embedding(frame):
    """
    Detecta el rostro en el frame y devuelve el embedding como vector numpy.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = detector(gray)

    if len(faces) == 0:
        return None  # No se detectó rostro

    shape = shape_predictor(gray, faces[0])
    embedding = face_rec_model.compute_face_descriptor(gray, shape)
    return np.array(embedding)

def calcular_similitud(embedding1, embedding2):
    """
    Calcula la distancia euclidiana entre dos embeddings.
    """
    return np.linalg.norm(embedding1 - embedding2)

def es_duplicado(nuevo_embedding, embeddings_existentes, umbral=0.6):
    """
    Compara el nuevo embedding con los existentes y determina si ya existe.
    """
    for _, _, _, _, vector_str in embeddings_existentes:
        vector = np.fromstring(vector_str, sep=',')
        distancia = calcular_similitud(nuevo_embedding, vector)
        if distancia < umbral:
            return True
    return False

def serializar_embedding(embedding):
    """
    Convierte el vector numpy a string para guardar en base de datos.
    """
    return ','.join(map(str, embedding))
