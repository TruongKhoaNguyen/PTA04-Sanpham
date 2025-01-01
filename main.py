"""pip install PyQt6"""
from PyQt6.QtWidgets import QApplication,QMainWindow,QMessageBox
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
            #ip.show()
        else:
            htb = QMessageBox()
            #dat tieu de
            htb.setWindowTitle("Information go here")
            #icon
            htb.setIcon(QMessageBox.Icon.Warning)
            #! thong bao
            htb.setText("ERROR 404 :(")
            #change stylesheet
            htb.setStyleSheet("background-color:tan ; color:black ;")
            sys.exit(htb.exec())

class IphonePage(QMainWindow):
    # ham khoi tao
    def __init__(self):
        super().__init__()
        # read
        uic.loadUi("UI-GiaoDien/Dien_thoai.ui",self)

class Homepage(QMainWindow):
    # ham khoi tao
    def __init__(self):
        super().__init__()
        # read
        uic.loadUi("UI-GiaoDien/homepage.ui",self)
        #connect event
        self.btnProfile.clicked.connect(self.showProfile)
        self.btnPlay_PP.clicked.connect(lambda: self.runGame("https://store.steampowered.com/app/1721470/Poppy_Playtime/"))
        self.btnPlay_PVZ.clicked.connect(lambda: self.runGame("https://pvz.ee"))
        self.btnPlay_RB.clicked.connect(lambda: self.runGame("https://www.roblox.com/home"))
        self.btnPlay_GD.clicked.connect(lambda: self.runGame("https://vn.crazygames.com/trò-chơi/geometry-dash-online"))
    def showProfile(self):
        profile.show()
    def runGame(self,link_game):
        webbrowser.open(link_game)

class Profile(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI-GiaoDien/Profile.ui",self)
        self.information()
        self.btnFacebook.clicked.connect(self.FB)
        self.btnSave.clicked.connect(self.save)

    def save(self):
        prototype1 = self.txtHo.text()
        prototype2 = self.txtTen.text()
        prototype3 = self.txtSodienthoai.text()
        prototype4 = self.txtDiachi.text()
        prototype5 = self.txtBaihat.text()
        list_kill = [prototype1,prototype2,prototype3,prototype4,prototype5]
        print(list_kill)

    def FB(self):
        webbrowser.open("https://www.facebook.com/messages/t/27020118477575302")
    
    def information(self):
        #self.txtUsername.setText("Gooigi")
        #self.txtEmail.setText("Doraemon@gmail.com")
        self.txtHo.setText("Nguyễn")
        self.txtTen.setText("Khoa")
        self.txtSodienthoai.setText("098 XXX XXXX")
        self.txtDiachi.setText("Where...")
        self.txtBaihat.setText("Back on Dash")

if __name__ == "__main__":
    # tao 1 app
    app = QApplication(sys.argv)
    #lg = LoginPage()
    #ip = IphonePage()
    home = Homepage()
    #lg.show()
    profile = Profile()
    home.show()
    app.exec()