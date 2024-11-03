"""pip install PyQt6"""
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic # doc giao dien ui
import sys # he thong may tinh
import webbrowser

##webbrowser.open("https://www.youtube.com/watch?v=0tU54gOwKKs")

from model.account import account

class LoginPage(QMainWindow):
    # ham khoi tao
    def __init__(self):
        super().__init__()
        # read
        uic.loadUi("UI-GiaoDien/Log_in.ui",self)
        # event
        self.btn_Login.clicked.connect(self.checkLogin)
    def checkLogin(self):
        myacc = account()
        check = myacc.Checking(self.txt_Username.text(),self.txt_Password.text())
        if check == True:
            self.close()
            ip.show()
        else:
            print("Failure")

class IphonePage(QMainWindow):
    # ham khoi tao
    def __init__(self):
        super().__init__()
        # read
        uic.loadUi("UI-GiaoDien/Dien_thoai.ui",self)

if __name__ == "__main__":
    # tao 1 app
    app = QApplication(sys.argv)
    lg = LoginPage()
    ip = IphonePage()
    lg.show()
    app.exec()