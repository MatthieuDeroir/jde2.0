from data import *
from src.DataLabel import DataLabel


class Ui_Truckscreen(QMainWindow):
    def fetchData(self):
        try:
            self.pathFullScreen = req("get", ip_fs).json()
        except:
            print("can't get fs path ")

    def setupUi(self, MainWindow):
        try:
            self.media = req("get", ip_fs).json()
        except:
            print("can't get medias")
        self.timer = QTimer()
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(screen_width, screen_height)
        MainWindow.setStyleSheet("background-color: black;")
        MainWindow.setDocumentMode(False)

        QtGui.QFontDatabase.addApplicationFont("Arial.otf")

        # region MAIN
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # endregion

        # region LOGO
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setObjectName("logo_label")
        self.logo_label.setStyleSheet("background-image: url(./logo.jpeg)")
        self.logo_label.setGeometry(QtCore.QRect(0, 0, screen_width, 50))
        # endregion

        # region TITLE 1
        self.title_1_reference = QtWidgets.QLabel(self.centralwidget)
        self.title_1_reference.setGeometry(QtCore.QRect(ref_x, 50, 81, font_size))
        self.title_1_reference.setStyleSheet("color: white;")
        self.title_1_reference.setFont(QtGui.QFont(font, title_font_size))
        self.title_1_reference.setObjectName("title_1_reference")
        self.title_1_state = QtWidgets.QLabel(self.centralwidget)
        self.title_1_state.setGeometry(QtCore.QRect(state_x + 10, 50, 41, font_size))
        self.title_1_state.setStyleSheet("color: white;")
        self.title_1_state.setFont(QtGui.QFont(font, title_font_size))
        self.title_1_state.setAlignment(QtCore.Qt.AlignCenter)
        self.title_1_state.setObjectName("title_1_state")
        self.title_1_dock = QtWidgets.QLabel(self.centralwidget)
        self.title_1_dock.setText("DOCK")
        self.title_1_dock.setGeometry(
            QtCore.QRect(screen_width - self.getWidth(self.title_1_dock) * dock_title_x - 6, 50, 41, font_size))
        self.title_1_dock.setStyleSheet("color: white;")
        self.title_1_dock.setFont(QtGui.QFont(font, title_font_size))
        self.title_1_dock.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.title_1_dock.setObjectName("title_1_dock")
        # endregion

        # region REFERENCES
        self.reference_list = QtWidgets.QVBoxLayout()
        self.reference_list.setGeometry(QtCore.QRect(0, ref_list_x, screen_width, 166))
        self.reference_list.setObjectName("reference_list")

        # region LINE 1
        self.line = 0
        self.line_1 = QtWidgets.QHBoxLayout()
        self.ref_1 = DataLabel(self.centralwidget, self.line, "ref")
        self.ref_1.setFont(QtGui.QFont(font, line_font_size))
        self.ref_1.setStyleSheet("color:yellow;")
        self.ref_1.setText(data[self.line]['ref'])
        self.ref_1.setGeometry(
            QtCore.QRect(ref_x, ref_list_x + (font_size * self.line), self.getWidth(self.ref_1) + 8, font_size))

        self.state_1 = DataLabel(self.centralwidget, self.line, "state")
        self.state_1.setFont(QtGui.QFont(font, line_font_size))
        self.state_1.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.state_1.setStyleSheet("color:blue;") if data[self.line][
                                                         'state'] == 'LOADING' else self.state_1.setStyleSheet(
            "color:#66FF22;")
        self.state_1.setText(data[self.line]['state'])
        self.state_1.setGeometry(QtCore.QRect(state_x, ref_list_x + (font_size * self.line), state_max_size, font_size))

        self.dock_1 = DataLabel(self.centralwidget, self.line, "dock")
        self.dock_1.setFont(QtGui.QFont(font, line_font_size))
        self.dock_1.setStyleSheet("color:white;")
        self.dock_1.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.dock_1.setText(data[self.line]['dock'])
        self.dock_1.setGeometry(
            QtCore.QRect(screen_width - self.getWidth(self.dock_1) - margin, ref_list_x + (font_size * self.line),
                         self.getWidth(self.dock_1) + margin, font_size))

        # endregion

        # region LINE 2
        self.line = 1
        self.line_2 = QtWidgets.QHBoxLayout()
        self.ref_2 = DataLabel(self.centralwidget, self.line, "ref")
        self.ref_2.setFont(QtGui.QFont(font, line_font_size))
        self.ref_2.setStyleSheet("color:yellow;")
        self.ref_2.setText(data[self.line]['ref'])
        self.ref_2.setGeometry(
            QtCore.QRect(ref_x, ref_list_x + (font_size * self.line), self.getWidth(self.ref_2) + 8, font_size))

        self.state_2 = DataLabel(self.centralwidget, self.line, "state")
        self.state_2.setFont(QtGui.QFont(font, line_font_size))
        self.state_2.setStyleSheet("color:blue;") if data[self.line][
                                                         'state'] == 'LOADING' else self.state_2.setStyleSheet(
            "color:#66FF22;")
        self.state_2.setText(data[self.line]['state'])
        self.state_2.setGeometry(QtCore.QRect(state_x, ref_list_x + (font_size * self.line), state_max_size, font_size))
        self.state_2.setAlignment(QtCore.Qt.AlignCenter)

        # self.timer.timeout.connect(self.blink)

        self.dock_2 = DataLabel(self.centralwidget, self.line, "dock")
        self.dock_2.setFont(QtGui.QFont(font, line_font_size))

        self.dock_2.setStyleSheet("color:white;")
        self.dock_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.dock_2.setText(data[self.line]['dock'])
        self.dock_2.setGeometry(
            QtCore.QRect(screen_width - self.getWidth(self.dock_2) - margin, ref_list_x + (font_size * self.line),
                         self.getWidth(self.dock_2) + margin, font_size))

        # endregion

        # region LINE 3
        self.line = 2
        self.line_3 = QtWidgets.QHBoxLayout()
        self.ref_3 = DataLabel(self.centralwidget, self.line, "ref")
        self.ref_3.setFont(QtGui.QFont(font, line_font_size))

        self.ref_3.setStyleSheet("color:yellow;")
        self.ref_3.setFont(QtGui.QFont(font, line_font_size))

        self.ref_3.setText(data[self.line]['ref'])
        self.ref_3.setGeometry(
            QtCore.QRect(ref_x, ref_list_x + (font_size * self.line), self.getWidth(self.ref_3) + 8, font_size))

        self.state_3 = DataLabel(self.centralwidget, self.line, "state")
        self.state_3.setFont(QtGui.QFont(font, line_font_size))

        self.state_3.setAlignment(QtCore.Qt.AlignCenter)
        self.state_3.setStyleSheet("color:blue;") if data[self.line][
                                                         'state'] == 'LOADING' else self.state_3.setStyleSheet(
            "color:#66FF22;")
        self.state_3.setText(data[self.line]['state'])
        self.state_3.setGeometry(QtCore.QRect(state_x, ref_list_x + (font_size * self.line), state_max_size, font_size))
        # self.timer.timeout.connect(self.blink)

        self.dock_3 = DataLabel(self.centralwidget, self.line, "dock")
        self.dock_3.setFont(QtGui.QFont(font, line_font_size))

        self.dock_3.setStyleSheet("color:white;")
        self.dock_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.dock_3.setText(data[self.line]['dock'])
        self.dock_3.setGeometry(
            QtCore.QRect(screen_width - self.getWidth(self.dock_3) - margin, ref_list_x + (font_size * self.line),
                         self.getWidth(self.dock_3) + margin, font_size))

        # endregion

        # region LINE 4
        self.line = 3
        self.line_4 = QtWidgets.QHBoxLayout()
        self.ref_4 = DataLabel(self.centralwidget, self.line, "ref")
        self.ref_4.setFont(QtGui.QFont(font, line_font_size))

        self.ref_4.setFont(QtGui.QFont(font, line_font_size))

        self.ref_4.setStyleSheet("color:yellow;")
        self.ref_4.setText(data[self.line]['ref'])
        self.ref_4.setGeometry(
            QtCore.QRect(ref_x, ref_list_x + (font_size * self.line), self.getWidth(self.ref_4) + 8, font_size))

        self.state_4 = DataLabel(self.centralwidget, self.line, "state")
        self.state_4.setFont(QtGui.QFont(font, line_font_size))

        self.state_4.setAlignment(QtCore.Qt.AlignCenter)
        self.state_4.setStyleSheet("color:blue;") if data[self.line][
                                                         'state'] == 'LOADING' else self.state_4.setStyleSheet(
            "color:#66FF22;")
        self.state_4.setText(data[self.line]['state'])
        self.state_4.setGeometry(QtCore.QRect(state_x, ref_list_x + (font_size * self.line), state_max_size, font_size))
        # self.timer.timeout.connect(self.blink)

        self.dock_4 = DataLabel(self.centralwidget, self.line, "dock")
        self.dock_4.setFont(QtGui.QFont(font, line_font_size))

        self.dock_4.setStyleSheet("color:white;")
        self.dock_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.dock_4.setText(data[self.line]['dock'])
        self.dock_4.setGeometry(
            QtCore.QRect(screen_width - self.getWidth(self.dock_4) - margin, ref_list_x + (font_size * self.line),
                         self.getWidth(self.dock_4) + margin, font_size))

        # endregion

        # region LINE 5
        self.line = 4
        self.line_5 = QtWidgets.QHBoxLayout()
        self.ref_5 = DataLabel(self.centralwidget, self.line, "ref")
        self.ref_5.setFont(QtGui.QFont(font, line_font_size))

        self.ref_5.setFont(QtGui.QFont(font, line_font_size))
        self.ref_5.setStyleSheet("color:yellow;")
        self.ref_5.setText(data[self.line]['ref'])
        self.ref_5.setGeometry(
            QtCore.QRect(ref_x, ref_list_x + (font_size * self.line), self.getWidth(self.ref_5) + 8, font_size))

        self.state_5 = DataLabel(self.centralwidget, self.line, "state")
        self.state_5.setFont(QtGui.QFont(font, line_font_size))

        self.state_5.setAlignment(QtCore.Qt.AlignCenter)
        self.state_5.setStyleSheet("color:blue;") if data[self.line][
                                                         'state'] == 'LOADING' else self.state_5.setStyleSheet(
            "color:#66FF22;")
        self.state_5.setText(data[self.line]['state'])
        self.state_5.setGeometry(QtCore.QRect(state_x, ref_list_x + (font_size * self.line), state_max_size, font_size))
        # self.timer.timeout.connect(self.blink)

        self.dock_5 = DataLabel(self.centralwidget, self.line, "dock")
        self.dock_5.setFont(QtGui.QFont(font, line_font_size))

        self.dock_5.setStyleSheet("color:white;")
        self.dock_5.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.dock_5.setText(data[self.line]['dock'])
        self.dock_5.setGeometry(
            QtCore.QRect(screen_width - self.getWidth(self.dock_5) - margin, ref_list_x + (font_size * self.line),
                         self.getWidth(self.dock_5) + margin, font_size))

        # endregion

        # region LINE 6
        self.line = 5
        self.line_6 = QtWidgets.QHBoxLayout()
        self.ref_6 = DataLabel(self.centralwidget, self.line, "ref")
        self.ref_6.setFont(QtGui.QFont(font, line_font_size))

        self.ref_6.setFont(QtGui.QFont(font, line_font_size))
        self.ref_6.setStyleSheet("color:yellow;")
        self.ref_6.setText(data[self.line]['ref'])
        self.ref_6.setGeometry(
            QtCore.QRect(ref_x, ref_list_x + (font_size * self.line), self.getWidth(self.ref_6) + 8, font_size))

        self.state_6 = DataLabel(self.centralwidget, self.line, "state")
        self.state_6.setFont(QtGui.QFont(font, line_font_size))

        self.state_6.setAlignment(QtCore.Qt.AlignCenter)
        self.state_6.setStyleSheet("color:blue;") if data[self.line][
                                                         'state'] == 'LOADING' else self.state_6.setStyleSheet(
            "color:#66FF22;")
        self.state_6.setText(data[self.line]['state'])
        self.state_6.setGeometry(QtCore.QRect(state_x, ref_list_x + (font_size * self.line), state_max_size, font_size))
        # self.timer.timeout.connect(self.blink)

        self.dock_6 = DataLabel(self.centralwidget, self.line, "dock")
        self.dock_6.setFont(QtGui.QFont(font, line_font_size))

        self.dock_6.setStyleSheet("color:white;")
        self.dock_6.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.dock_6.setText(data[self.line]['dock'])
        self.dock_6.setGeometry(
            QtCore.QRect(screen_width - self.getWidth(self.dock_6) - margin, ref_list_x + (font_size * self.line),
                         self.getWidth(self.dock_6) + margin, font_size))

        # endregion
        # endregion

        # region SEPARATOR
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 236, screen_width, 10))
        self.line.setStyleSheet("background-color: white;color: white;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        # endregion

        # region TITLE 2
        self.title_2_reference = QtWidgets.QLabel(self.centralwidget)
        self.title_2_reference.setGeometry(QtCore.QRect(ref_x, 246, 81, font_size))
        self.title_2_reference.setStyleSheet("color: white;")
        self.title_2_reference.setObjectName("title_2_reference")
        self.title_2_reference.setFont(QtGui.QFont(font, title_font_size))

        self.title_2_state = QtWidgets.QLabel(self.centralwidget)
        self.title_2_state.setGeometry(QtCore.QRect(state_x + 10, 246, 41, font_size))
        self.title_2_state.setStyleSheet("color: white;")
        self.title_2_state.setAlignment(QtCore.Qt.AlignCenter)
        self.title_2_state.setObjectName("title_2_state")
        self.title_2_state.setFont(QtGui.QFont(font, title_font_size))

        self.title_2_dock = QtWidgets.QLabel(self.centralwidget)
        self.title_2_dock.setText("DOCK")

        self.title_2_dock.setGeometry(
            QtCore.QRect(screen_width - self.getWidth(self.title_2_dock) * dock_title_x - margin, 246, 41, font_size))
        self.title_2_dock.setStyleSheet("color: white;")
        self.title_2_dock.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.title_2_dock.setObjectName("title_2_dock")
        self.title_2_dock.setFont(QtGui.QFont(font, title_font_size))

        # endregion

        # region NEXT REFERENCES
        self.next_reference_list = QtWidgets.QVBoxLayout(self.centralwidget)
        self.next_reference_list.setGeometry(QtCore.QRect(0, 270, screen_width, 166))
        self.next_reference_list.setObjectName("next_reference_list")

        # region LINE 7
        self.line = 6
        self.line_7 = QtWidgets.QHBoxLayout()
        self.ref_7 = DataLabel(self.centralwidget, self.line, "ref")
        self.ref_7.setFont(QtGui.QFont(font, line_font_size))
        self.ref_7.setStyleSheet("color:yellow;")
        self.ref_7.setText(data[self.line]['ref'])
        self.ref_7.setGeometry(
            QtCore.QRect(ref_x, ref_list_x + (font_size * self.line) + separator, self.getWidth(self.ref_7) + 8,
                         font_size))

        self.state_7 = DataLabel(self.centralwidget, self.line, "state")
        self.state_7.setFont(QtGui.QFont(font, line_font_size))
        self.state_7.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.state_7.setStyleSheet("color:orange;")
        self.state_7.setText(data[self.line]['state'])
        self.state_7.setGeometry(
            QtCore.QRect(state_x, ref_list_x + separator + (font_size * self.line), state_max_size, font_size))

        self.dock_7 = DataLabel(self.centralwidget, self.line, "dock")
        self.dock_7.setFont(QtGui.QFont(font, line_font_size))
        self.dock_7.setStyleSheet("color:white;")
        self.dock_7.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.dock_7.setText(data[self.line]['dock'])
        self.dock_7.setGeometry(
            QtCore.QRect(screen_width - self.getWidth(self.dock_7) - margin,
                         ref_list_x + (font_size * self.line) + separator,
                         self.getWidth(self.dock_7) + margin, font_size))

        # endregion

        # region LINE 8
        self.line = 7
        self.line_8 = QtWidgets.QHBoxLayout()
        self.ref_8 = DataLabel(self.centralwidget, self.line, "ref")
        self.ref_8.setFont(QtGui.QFont(font, line_font_size))
        self.ref_8.setStyleSheet("color:yellow;")
        self.ref_8.setText(data[self.line]['ref'])
        self.ref_8.setGeometry(
            QtCore.QRect(ref_x, ref_list_x + (font_size * self.line) + separator, self.getWidth(self.ref_8) + 8,
                         font_size))

        self.state_8 = DataLabel(self.centralwidget, self.line, "state")
        self.state_8.setFont(QtGui.QFont(font, line_font_size))
        self.state_8.setStyleSheet("color:orange;")
        self.state_8.setText(data[self.line]['state'])
        self.state_8.setGeometry(
            QtCore.QRect(state_x, ref_list_x + (font_size * self.line) + separator, state_max_size, font_size))
        self.state_8.setAlignment(QtCore.Qt.AlignCenter)

        # self.timer.timeout.connect(self.blink)

        self.dock_8 = DataLabel(self.centralwidget, self.line, "dock")
        self.dock_8.setFont(QtGui.QFont(font, line_font_size))

        self.dock_8.setStyleSheet("color:white;")
        self.dock_8.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.dock_8.setText(data[self.line]['dock'])
        self.dock_8.setGeometry(
            QtCore.QRect(screen_width - self.getWidth(self.dock_8) - margin,
                         ref_list_x + (font_size * self.line) + separator,
                         self.getWidth(self.dock_8) + margin, font_size))

        # endregion

        # region LINE 9
        self.line = 8
        self.line_9 = QtWidgets.QHBoxLayout()
        self.ref_9 = DataLabel(self.centralwidget, self.line, "ref")
        self.ref_9.setFont(QtGui.QFont(font, line_font_size))

        self.ref_9.setStyleSheet("color:yellow;")
        self.ref_9.setFont(QtGui.QFont(font, line_font_size))

        self.ref_9.setText(data[self.line]['ref'])
        self.ref_9.setGeometry(
            QtCore.QRect(ref_x, ref_list_x + (font_size * self.line) + separator, self.getWidth(self.ref_9) + 8,
                         font_size))

        self.state_9 = DataLabel(self.centralwidget, self.line, "state")
        self.state_9.setFont(QtGui.QFont(font, line_font_size))

        self.state_9.setAlignment(QtCore.Qt.AlignCenter)
        self.state_9.setStyleSheet("color:orange;")
        self.state_9.setText(data[self.line]['state'])
        self.state_9.setGeometry(
            QtCore.QRect(state_x, ref_list_x + (font_size * self.line) + separator, state_max_size, font_size))
        # self.timer.timeout.connect(self.blink)

        self.dock_9 = DataLabel(self.centralwidget, self.line, "dock")
        self.dock_9.setFont(QtGui.QFont(font, line_font_size))

        self.dock_9.setStyleSheet("color:white;")
        self.dock_9.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.dock_9.setText(data[self.line]['dock'])
        self.dock_9.setGeometry(
            QtCore.QRect(screen_width - self.getWidth(self.dock_9) - margin,
                         ref_list_x + (font_size * self.line) + separator,
                         self.getWidth(self.dock_9) + margin, font_size))

        # endregion

        # region LINE 10
        self.line = 9
        self.line_10 = QtWidgets.QHBoxLayout()
        self.ref_10 = DataLabel(self.centralwidget, self.line, "ref")
        self.ref_10.setFont(QtGui.QFont(font, line_font_size))

        self.ref_10.setStyleSheet("color:yellow;")
        self.ref_10.setFont(QtGui.QFont(font, line_font_size))

        self.ref_10.setText(data[self.line]['ref'])
        self.ref_10.setGeometry(
            QtCore.QRect(ref_x, ref_list_x + (font_size * self.line) + separator, self.getWidth(self.ref_10) + 8,
                         font_size))

        self.state_10 = DataLabel(self.centralwidget, self.line, "state")
        self.state_10.setFont(QtGui.QFont(font, line_font_size))

        self.state_10.setAlignment(QtCore.Qt.AlignCenter)
        self.state_10.setStyleSheet("color:orange;")
        self.state_10.setText(data[self.line]['state'])
        self.state_10.setGeometry(
            QtCore.QRect(state_x, ref_list_x + (font_size * self.line) + separator, state_max_size, font_size))
        # self.timer.timeout.connect(self.blink)

        self.dock_10 = DataLabel(self.centralwidget, self.line, "dock")
        self.dock_10.setFont(QtGui.QFont(font, line_font_size))

        self.dock_10.setStyleSheet("color:white;")
        self.dock_10.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.dock_10.setText(data[self.line]['dock'])
        self.dock_10.setGeometry(
            QtCore.QRect(screen_width - self.getWidth(self.dock_10) - margin,
                         ref_list_x + (font_size * self.line) + separator,
                         self.getWidth(self.dock_10) + margin, font_size))

        # endregion

        # region LINE 11
        self.line = 10
        self.line_11 = QtWidgets.QHBoxLayout()
        self.ref_11 = DataLabel(self.centralwidget, self.line, "ref")
        self.ref_11.setFont(QtGui.QFont(font, line_font_size))

        self.ref_11.setStyleSheet("color:yellow;")
        self.ref_11.setFont(QtGui.QFont(font, line_font_size))

        self.ref_11.setText(data[self.line]['ref'])
        self.ref_11.setGeometry(
            QtCore.QRect(ref_x, ref_list_x + (font_size * self.line) + separator, self.getWidth(self.ref_11) + 8,
                         font_size))

        self.state_11 = DataLabel(self.centralwidget, self.line, "state")
        self.state_11.setFont(QtGui.QFont(font, line_font_size))

        self.state_11.setAlignment(QtCore.Qt.AlignCenter)
        self.state_11.setStyleSheet("color:orange;")
        self.state_11.setText(data[self.line]['state'])
        self.state_11.setGeometry(
            QtCore.QRect(state_x, ref_list_x + (font_size * self.line) + separator, state_max_size, font_size))
        # self.timer.timeout.connect(self.blink)

        self.dock_11 = DataLabel(self.centralwidget, self.line, "dock")
        self.dock_11.setFont(QtGui.QFont(font, line_font_size))

        self.dock_11.setStyleSheet("color:white;")
        self.dock_11.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.dock_11.setText(data[self.line]['dock'])
        self.dock_11.setGeometry(
            QtCore.QRect(screen_width - self.getWidth(self.dock_11) - margin,
                         ref_list_x + (font_size * self.line) + separator,
                         self.getWidth(self.dock_11) + margin, font_size))

        # endregion

        # region LINE 12
        self.line = 11
        self.line_12 = QtWidgets.QHBoxLayout()
        self.ref_12 = DataLabel(self.centralwidget, self.line, "ref")
        self.ref_12.setFont(QtGui.QFont(font, line_font_size))

        self.ref_12.setStyleSheet("color:yellow;")
        self.ref_12.setFont(QtGui.QFont(font, line_font_size))

        self.ref_12.setText(data[self.line]['ref'])
        self.ref_12.setGeometry(
            QtCore.QRect(ref_x, ref_list_x + (font_size * self.line) + separator, self.getWidth(self.ref_12) + 8,
                         font_size))

        self.state_12 = DataLabel(self.centralwidget, self.line, "state")
        self.state_12.setFont(QtGui.QFont(font, line_font_size))

        self.state_12.setAlignment(QtCore.Qt.AlignCenter)
        self.state_12.setStyleSheet("color:orange;")
        self.state_12.setText(data[self.line]['state'])
        self.state_12.setGeometry(
            QtCore.QRect(state_x, ref_list_x + (font_size * self.line) + separator, state_max_size, font_size))
        # self.timer.timeout.connect(self.blink)

        self.dock_12 = DataLabel(self.centralwidget, self.line, "dock")
        self.dock_12.setFont(QtGui.QFont(font, line_font_size))

        self.dock_12.setStyleSheet("color:white;")
        self.dock_12.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.dock_12.setText(data[self.line]['dock'])
        self.dock_12.setGeometry(
            QtCore.QRect(screen_width - self.getWidth(self.dock_12) - margin,
                         ref_list_x + (font_size * self.line) + separator,
                         self.getWidth(self.dock_12) + margin, font_size))

        # endregion

        # endregion

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_1_reference.setText(_translate("MainWindow", "REFERENCE"))
        self.title_1_state.setText(_translate("MainWindow", "STATE"))
        self.title_1_dock.setText(_translate("MainWindow", "DOCK"))
        self.title_2_reference.setText(_translate("MainWindow", "NEXT REF."))
        self.title_2_state.setText(_translate("MainWindow", "STATE"))
        self.title_2_dock.setText(_translate("MainWindow", "DOCK"))

    def getWidth(self, text):
        return text.fontMetrics().boundingRect(text.text()).width()
