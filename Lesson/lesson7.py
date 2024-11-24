import sys
from PyQt6.QtWidgets import QApplication,QMessageBox

app = QApplication(sys.argv)
#tao thong bao
htb = QMessageBox()
#dat tieu de
htb.setWindowTitle("Information go here")
#icon
htb.setIcon(QMessageBox.Icon.Warning)
#! thong bao
htb.setText("Quit out?")
#change stylesheet
htb.setStyleSheet("background-color:tan ; color:black ;")
sys.exit(htb.exec())