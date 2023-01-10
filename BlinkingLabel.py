from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QTimer,QDateTime

class BlinkingLabel(QLabel):
    def __init__(self, widget, state):
        super().__init__(widget)
        self.timer = QTimer()
        self.state = state

        self.timer.start(1000)
        if self.state == 'COME':
            self.timer.timeout.connect(self.blink)

    def blink(self):
        if self.isHidden():
            self.show()
        else:
            self.hide()

