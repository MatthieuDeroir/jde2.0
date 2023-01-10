from config import *


class DisplayLabel(QLabel):
    def __init__(self, widget, pos):
        super().__init__(widget)
        # timers
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.fetchData)
        self.timer.timeout.connect(self.updateData)

        # position is to determine which media in the database need to be displayed
        # also a -1 position means that the display is black
        self.pos = pos

        self.setScaledContents(True)

        self.path = "../../"

    def fetchData(self):
        if self.pos == -1:
            self.path = "../../assets/blackScreen.png"
        else:
            try:
                fetched_datas = req("get", ip_fs).json()
                self.path = fetched_datas[self.pos]['path']
                print("path = " + self.path)
            except:
                print("Can't fetch the required data to display. Check your connection. (DisplayLabel.py)")

    def updateData(self):
        if self.pos == -1:
            self.setStyleSheet("background-image:url(" + self.path + ")")
        else:
            self.setStyleSheet(
                "background-image:url(" + path_to_media + self.path + "); "
                                                                      "background-repeat: no-repeat;"
                                                                      "background-size: contain;width:192px;")

