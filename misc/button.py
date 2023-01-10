from PySide6.QtWidgets import QApplication, QTableWidget, QTextEdit, QLineEdit, QWidget, QMainWindow, QPushButton,
from PySide6.QtCore import Qt
import sys
from config.config import height, width, x, y


class Button(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('test')
        self.setFixedSize(width, height)
        self.push()
        self.option = 0
        button = QPushButton()

    def push(self):
        btnfull = QPushButton('Fullscreen', self)
        btnfull.move(0, 0)
        btnsplit = QPushButton('Splitscreen', self)
        btnsplit.move(0, 20)
        btntruck = QPushButton('Trucks', self)
        btntruck.move(0, 40)


