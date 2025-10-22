import cv2
from core.embedding_utils import extraer_embedding, es_duplicado, serializar_embedding
from db.db_manager import insertar_persona, insertar_embedding, obtener_todos_los_embeddings

def registrar_persona(nombre, apellido, email):
    """
    Captura rostro desde webcam, extrae embedding, verifica duplicado y registra en la base de datos.
    """
    cap = cv2.VideoCapture(0)
    print("Presiona 'c' para capturar rostro, 'q' para salir.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error al acceder a la cámara.")
            break

        cv2.imshow("Registro - Cámara", frame)
        key = cv2.waitKey(1)

        if key == ord('c'):
            embedding = extraer_embedding(frame)
            if embedding is None:
                print("No se detectó rostro. Intenta de nuevo.")
                continue

            existentes = obtener_todos_los_embeddings()
            if es_duplicado(embedding, existentes):
                print("Este rostro ya está registrado.")
                continue

            try:
                persona_id = insertar_persona(nombre, apellido, email)
                vector_str = serializar_embedding(embedding)
                insertar_embedding(persona_id, vector_str)
                print("Registro exitoso.")
            except Exception as e:
                print(f"Error al registrar: {e}")
            break

        elif key == ord('q'):
            print("Registro cancelado.")
            break

    cap.release()
    cv2.destroyAllWindows()
