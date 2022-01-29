from PyQt5 import QtCore, QtGui, QtWidgets

from _login_design import Ui_MainWindow as Ui_LoginWindow

from os import environ
from __database import database

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"


class LoginWindow(QtWidgets.QMainWindow, Ui_LoginWindow):
    logged = QtCore.pyqtSignal()
    register = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        #super the class to setup the Ui
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        #after push the button --> check user id
        self.LoginButton.clicked.connect(self.authenticate)
        self.CreateAccountButton.clicked.connect(self.registerTransfer)

    @QtCore.pyqtSlot()
    def registerTransfer(self):
        self.register.emit()

    @QtCore.pyqtSlot()
    def authenticate(self):
        #user & pass entered
        local_username = self.Username.text()
        local_password = self.Password.text()

        #user & pass get from db
        database.get_password(database, 'username', local_username)
        #print("\nValid Username: " + database.username)
        #print("Valid Password: " + database.password + "\n")

        #login and close the previous window
        if database.username == local_username and database.password == local_password:
            self.logged.emit()
            self.close()

            print("Logging in\n")
        else:
            print("Wrong Input")


        
        


    


