import cv2
from core.embedding_utils import extraer_embedding, calcular_similitud
from db.db_manager import obtener_todos_los_embeddings

def reconocer_desde_camara(umbral=0.6):
    cap = cv2.VideoCapture(0)
    print("Presiona 'q' para salir.")

    embeddings_registrados = obtener_todos_los_embeddings()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error al acceder a la cámara.")
            break

        embedding_actual = extraer_embedding(frame)
        nombre_detectado = "Desconocido"

        if embedding_actual is not None:
            for persona_id, nombre, apellido, email, vector_str in embeddings_registrados:
                vector = [float(x) for x in vector_str.split(',')]
                distancia = calcular_similitud(embedding_actual, vector)
                if distancia < umbral:
                    nombre_detectado = f"{nombre} {apellido}"
                    break

        cv2.putText(frame, nombre_detectado, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Reconocimiento Facial", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
