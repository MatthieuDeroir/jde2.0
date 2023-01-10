from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QVBoxLayout, QSizePolicy
import threading

from DisplayLabel import DisplayLabel
from data import *
from utils.req import req

class VideoThread(QtCore.QThread):
    def __init__(self, url, videoWidget):
        QtCore.QThread.__init__(self)
        self.url = url
        self.videoWidget = videoWidget

    def run(self):
        mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        mediaPlayer.setVideoOutput(self.videoWidget)
        mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.url)))
        mediaPlayer.play()

class Ui_Splitscreen(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(screen_width, screen_height)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        layout = QVBoxLayout()
        self.centralwidget.setLayout(layout)
        MainWindow.setCentralWidget(self.centralwidget)


        

        try:
            self.fetched_datas = req("get", ip_fs).json()
        except:
            print("cant fetch datas")

        for i in range(1, 4):
            if self.fetched_datas[i]['format'] == 'mp4':
                print("coucou")
                videoWidget = QVideoWidget()
                videoWidget.setFixedHeight(145)
                layout.addWidget(videoWidget)
                videoWidget.moveToThread(QtCore.QCoreApplication.instance().thread())
                thread = VideoThread('/path/to/video' + str(i) + '.mp4', videoWidget)
                thread.start()
                
                # self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
                # layout.addWidget(videoWidgets[i - 1])
            
                # self.mediaPlayer.setObjectName("video" + str(i))
                # self.mediaPlayer.setVideoOutput(videoWidgets[i - 1])

                # self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile('/home/pi/jde/panel/GUI/Chats.mp4')))
                # videoWidgets[i - 1].setFixedHeight(145)
                
                # self.mediaPlayer.play()
                # mediaPlayer.error.connect(self.handleError)
            else:
                display_label = DisplayLabel(self.centralwidget, i)
                display_label.setObjectName("display_label_" + str(i))
                
                layout.addWidget(display_label)
                
    def handleStateChanged(self, state):
        if state == QMediaPlayer.LoadedMedia:
            mediaPlayer.play()
            print("media is loaded")
        elif state == QMediaPlayer.StoppedState:
            mediaPlayer.play()
            print("media has stopped")


    def handleError(self, error):
        if error == QMediaPlayer.ResourceError:
            print("Media file not found or network error")
        elif error == QMediaPlayer.QMediaPlayer.FormatError:
            print("Media file format not supported")
        elif error == QMediaPlayer.AccessDeniedError:
            print("Access to media file denied")
        else:
            print("Error while playing the media file")