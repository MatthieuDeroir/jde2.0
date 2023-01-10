from config import *
from src.Modes.Fullscreen import Ui_Fullscreen
from src.Modes.Splitscreen import Ui_Splitscreen
from src.Modes.Trucks import Ui_Truckscreen


class Main(QtWidgets.QMainWindow):
    stop = 1

    def __init__(self, mode):
        super(Main, self).__init__()

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.move(0, 0)

        self.mode = mode
        self.current_mode = 3
        self.hasChangedDisplayMode = True
        self.index = index

        self.medias = []
        self.current_medias = []

        self.week_start = ["", ""]
        self.stop = ["", ""]
        self.veille = True
        self.lastMedia = True
        # build ui
        self.getOption()
        self.timer = QTimer(self)
        self.timer.start(1000)

        self.timer.timeout.connect(self.updateMode)
        self.timer.timeout.connect(self.getOption)
        self.timer.timeout.connect(self.screenBlanking)

    def getOption(self):
        try:
            if self.current_mode is not self.mode or self.modeChange == True:
                self.hasChangedDisplayMode = True
                self.current_mode = self.mode
            if self.mode == 3:
                if self.index > 4:
                    if len(self.medias) != 5:
                        self.timer.start(self.medias[self.index]['duration'] * 1000)
                        self.ui = Ui_Fullscreen(self.index)
                        self.ui.setupUi(self)
                        self.noMedia = True
                    if self.index >= len(self.medias) - 1:
                        self.index = 3
                elif self.index == 4 and self.noMedia == True:
                    self.timer.start(self.medias[self.index]['duration'] * 1000)
                    self.ui = Ui_Truckscreen()
                    self.ui.setupUi(self)
                    self.noMedia = False

                self.index = self.index + 1
            elif self.mode == 2 and self.hasChangedDisplayMode == True:
                self.ui = Ui_Fullscreen(0)

            elif self.mode == 1 and self.hasChangedDisplayMode == True:
                self.ui = Ui_Splitscreen()

            elif self.mode == 0 or self.mode == 4 and self.hasChangedDisplayMode == True:
                self.ui = Ui_Fullscreen(1000)

            if self.hasChangedDisplayMode and self.mode != 3:
                self.hasChangedDisplayMode = False
                self.noMedia = True
                try:
                    self.modeChange = req("put", ip_mode_put, {'modeChange': False})
                except:
                    print("Can't put modeChange to false at " + ip_mode_put)

                self.ui.setupUi(self)

            return self.index
        except:
            print("Can't update mode, current mode is " + str(self.mode))

    def updateMode(self):
        try:
            self.mode = int(req("get", ip_mode).json()[0]['activeMode'])
            self.modeBack = int(req("get", ip_mode).json()[0]['modeBack'])
            self.modeChange = req("get", ip_mode).json()[0]['modeChange']
        except:
            print("Can't fetch mode options at " + ip_mode)
        try:
            self.medias = req("get", ip_fs).json()
        except:
            print("Can't fetch media path at " + ip_fs)
        try:
            # jours de la semaine
            self.week_start = req("get", ip_sb).json()[0]['start'].split(":")
            self.week_stop = req("get", ip_sb).json()[0]['stop'].split(":")
            # samedi
            self.saturday_start = req("get", ip_sb).json()[1]['start'].split(":")
            self.saturday_stop = req("get", ip_sb).json()[1]['stop'].split(":")
            # dimanche
            self.sunday_start = req("get", ip_sb).json()[2]['start'].split(":")
            self.sunday_stop = req("get", ip_sb).json()[2]['stop'].split(":")
        except:
            print("Can't fetch shutdown time at " + ip_sb)

    def screenBlanking(self):
        now = datetime.now()
        self.current_hour = now.strftime("%H")
        self.current_minute = now.strftime("%M")
        self.current_days = now.strftime("%A")
        try:
            if (self.current_days == "Sunday"):

                self.display("on") if ((
                        self.sunday_start[0] < self.current_hour or self.sunday_start[0] == self.current_hour and
                        self.sunday_start[1] <= self.current_minute)) else self.display("off")
            elif self.current_days == "Saturday":
                self.display("on") if ((
                                               self.saturday_start[0] < self.current_hour or self.saturday_start[
                                           0] == self.current_hour and
                                               self.saturday_start[1] <= self.current_minute) and self.saturday_stop[
                                           0] > self.current_hour or
                                       self.saturday_start[0] == self.current_hour and
                                       self.saturday_stop[1] > self.current_minute) else self.display("off")
            else:
                self.display("on") if ((
                                               self.week_start[0] < self.current_hour or self.week_start[
                                           0] == self.current_hour and
                                               self.week_start[1] <= self.current_minute) and self.week_stop[
                                           0] > self.current_hour or
                                       self.week_start[0] == self.current_hour and
                                       self.week_stop[1] > self.current_minute) else self.display("off")

        except:
            print('Screen blanking error - value not found, they might not have been initialised yet')

    def display(self, state):
        if state == "on" and self.veille == False:
            try:
                requests.put(ip_mode_put, data={'activeMode': self.modeBack})
                self.veille = True
            except:
                print("Can't put 'stop screensaver' to modeBack at " + ip_mode_put)
        elif state == "off" and self.veille == True:
            try:
                requests.put(ip_mode_put, data={'activeMode': '0'})
                self.veille = False
            except:
                print("Can't put 'start screensaver' to modeBack at " + ip_mode_put)


if __name__ == '__main__':
    mode = 3
    medias = []
    index = 3

    app = QtWidgets.QApplication(sys.argv)
    main = Main(mode)
    main.setStyleSheet("QMainWindow { background-color: black; }")

    main.show()
    sys.exit(app.exec_())
