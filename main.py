
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt


class Motoca(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Motoca") # Titulo da janela
        self.resize(900, 600) # Tamanho da janela


if __name__ == "__main__":
    app = QApplication(sys.argv)

    janela = Motoca()
    janela.show()

    sys.exit(app.exec())
