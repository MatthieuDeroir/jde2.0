from PyQt6.QtWidgets import *
from PySide6.QtCore import Qt
from config.config import *
from PySide6 import *

class DynamicWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('dynamics')
        self.setFixedSize(width, height)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.move(x, y)

    def onAddWidget(self):

    def onRemoveWidget(self):