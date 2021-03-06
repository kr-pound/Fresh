# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkout.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(583, 246)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CheckoutLabel = QtWidgets.QLabel(self.centralwidget)
        self.CheckoutLabel.setGeometry(QtCore.QRect(30, 10, 441, 61))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(True)
        self.CheckoutLabel.setFont(font)
        self.CheckoutLabel.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.CheckoutLabel.setObjectName("CheckoutLabel")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 120, 491, 221))
        self.frame.setStyleSheet("QFrame {\n"
"    background-color: rgb(237, 236, 233);\n"
"    border-radius: 50px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.TotalLabel = QtWidgets.QLabel(self.frame)
        self.TotalLabel.setGeometry(QtCore.QRect(30, 30, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.TotalLabel.setFont(font)
        self.TotalLabel.setStyleSheet("")
        self.TotalLabel.setObjectName("TotalLabel")
        self.CloseButton = QtWidgets.QPushButton(self.frame)
        self.CloseButton.setGeometry(QtCore.QRect(330, 80, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.CloseButton.setFont(font)
        self.CloseButton.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: rgb(0, 85, 0);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #64AB25;\n"
"    background: #333;\n"
"    border-radius: 15px;\n"
"}")
        self.CloseButton.setObjectName("CloseButton")
        self.BillButton = QtWidgets.QPushButton(self.frame)
        self.BillButton.setGeometry(QtCore.QRect(330, 30, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.BillButton.setFont(font)
        self.BillButton.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: rgb(0, 85, 0);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: black;\n"
"    background: lightgreen;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"")
        self.BillButton.setObjectName("BillButton")
        self.PriceLabel = QtWidgets.QLabel(self.frame)
        self.PriceLabel.setGeometry(QtCore.QRect(140, 30, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        self.PriceLabel.setFont(font)
        self.PriceLabel.setStyleSheet("background-color: white;\n"
"border-radius: 15px;")
        self.PriceLabel.setText("")
        self.PriceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PriceLabel.setObjectName("PriceLabel")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-150, -80, 761, 411))
        self.label.setStyleSheet("background-image: url(:/Bg/Background.jpg);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Bg/Background.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(-90, -110, 591, 192))
        self.graphicsView.setStyleSheet("QFrame {\n"
"    background-color: rgb(237, 236, 233);\n"
"    border-radius: 50px;\n"
"}")
        self.graphicsView.setObjectName("graphicsView")
        self.label.raise_()
        self.graphicsView.raise_()
        self.CheckoutLabel.raise_()
        self.frame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CheckoutLabel.setText(_translate("MainWindow", "Check out"))
        self.TotalLabel.setText(_translate("MainWindow", "Total"))
        self.CloseButton.setText(_translate("MainWindow", "OK"))
        self.BillButton.setText(_translate("MainWindow", "Bill Print"))
import Bg_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
