from db.db_manager import inicializar_db
from core.register import registrar_persona
from core.recognize import reconocer_desde_camara

def menu():
    print("\n--- Sistema de Reconocimiento Facial ---")
    print("1. Registrar nueva persona")
    print("2. Verificar desde cámara")
    print("3. Salir")
    return input("Selecciona una opción (1/2/3): ")

if __name__ == "__main__":
    inicializar_db()

    while True:
        opcion = menu()

        if opcion == '1':
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            email = input("Email: ")
            registrar_persona(nombre, apellido, email)

        elif opcion == '2':
            reconocer_desde_camara()

        elif opcion == '3':
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")
