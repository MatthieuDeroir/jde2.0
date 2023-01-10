from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QTimer, QDateTime
from data import ip, blink_time
from utils.req import req


class DataLabel(QLabel):
    def __init__(self, widget, index, category):
        super().__init__(widget)
        self.timer = QTimer()
        self.index = index
        self.category = category
        self.timer.start(100)
        self.data = ""
        self.previous_state = "LOADING"
        self.time = 0
        self.flag = 0
        self.timer.timeout.connect(self.fetchData)

    def fetchData(self):
        try:
            fetched_datas = req("get", ip).json()
            if self.category == 'ref':
                self.data = str(fetched_datas[self.index]['plate'])
            elif self.category == 'dock':
                self.data = str(fetched_datas[self.index]['dockIndex'])
            elif self.category == 'state':
                if fetched_datas[self.index]['state'] is False and fetched_datas[self.index]['flag'] is False:
                    self.data = 'WAIT'
                elif fetched_datas[self.index]['state'] is False and fetched_datas[self.index]['flag'] is True:
                    self.data = 'COME'
                elif fetched_datas[self.index]['state'] is True and fetched_datas[self.index]['flag'] is True:
                    self.setStyleSheet("color: #059ED8")
                    self.show()
                    self.data = 'LOADING'
                else:
                    self.data = ''


            if (self.category is 'state' or self.category is 'dock') and fetched_datas[self.index]['plate'] == '':
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
            print("cant fetch datas")

# self.data[self.index][self.category] = fetched_datas[self.index]




    def blink(self):
        # if self.isHidden():
        #     self.show()
        if self.flag == 1 and self.data is 'COME':
            self.setStyleSheet("color: #66FF22")
            self.flag = 0
        elif self.flag == 0 and self.data is 'COME':
            # self.hide()
            self.setStyleSheet("color: #006400")
            self.flag = 1
