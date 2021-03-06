# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(603, 581)
        MainWindow.setStyleSheet("background-color: rgb(152, 238, 152);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LoginFrame = QtWidgets.QFrame(self.centralwidget)
        self.LoginFrame.setGeometry(QtCore.QRect(30, 30, 531, 521))
        self.LoginFrame.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LoginFrame.setStyleSheet("QFrame {\n"
"    background: white;\n"
"    border-radius: 20px;\n"
"}")
        self.LoginFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LoginFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LoginFrame.setObjectName("LoginFrame")
        self.Username = QtWidgets.QLineEdit(self.LoginFrame)
        self.Username.setGeometry(QtCore.QRect(160, 240, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Username.setFont(font)
        self.Username.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Username.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Username.setStyleSheet("QLineEdit {\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: #717072;\n"
"    border-bottom: 1px solid #717072;\n"
"}")
        self.Username.setText("")
        self.Username.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.Username.setCursorPosition(0)
        self.Username.setDragEnabled(True)
        self.Username.setReadOnly(False)
        self.Username.setClearButtonEnabled(True)
        self.Username.setObjectName("Username")
        self.Password = QtWidgets.QLineEdit(self.LoginFrame)
        self.Password.setGeometry(QtCore.QRect(160, 290, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Password.setFont(font)
        self.Password.setStyleSheet("QLineEdit {\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: #717072;\n"
"    border-bottom: 1px solid #717072;\n"
"}")
        self.Password.setInputMask("")
        self.Password.setText("")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setDragEnabled(True)
        self.Password.setClearButtonEnabled(True)
        self.Password.setObjectName("Password")
        self.LoginButton = QtWidgets.QPushButton(self.LoginFrame)
        self.LoginButton.setGeometry(QtCore.QRect(290, 440, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.LoginButton.setFont(font)
        self.LoginButton.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 170, 0);\n"
"    border-radius: 15px;;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #64AB25;\n"
"    background: #333;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"")
        self.LoginButton.setObjectName("LoginButton")
        self.CreateAccountButton = QtWidgets.QPushButton(self.LoginFrame)
        self.CreateAccountButton.setGeometry(QtCore.QRect(90, 440, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.CreateAccountButton.setFont(font)
        self.CreateAccountButton.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 170, 0);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #64AB25;\n"
"    background: #333;\n"
"    border-radius: 15px;\n"
"}")
        self.CreateAccountButton.setObjectName("CreateAccountButton")
        self.label_5 = QtWidgets.QLabel(self.LoginFrame)
        self.label_5.setGeometry(QtCore.QRect(-30, -140, 491, 171))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font: 10pt \"Segoe UI\";\n"
"background-color: rgb(255, 255, 255,0);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.LoginFrame)
        self.label.setGeometry(QtCore.QRect(150, -30, 231, 231))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Logo/Logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.WelcomeLabel = QtWidgets.QLabel(self.LoginFrame)
        self.WelcomeLabel.setGeometry(QtCore.QRect(30, 160, 471, 71))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        self.WelcomeLabel.setFont(font)
        self.WelcomeLabel.setStyleSheet("color: rgb(0, 85, 0);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.WelcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.WelcomeLabel.setObjectName("WelcomeLabel")
        self.WelcomeLabel_2 = QtWidgets.QLabel(self.LoginFrame)
        self.WelcomeLabel_2.setGeometry(QtCore.QRect(20, 370, 491, 21))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.WelcomeLabel_2.setFont(font)
        self.WelcomeLabel_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.WelcomeLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.WelcomeLabel_2.setObjectName("WelcomeLabel_2")
        self.WelcomeLabel_3 = QtWidgets.QLabel(self.LoginFrame)
        self.WelcomeLabel_3.setGeometry(QtCore.QRect(20, 390, 491, 21))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.WelcomeLabel_3.setFont(font)
        self.WelcomeLabel_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.WelcomeLabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.WelcomeLabel_3.setObjectName("WelcomeLabel_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(-290, -180, 921, 791))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/Bg/Background.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_4.raise_()
        self.LoginFrame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Username.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.Username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.Password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.LoginButton.setText(_translate("MainWindow", "Login"))
        self.CreateAccountButton.setText(_translate("MainWindow", "Create Account"))
        self.WelcomeLabel.setText(_translate("MainWindow", "Welcome to Fresh!"))
        self.WelcomeLabel_2.setText(_translate("MainWindow", "Please create an account "))
        self.WelcomeLabel_3.setText(_translate("MainWindow", "if you don\'t have one before start using."))
import Bg_rc
import Logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
