from config import *


class DataLabel(QLabel):
    def __init__(self, widget, index, category):
        super().__init__(widget)

        self.timer = QTimer()
        self.timer.start(100)
        self.timer.timeout.connect(self.fetchData)

        self.index = index
        self.category = category

        self.data = ""
        self.previous_state = "LOADING"
        self.time = 0
        self.flag = 0

    def fetchData(self):
        try:
            datas = req("get", ip).json()
            if self.category == 'ref':
                self.data = str(datas[self.index]['plate'])
            elif self.category == 'dock':
                self.data = str(datas[self.index]['dockIndex'])
            elif self.category == 'state':
                if datas[self.index]['state'] is False and datas[self.index]['flag'] is False:
                    self.data = 'WAIT'
                elif datas[self.index]['state'] is False and datas[self.index]['flag'] is True:
                    self.data = 'COME'
                elif datas[self.index]['state'] is True and datas[self.index]['flag'] is True:
                    self.setStyleSheet("color: #059ED8")
                    self.show()
                    self.data = 'LOADING'
                else:
                    self.data = ''

            if (self.category == 'state' or self.category == 'dock') and datas[self.index]['plate'] == '':
                self.data = ''

            self.setText(self.data)
            if self.category == 'state' and self.data == 'COME':
                self.timer.timeout.connect(self.blink)
                # self.setStyleSheet("color: #66FF22")
            elif self.category == 'state' and self.data == 'LOADING':
                self.setStyleSheet("color: #059ED8")
                self.show()
            elif self.category == 'state' and self.data == 'WAIT':
                self.setStyleSheet("color: orange")

        except:
            print("Can't fetch the required data to display. Check your connection. (DataLabel.py)")

    def blink(self):
        if self.flag == 1 and self.data == 'COME':
            self.setStyleSheet("color: #66FF22")
            self.flag = 0
        elif self.flag == 0 and self.data == 'COME':
            self.setStyleSheet("color: #006400")
            self.flag = 1
