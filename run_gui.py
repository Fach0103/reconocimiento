import sys
from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow
from db.db_manager import inicializar_db

if __name__ == "__main__":
    inicializar_db()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
