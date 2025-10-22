from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
)
from core.register import registrar_persona
from core.recognize import reconocer_desde_camara
from db.db_manager import inicializar_db

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reconocimiento Facial")
        self.setGeometry(100, 100, 300, 200)
        self.init_ui()

    def init_ui(self):
        self.label_nombre = QLabel("Nombre:")
        self.input_nombre = QLineEdit()

        self.label_apellido = QLabel("Apellido:")
        self.input_apellido = QLineEdit()

        self.label_email = QLabel("Email:")
        self.input_email = QLineEdit()

        self.btn_registrar = QPushButton("Registrar")
        self.btn_verificar = QPushButton("Verificar desde cámara")

        self.btn_registrar.clicked.connect(self.registrar)
        self.btn_verificar.clicked.connect(self.verificar)

        layout = QVBoxLayout()
        layout.addWidget(self.label_nombre)
        layout.addWidget(self.input_nombre)
        layout.addWidget(self.label_apellido)
        layout.addWidget(self.input_apellido)
        layout.addWidget(self.label_email)
        layout.addWidget(self.input_email)
        layout.addWidget(self.btn_registrar)
        layout.addWidget(self.btn_verificar)

        self.setLayout(layout)

    def registrar(self):
        nombre = self.input_nombre.text()
        apellido = self.input_apellido.text()
        email = self.input_email.text()

        if not nombre or not apellido or not email:
            QMessageBox.warning(self, "Error", "Completa todos los campos.")
            return

        registrar_persona(nombre, apellido, email)

    def verificar(self):
        reconocer_desde_camara()
