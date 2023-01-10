from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from config.config import height, width, x, y
from misc.fullScreen import FullScreen
from misc.splitScreen import SplitScreen
from misc.trucks import Trucks
from misc.button import Button


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('SplitScreen')
        self.setFixedSize(width, height)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.move(x, y)
        self.create_widgets()

    def create_widgets(self):
        self.fullScreen = FullScreen()
        self.splitScreen = SplitScreen()
        self.trucks = Trucks()
        self.button = Button()

    def update_display(self, option):
        button = Button()
        if option == 1:
            self.fullScreen.show()
        elif option == 2:
            self.splitScreen.show()
        elif option == 3:
            self.trucks.show()





