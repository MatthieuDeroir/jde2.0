from config import *
from src.Labels.DisplayLabel import DisplayLabel


class Ui_Splitscreen(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(192, 433)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, screen_width, screen_height))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.line = 0

        self.display_label_1 = DisplayLabel(self.centralwidget, 1)
        self.display_label_1.setObjectName("display_label_1")
        self.display_label_1.setGeometry(
            QtCore.QRect(0, 0 + (screen_height / 3 * self.line), screen_width, screen_height / 3))
        self.display_label_1.setScaledContents(True)

        self.line = 1

        self.display_label_2 = DisplayLabel(self.centralwidget, 2)
        self.display_label_2.setObjectName("display_label_2")
        self.display_label_2.setGeometry(
            QtCore.QRect(0, 0 + (screen_height / 3 * self.line), screen_width, screen_height / 3))
        self.display_label_2.setScaledContents(True)

        self.line = 2

        self.display_label_3 = DisplayLabel(self.centralwidget, 3)
        self.display_label_3.setObjectName("display_label_3")
        self.display_label_3.setGeometry(
            QtCore.QRect(0, 0 + (screen_height / 3 * self.line), screen_width, screen_height / 3))
        self.display_label_3.setScaledContents(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
