from PyQt6.QtWidgets import QApplication,QMainWindow,QMessageBox,QWidget
from PyQt6 import uic
import sys
import webbrowser

class account:
    def __init__(self,_user = "Khoa@gmail.com" ,_pass = "1234"):
        self.username = _user
        self.password = _pass
    def Checking(self,_user,_pass):
        if _user == self.username and _pass == self.password:
            return True
        else:
            return False

class SignIn(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI-GiaoDien/HW_Sign_in.ui",self)
        self.setWindowTitle("Sign in")
        self.btnSignin.clicked.connect(self.checkLogin)
    def checkLogin(self):
        myacc = account()
        check = myacc.Checking(self.txtUsername.text(),self.txtPassword.text())
        if check == True:
            demo.show()
            self.close()
        else:
            htb = QMessageBox()
            htb.setWindowTitle("Login in failed")
            htb.setIcon(QMessageBox.Icon.Warning)
            htb.setText("Wrong Information :(")
            htb.setStyleSheet("background-color:tan ; color:black ;")
            htb.exec()

class Demo(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI-GiaoDien/homepage.ui",self)
        self.setWindowTitle("Game Centre")
        # main
        self.btnPlay_PP.clicked.connect(lambda: self.mainStack.setCurrentIndex(1))
        self.btnPlay_PVZ.clicked.connect(lambda: self.mainStack.setCurrentIndex(2))
        self.btnPlay_RB.clicked.connect(lambda: self.mainStack.setCurrentIndex(3))
        self.btnPlay_GD.clicked.connect(lambda: self.mainStack.setCurrentIndex(4))
        self.btnPlay_FF.clicked.connect(lambda: self.mainStack.setCurrentIndex(5))
        self.btnPlay_M.clicked.connect(lambda: self.mainStack.setCurrentIndex(6))
        self.btnPlay_BMW.clicked.connect(lambda: self.mainStack.setCurrentIndex(7))
        self.btnPlay_A.clicked.connect(lambda: self.mainStack.setCurrentIndex(8))
        self.btnHome.clicked.connect(lambda: self.mainStack.setCurrentIndex(0))
        self.btnExit.clicked.connect(self.quit)
        self.btnProfile.clicked.connect(self.showProfile)
        # play
        self.letplay_PP.clicked.connect(lambda: self.runit("https://store.steampowered.com/app/1721470/Poppy_Playtime/"))
        self.letplay_PVZ.clicked.connect(lambda: self.runit("https://apps.apple.com/vn/app/plants-vs-zombies/id893677096?l=vi"))
        self.letplay_RB.clicked.connect(lambda: self.runit("https://www.xbox.com/en-US/games/store/roblox/9nblgggzm6wm?ocid=storeforweb"))
        self.letplay_GD.clicked.connect(lambda: self.runit("https://store.steampowered.com/app/322170/Geometry_Dash/"))
        self.letplay_FF.clicked.connect(lambda: self.runit("https://apps.apple.com/us/app/free-fire-winterlands/id1300146617"))
        self.letplay_M.clicked.connect(lambda: self.runit("https://www.nintendo.com/us/store/products/arcade-archives-vs-super-mario-bros-switch/"))
        self.letplay_BMW.clicked.connect(lambda: self.runit("https://www.playstation.com/en-vn/games/black-myth-wukong/"))
        self.letplay_A.clicked.connect(lambda: self.runit("https://store.steampowered.com/app/945360/Among_Us/"))
    def quit(self):
        QApplication.quit()
    def showProfile(self):
        profile.show()
    def runit(self,link):
        webbrowser.open(link)

class Profile(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI-GiaoDien/Profile.ui",self)
        self.setWindowTitle("My profile")
        self.information()
        self.btnFacebook.clicked.connect(self.FB)
        self.btnDiscord.clicked.connect(self.DC)
        self.btnSave.clicked.connect(self.save)
    def save(self):
        prototype1 = self.txtHo.text()
        prototype2 = self.txtTen.text()
        prototype3 = self.txtSodienthoai.text()
        prototype4 = self.txtDiachi.text()
        prototype5 = self.txtBaihat.text()
        prototype6 = self.mybirthday.text()
        list_kill = [prototype1,prototype2,prototype3,prototype4,prototype6,prototype5]
        print(list_kill)
    def FB(self):
        webbrowser.open("https://www.facebook.com/messages/t/27020118477575302")
    def DC(self):
        webbrowser.open("https://discord.com/channels/@me")
    def information(self):
        #self.txtUsername.setText("Gooigi")
        #self.txtEmail.setText("Doraemon@gmail.com")
        self.txtHo.setText("Nguyễn")
        self.txtTen.setText("Khoa")
        self.txtSodienthoai.setText("098 XXX XXXX")
        self.txtDiachi.setText("Where...")
        self.txtBaihat.setText("Back on Dash")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    signin = SignIn()
    profile = Profile()
    signin.show()
    app.exec()