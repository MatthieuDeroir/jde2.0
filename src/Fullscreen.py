from data import *
from src.DisplayLabel import DisplayLabel


class Ui_Fullscreen(object):
    def __init__(self, index):
        self.index = index
        self.path = "../"
        self.format = ""
        self.current_path = '../'
        timer = QTimer()
        timer.start(1000)  # Update the UI every 1 second
        timer.timeout.connect(self.setupUi)
        self.fetched_datas = ""
        self.fetched_datas = req("get", ip_fs).json()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(192, 433)
        try:
            self.fetched_datas = req("get", ip_fs).json()
            self.path = self.fetched_datas[self.index]['path']

            if self.fetched_datas[self.index]['format'] == 'mp4':
                videoWidget = QVideoWidget()
                wid = QtWidgets.QWidget(MainWindow)
                MainWindow.setCentralWidget(wid)
                self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
                layout = QVBoxLayout()
                layout.addWidget(videoWidget)
                wid.setLayout(layout)
                self.mediaPlayer.setObjectName("display_label")
                self.mediaPlayer.setVideoOutput(videoWidget)
                self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(path_to_video + self.path)))
                self.mediaPlayer.play()
            else:
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(0, 0, screen_width, screen_height))
                self.label.setObjectName("label")
                MainWindow.setCentralWidget(self.centralwidget)

                self.display_label = DisplayLabel(self.centralwidget, self.index)
                self.display_label.setObjectName("display_label")

                self.display_label.setGeometry(QtCore.QRect(0, 0, screen_width, screen_height))
                self.display_label.setScaledContents(True)
        except:
            print("cant fetch datas")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
