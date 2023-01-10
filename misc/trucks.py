from PySide6.QtWidgets import QApplication, QTableWidget, QTextEdit, QLineEdit, QWidget, QMainWindow
from PySide6.QtCore import Qt
import sys
from config.config import height, width, x, y


class Trucks(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Trucks')
        self.setFixedSize(width, height)
        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.move(x, y)
