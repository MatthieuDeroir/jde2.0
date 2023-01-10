from data import *
from src.DisplayLabel import DisplayLabel


class Ui_Shutdown(object):
    def __init__(self, index):
        self.index = index

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(192, 433)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, screen_width, screen_height))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.display_label = DisplayLabel(self.centralwidget, self.index)
        self.display_label.setObjectName("display_label")
        self.display_label.setStyleSheet("background-image:url(./medias/fullscreenBlack.png)")
        self.display_label.setGeometry(QtCore.QRect(0, 0, screen_width, screen_height))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
