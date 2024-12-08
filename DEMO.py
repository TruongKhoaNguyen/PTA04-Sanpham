from PyQt6.QtWidgets import QApplication,QMainWindow,QMessageBox
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6 import uic
import sys
import webbrowser

class Demo(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI-GiaoDien/homepage.ui",self)
        #self.btnProfile.clicked.connect(self.showProfile)
        self.btnPlay_PP.clicked.connect(lambda: self.mainStack.setCurrentIndex(1))
        self.btnPlay_PVZ.clicked.connect(lambda: self.mainStack.setCurrentIndex(2))
        self.btnPlay_RB.clicked.connect(lambda: self.mainStack.setCurrentIndex(3))
        self.btnPlay_GD.clicked.connect(lambda: self.mainStack.setCurrentIndex(4))
        self.btnPlay_GD.clicked.connect(lambda: self.mainStack.setCurrentIndex(4))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    #profile = Profile()
    demo.show()
    app.exec()