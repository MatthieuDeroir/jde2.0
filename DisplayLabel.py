from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QTimer, QDateTime
from data import *
from utils.req import req


class DisplayLabel(QLabel):
    def __init__(self, widget, pos):
        super().__init__(widget)
        self.timer = QTimer()
        self.pos = pos

        self.timer.start(1000)
        self.timer.timeout.connect(self.fetchData)
        self.timer.timeout.connect(self.updateData)
        self.setScaledContents(True)
        self.setStyleSheet("width:192px;")

        self.path = "./"

    def fetchData(self):
        if self.pos == -1:
            self.path = "./medias/fullscreenBlack.png"
        else:
            try:
                fetched_datas = req("get", ip_fs).json()
                self.path = fetched_datas[self.pos]['path']
                print("path = " + self.path)
            except:
                print("cant fetch datas")

    def updateData(self):
        if self.pos == -1:
            self.setStyleSheet("background-image:url(" + self.path + ")")
        else:
            print(path_to_media + self.path)
            self.setStyleSheet("background-image:url(" + path_to_media + self.path + ")")
            print("image display")

    def blink(self):
        if self.isHidden():
            self.show()
        else:
            self.hide()
