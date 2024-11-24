from PyQt6.QtWidgets import QApplication,QMainWindow,QMessageBox
from PyQt6 import uic
import sys

class account:
    def __init__(self,_user = "gmail.com",_pass = "XXXXX"):
        self.username = _user
        self.password = _pass
    def Checking(self,_user,_pass):
        if _user == self.username and _pass == self.password:
            return True
        else:
            return False

class Sign_in(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI-GiaoDien/HW_Sign_in.ui",self)
        self.btnSignin.clicked.connect(self.checkSignin)
    def checkSignin(self):
        myacc = account()
        check = myacc.Checking(self.txtUsername.text(),self.txtPassword.text())
        if check == True:
            yes = QMessageBox()
            yes.setWindowTitle("Sign_in_successful")
            yes.setIcon(QMessageBox.Icon.Information)
            yes.setText("You're signed in !")
            yes.setStyleSheet("background-color:lightgreen ; color:black ;")
            sys.exit(yes.exec())
        else:
            wrong = QMessageBox()
            wrong.setWindowTitle("Sign_in_error")
            wrong.setIcon(QMessageBox.Icon.Critical)
            wrong.setText("Sign in failed :(")
            wrong.setStyleSheet("background-color:coral ; color:black ;")
            sys.exit(wrong.exec())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    sgi = Sign_in()
    sgi.show()
    app.exec()