from PyQt5 import QtCore, QtGui, QtWidgets
from _register_design import Ui_MainWindow as Ui_RegisterWindow
from __database import database

from os import environ

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

class RegisterWindow(QtWidgets.QMainWindow, Ui_RegisterWindow):
    login = QtCore.pyqtSignal()

    username = None
    password = None

    def __init__(self, parent=None):
        #super the class to setup the Ui
        super(RegisterWindow, self).__init__(parent)
        self.setupUi(self)

        self.db = database

        #after push the button --> submit data and go back
        self.ConfirmButton.clicked.connect(self.receiveData)

    @QtCore.pyqtSlot()
    def loginTransfer(self):
        self.login.emit()
        self.close()

    def receiveData(self):
        if (self.PasswordLineEdit.text() == self.RePasswordLineEdit.text()) and (self.UsernameLineEdit.text() != ""):
            self.username = self.UsernameLineEdit.text()
            self.password = self.PasswordLineEdit.text()

            self.submitData()
            self.clear_lineEdit()
            self.loginTransfer()

        else:
            print("Wrong Input")

    #clear line edit after push button
    def clear_lineEdit(self):
        cleared_text = ""

        self.UsernameLineEdit.setText(cleared_text)
        self.PasswordLineEdit.setText(cleared_text)
        self.RePasswordLineEdit.setText(cleared_text)

    #send data to __database.py
    def submitData(self):
        self.db.username = self.username
        self.db.password = self.password

        self.db.push_users(self.db)


