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
        self.btnPlay_PP.clicked.connect(lambda: self.mainStack.setCurrentIndex(1))
        self.btnPlay_PVZ.clicked.connect(lambda: self.mainStack.setCurrentIndex(2))
        self.btnPlay_RB.clicked.connect(lambda: self.mainStack.setCurrentIndex(3))
        self.btnPlay_GD.clicked.connect(lambda: self.mainStack.setCurrentIndex(4))
        self.btnPlay_FF.clicked.connect(lambda: self.mainStack.setCurrentIndex(5))
        self.btnPlay_M.clicked.connect(lambda: self.mainStack.setCurrentIndex(6))
        self.btnPlay_BMW.clicked.connect(lambda: self.mainStack.setCurrentIndex(7))
        self.btnPlay_A.clicked.connect(lambda: self.mainStack.setCurrentIndex(8))
        self.btnHome.clicked.connect(lambda: self.mainStack.setCurrentIndex(0))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    #profile = Profile()
    demo.show()
    app.exec()