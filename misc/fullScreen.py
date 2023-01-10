# from PySide6.QtWidgets import QApplication, QTableWidget, QTextEdit, QLineEdit, QWidget, QMainWindow,QLabel, QGridLayout
# from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie, QRegion, QImage
# from PySide6.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from config.config import height, width, x, y, imageFSPath


class FullScreen(QWidget):
    # def __init__(self):
    #     super().__init__()
    #     self.setWindowTitle('FullScreen')
    #     self.setFixedSize(width, height)
    #     # self.setWindowFlag(Qt.FramelessWindowHint)
    #     self.move(x, y)
    #     self.label = QLabel()
    #     self.image = QImage(imageFSPath)
    #     self.grid = QGridLayout()
    #     self.grid.addWidget(self.label, 1, 1)
    #     self.setLayout(self.grid)

    def __init__(self):
        super().__init__()
        app = QApplication([])
        self.im = QPixmap("../medias/image.jpg")
        self.label = QLabel()
        self.label.setPixmap(self.im)

        self.grid = QGridLayout()
        self.grid.addWidget(self.label, 1, 1)
        self.setLayout(self.grid)

        self.setGeometry(50, 50, 320, 200)
        self.setWindowTitle("PyQT show image")
        self.show()
        sys.exit(app.exec())



