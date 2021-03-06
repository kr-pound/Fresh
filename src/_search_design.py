# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(982, 618)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ProductFrame1 = QtWidgets.QFrame(self.centralwidget)
        self.ProductFrame1.setGeometry(QtCore.QRect(70, 210, 151, 361))
        self.ProductFrame1.setStyleSheet("QFrame {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: lightgray;\n"
"    border-radius: 30px;\n"
"}")
        self.ProductFrame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ProductFrame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ProductFrame1.setObjectName("ProductFrame1")
        self.ProductPicture1 = QtWidgets.QLabel(self.ProductFrame1)
        self.ProductPicture1.setGeometry(QtCore.QRect(10, 10, 131, 91))
        self.ProductPicture1.setStyleSheet("QLabel {\n"
"    image: url(:/)\n"
"}")
        self.ProductPicture1.setText("")
        self.ProductPicture1.setObjectName("ProductPicture1")
        self.ProductLabel1 = QtWidgets.QLabel(self.ProductFrame1)
        self.ProductLabel1.setGeometry(QtCore.QRect(10, 110, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.ProductLabel1.setFont(font)
        self.ProductLabel1.setText("")
        self.ProductLabel1.setObjectName("ProductLabel1")
        self.ProductDescription1 = QtWidgets.QTextBrowser(self.ProductFrame1)
        self.ProductDescription1.setGeometry(QtCore.QRect(10, 130, 131, 121))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(10)
        self.ProductDescription1.setFont(font)
        self.ProductDescription1.setStyleSheet("color: black;")
        self.ProductDescription1.setObjectName("ProductDescription1")
        self.BuyingButton1 = QtWidgets.QPushButton(self.ProductFrame1)
        self.BuyingButton1.setGeometry(QtCore.QRect(20, 310, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        font.setBold(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.BuyingButton1.setFont(font)
        self.BuyingButton1.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background: rgb(0, 121, 0);\n"
"    border-radius: 15px;\n"
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
        self.BuyingButton1.setObjectName("BuyingButton1")
        self.ProductAmount1 = QtWidgets.QLabel(self.ProductFrame1)
        self.ProductAmount1.setGeometry(QtCore.QRect(20, 270, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.ProductAmount1.setFont(font)
        self.ProductAmount1.setStyleSheet("color: black;")
        self.ProductAmount1.setAlignment(QtCore.Qt.AlignCenter)
        self.ProductAmount1.setObjectName("ProductAmount1")
        self.ProductIncrease1 = QtWidgets.QPushButton(self.ProductFrame1)
        self.ProductIncrease1.setGeometry(QtCore.QRect(110, 270, 21, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.ProductIncrease1.setFont(font)
        self.ProductIncrease1.setStyleSheet("QPushButton {\n"
"    background: white;\n"
"}")
        self.ProductIncrease1.setObjectName("ProductIncrease1")
        self.ProductDecrease1 = QtWidgets.QPushButton(self.ProductFrame1)
        self.ProductDecrease1.setGeometry(QtCore.QRect(20, 270, 21, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.ProductDecrease1.setFont(font)
        self.ProductDecrease1.setStyleSheet("QPushButton {\n"
"    background: white;\n"
"}")
        self.ProductDecrease1.setObjectName("ProductDecrease1")
        self.TickMark1 = QtWidgets.QLabel(self.ProductFrame1)
        self.TickMark1.setGeometry(QtCore.QRect(10, 10, 21, 21))
        self.TickMark1.setStyleSheet("QLabel {\n"
"    image: url(:);\n"
"}")
        self.TickMark1.setText("")
        self.TickMark1.setObjectName("TickMark1")
        self.ProductFrame3 = QtWidgets.QFrame(self.centralwidget)
        self.ProductFrame3.setGeometry(QtCore.QRect(410, 210, 151, 361))
        self.ProductFrame3.setStyleSheet("QFrame {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: lightgray;\n"
"    border-radius: 30px;\n"
"}")
        self.ProductFrame3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ProductFrame3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ProductFrame3.setObjectName("ProductFrame3")
        self.ProductPicture3 = QtWidgets.QLabel(self.ProductFrame3)
        self.ProductPicture3.setGeometry(QtCore.QRect(10, 10, 131, 91))
        self.ProductPicture3.setStyleSheet("QLabel {\n"
"    image: url(:/)\n"
"}")
        self.ProductPicture3.setText("")
        self.ProductPicture3.setObjectName("ProductPicture3")
        self.ProductLabel3 = QtWidgets.QLabel(self.ProductFrame3)
        self.ProductLabel3.setGeometry(QtCore.QRect(10, 110, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.ProductLabel3.setFont(font)
        self.ProductLabel3.setText("")
        self.ProductLabel3.setObjectName("ProductLabel3")
        self.ProductDescription3 = QtWidgets.QTextBrowser(self.ProductFrame3)
        self.ProductDescription3.setGeometry(QtCore.QRect(10, 130, 131, 121))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(10)
        self.ProductDescription3.setFont(font)
        self.ProductDescription3.setStyleSheet("color: black;")
        self.ProductDescription3.setObjectName("ProductDescription3")
        self.BuyingButton3 = QtWidgets.QPushButton(self.ProductFrame3)
        self.BuyingButton3.setGeometry(QtCore.QRect(20, 310, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        font.setBold(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.BuyingButton3.setFont(font)
        self.BuyingButton3.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background: rgb(0, 121, 0);\n"
"    border-radius: 15px;\n"
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
        self.BuyingButton3.setObjectName("BuyingButton3")
        self.ProductAmount3 = QtWidgets.QLabel(self.ProductFrame3)
        self.ProductAmount3.setGeometry(QtCore.QRect(20, 270, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.ProductAmount3.setFont(font)
        self.ProductAmount3.setStyleSheet("color: black;")
        self.ProductAmount3.setAlignment(QtCore.Qt.AlignCenter)
        self.ProductAmount3.setObjectName("ProductAmount3")
        self.ProductIncrease3 = QtWidgets.QPushButton(self.ProductFrame3)
        self.ProductIncrease3.setGeometry(QtCore.QRect(110, 270, 21, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.ProductIncrease3.setFont(font)
        self.ProductIncrease3.setStyleSheet("QPushButton {\n"
"    background: white;\n"
"}")
        self.ProductIncrease3.setObjectName("ProductIncrease3")
        self.ProductDecrease3 = QtWidgets.QPushButton(self.ProductFrame3)
        self.ProductDecrease3.setGeometry(QtCore.QRect(20, 270, 21, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.ProductDecrease3.setFont(font)
        self.ProductDecrease3.setStyleSheet("QPushButton {\n"
"    background: white;\n"
"}")
        self.ProductDecrease3.setObjectName("ProductDecrease3")
        self.TickMark3 = QtWidgets.QLabel(self.ProductFrame3)
        self.TickMark3.setGeometry(QtCore.QRect(10, 10, 21, 21))
        self.TickMark3.setStyleSheet("QLabel {\n"
"    image: url(:);\n"
"}")
        self.TickMark3.setText("")
        self.TickMark3.setObjectName("TickMark3")
        self.ProductFrame2 = QtWidgets.QFrame(self.centralwidget)
        self.ProductFrame2.setGeometry(QtCore.QRect(240, 210, 151, 361))
        self.ProductFrame2.setStyleSheet("QFrame {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: lightgray;\n"
"    border-radius: 30px;\n"
"}")
        self.ProductFrame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ProductFrame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ProductFrame2.setObjectName("ProductFrame2")
        self.ProductPicture2 = QtWidgets.QLabel(self.ProductFrame2)
        self.ProductPicture2.setGeometry(QtCore.QRect(10, 10, 131, 91))
        self.ProductPicture2.setStyleSheet("QLabel {\n"
"    image: url(:/)\n"
"}")
        self.ProductPicture2.setText("")
        self.ProductPicture2.setObjectName("ProductPicture2")
        self.ProductLabel2 = QtWidgets.QLabel(self.ProductFrame2)
        self.ProductLabel2.setGeometry(QtCore.QRect(10, 110, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.ProductLabel2.setFont(font)
        self.ProductLabel2.setText("")
        self.ProductLabel2.setObjectName("ProductLabel2")
        self.ProductDescription2 = QtWidgets.QTextBrowser(self.ProductFrame2)
        self.ProductDescription2.setGeometry(QtCore.QRect(10, 130, 131, 121))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(10)
        self.ProductDescription2.setFont(font)
        self.ProductDescription2.setStyleSheet("color: black;")
        self.ProductDescription2.setObjectName("ProductDescription2")
        self.BuyingButton2 = QtWidgets.QPushButton(self.ProductFrame2)
        self.BuyingButton2.setGeometry(QtCore.QRect(20, 310, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        font.setBold(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.BuyingButton2.setFont(font)
        self.BuyingButton2.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background: rgb(0, 121, 0);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #64AB25;\n"
"    background: #333;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"")
        self.BuyingButton2.setObjectName("BuyingButton2")
        self.ProductAmount2 = QtWidgets.QLabel(self.ProductFrame2)
        self.ProductAmount2.setGeometry(QtCore.QRect(20, 270, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.ProductAmount2.setFont(font)
        self.ProductAmount2.setStyleSheet("color: black;")
        self.ProductAmount2.setAlignment(QtCore.Qt.AlignCenter)
        self.ProductAmount2.setObjectName("ProductAmount2")
        self.ProductIncrease2 = QtWidgets.QPushButton(self.ProductFrame2)
        self.ProductIncrease2.setGeometry(QtCore.QRect(110, 270, 21, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.ProductIncrease2.setFont(font)
        self.ProductIncrease2.setStyleSheet("QPushButton {\n"
"    background: white;\n"
"}")
        self.ProductIncrease2.setObjectName("ProductIncrease2")
        self.ProductDecrease2 = QtWidgets.QPushButton(self.ProductFrame2)
        self.ProductDecrease2.setGeometry(QtCore.QRect(20, 270, 21, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.ProductDecrease2.setFont(font)
        self.ProductDecrease2.setStyleSheet("QPushButton {\n"
"    background: white;\n"
"}")
        self.ProductDecrease2.setObjectName("ProductDecrease2")
        self.TickMark2 = QtWidgets.QLabel(self.ProductFrame2)
        self.TickMark2.setGeometry(QtCore.QRect(10, 10, 21, 21))
        self.TickMark2.setStyleSheet("QLabel {\n"
"    image: url(:);\n"
"}")
        self.TickMark2.setText("")
        self.TickMark2.setObjectName("TickMark2")
        self.ProductFrame4 = QtWidgets.QFrame(self.centralwidget)
        self.ProductFrame4.setGeometry(QtCore.QRect(580, 210, 151, 361))
        self.ProductFrame4.setStyleSheet("QFrame {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: lightgray;\n"
"    border-radius: 30px;\n"
"}")
        self.ProductFrame4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ProductFrame4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ProductFrame4.setObjectName("ProductFrame4")
        self.ProductPicture4 = QtWidgets.QLabel(self.ProductFrame4)
        self.ProductPicture4.setGeometry(QtCore.QRect(10, 10, 131, 91))
        self.ProductPicture4.setStyleSheet("QLabel {\n"
"    image: url(:/)\n"
"}")
        self.ProductPicture4.setText("")
        self.ProductPicture4.setObjectName("ProductPicture4")
        self.ProductLabel4 = QtWidgets.QLabel(self.ProductFrame4)
        self.ProductLabel4.setGeometry(QtCore.QRect(10, 110, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.ProductLabel4.setFont(font)
        self.ProductLabel4.setText("")
        self.ProductLabel4.setObjectName("ProductLabel4")
        self.ProductDescription4 = QtWidgets.QTextBrowser(self.ProductFrame4)
        self.ProductDescription4.setGeometry(QtCore.QRect(10, 130, 131, 121))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(10)
        self.ProductDescription4.setFont(font)
        self.ProductDescription4.setStyleSheet("color: black;")
        self.ProductDescription4.setObjectName("ProductDescription4")
        self.BuyingButton4 = QtWidgets.QPushButton(self.ProductFrame4)
        self.BuyingButton4.setGeometry(QtCore.QRect(20, 310, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        font.setBold(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.BuyingButton4.setFont(font)
        self.BuyingButton4.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background: rgb(0, 121, 0);\n"
"    border-radius: 15px;\n"
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
        self.BuyingButton4.setObjectName("BuyingButton4")
        self.ProductAmount4 = QtWidgets.QLabel(self.ProductFrame4)
        self.ProductAmount4.setGeometry(QtCore.QRect(20, 270, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.ProductAmount4.setFont(font)
        self.ProductAmount4.setStyleSheet("color: black;")
        self.ProductAmount4.setAlignment(QtCore.Qt.AlignCenter)
        self.ProductAmount4.setObjectName("ProductAmount4")
        self.ProductIncrease4 = QtWidgets.QPushButton(self.ProductFrame4)
        self.ProductIncrease4.setGeometry(QtCore.QRect(110, 270, 21, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.ProductIncrease4.setFont(font)
        self.ProductIncrease4.setStyleSheet("QPushButton {\n"
"    background: white;\n"
"}")
        self.ProductIncrease4.setObjectName("ProductIncrease4")
        self.ProductDecrease4 = QtWidgets.QPushButton(self.ProductFrame4)
        self.ProductDecrease4.setGeometry(QtCore.QRect(20, 270, 21, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.ProductDecrease4.setFont(font)
        self.ProductDecrease4.setStyleSheet("QPushButton {\n"
"    background: white;\n"
"}")
        self.ProductDecrease4.setObjectName("ProductDecrease4")
        self.TickMark4 = QtWidgets.QLabel(self.ProductFrame4)
        self.TickMark4.setGeometry(QtCore.QRect(10, 10, 21, 21))
        self.TickMark4.setStyleSheet("QLabel {\n"
"    image: url(:);\n"
"}")
        self.TickMark4.setText("")
        self.TickMark4.setObjectName("TickMark4")
        self.ProductFrame5 = QtWidgets.QFrame(self.centralwidget)
        self.ProductFrame5.setGeometry(QtCore.QRect(750, 210, 151, 361))
        self.ProductFrame5.setStyleSheet("QFrame {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: lightgray;\n"
"    border-radius: 30px;\n"
"}")
        self.ProductFrame5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ProductFrame5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ProductFrame5.setObjectName("ProductFrame5")
        self.ProductPicture5 = QtWidgets.QLabel(self.ProductFrame5)
        self.ProductPicture5.setGeometry(QtCore.QRect(10, 10, 131, 91))
        self.ProductPicture5.setStyleSheet("QLabel {\n"
"    image: url(:/)\n"
"}")
        self.ProductPicture5.setText("")
        self.ProductPicture5.setObjectName("ProductPicture5")
        self.ProductLabel5 = QtWidgets.QLabel(self.ProductFrame5)
        self.ProductLabel5.setGeometry(QtCore.QRect(10, 110, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.ProductLabel5.setFont(font)
        self.ProductLabel5.setText("")
        self.ProductLabel5.setObjectName("ProductLabel5")
        self.ProductDescription5 = QtWidgets.QTextBrowser(self.ProductFrame5)
        self.ProductDescription5.setGeometry(QtCore.QRect(10, 130, 131, 121))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(10)
        self.ProductDescription5.setFont(font)
        self.ProductDescription5.setStyleSheet("color: black;")
        self.ProductDescription5.setObjectName("ProductDescription5")
        self.BuyingButton5 = QtWidgets.QPushButton(self.ProductFrame5)
        self.BuyingButton5.setGeometry(QtCore.QRect(20, 310, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        font.setBold(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.BuyingButton5.setFont(font)
        self.BuyingButton5.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background: rgb(0, 121, 0);\n"
"    border-radius: 15px;\n"
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
        self.BuyingButton5.setObjectName("BuyingButton5")
        self.ProductAmount5 = QtWidgets.QLabel(self.ProductFrame5)
        self.ProductAmount5.setGeometry(QtCore.QRect(20, 270, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.ProductAmount5.setFont(font)
        self.ProductAmount5.setStyleSheet("color: black;")
        self.ProductAmount5.setAlignment(QtCore.Qt.AlignCenter)
        self.ProductAmount5.setObjectName("ProductAmount5")
        self.ProductIncrease5 = QtWidgets.QPushButton(self.ProductFrame5)
        self.ProductIncrease5.setGeometry(QtCore.QRect(110, 270, 21, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.ProductIncrease5.setFont(font)
        self.ProductIncrease5.setStyleSheet("QPushButton {\n"
"    background: white;\n"
"}")
        self.ProductIncrease5.setObjectName("ProductIncrease5")
        self.ProductDecrease5 = QtWidgets.QPushButton(self.ProductFrame5)
        self.ProductDecrease5.setGeometry(QtCore.QRect(20, 270, 21, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.ProductDecrease5.setFont(font)
        self.ProductDecrease5.setStyleSheet("QPushButton {\n"
"    background: white;\n"
"}")
        self.ProductDecrease5.setObjectName("ProductDecrease5")
        self.TickMark5 = QtWidgets.QLabel(self.ProductFrame5)
        self.TickMark5.setGeometry(QtCore.QRect(10, 10, 21, 21))
        self.TickMark5.setStyleSheet("QLabel {\n"
"    image: url(:);\n"
"}")
        self.TickMark5.setText("")
        self.TickMark5.setObjectName("TickMark5")
        self.RightButton = QtWidgets.QPushButton(self.centralwidget)
        self.RightButton.setGeometry(QtCore.QRect(920, 370, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        font.setBold(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.RightButton.setFont(font)
        self.RightButton.setStyleSheet("QPushButton {\n"
"    background: lightgray;\n"
"    border-radius: 20px;\n"
"    image: url(:/others/Arrow/rightArrow.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: lightgreen;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.RightButton.setText("")
        self.RightButton.setObjectName("RightButton")
        self.LeftButton = QtWidgets.QPushButton(self.centralwidget)
        self.LeftButton.setGeometry(QtCore.QRect(10, 370, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        font.setBold(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.LeftButton.setFont(font)
        self.LeftButton.setStyleSheet("QPushButton {\n"
"    background: lightgray;\n"
"    border-radius: 20px;\n"
"    image: url(:/others/Arrow/leftArrow.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: lightgreen;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"\n"
"")
        self.LeftButton.setText("")
        self.LeftButton.setObjectName("LeftButton")
        self.BrandLabel = QtWidgets.QLabel(self.centralwidget)
        self.BrandLabel.setGeometry(QtCore.QRect(380, 10, 281, 101))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(50)
        font.setBold(True)
        font.setItalic(False)
        self.BrandLabel.setFont(font)
        self.BrandLabel.setStyleSheet("QLabel {\n"
"    color: rgb(245, 245, 245);\n"
" background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.BrandLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BrandLabel.setObjectName("BrandLabel")
        self.CartButton = QtWidgets.QPushButton(self.centralwidget)
        self.CartButton.setGeometry(QtCore.QRect(850, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.CartButton.setFont(font)
        self.CartButton.setStyleSheet("QPushButton {\n"
"    font: 700 10pt \"Sitka\";\n"
"    color: black;\n"
"    background:  rgb(245, 245, 245);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: black;\n"
"    background: lightblue;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"")
        self.CartButton.setObjectName("CartButton")
        self.RefreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.RefreshButton.setGeometry(QtCore.QRect(850, 60, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.RefreshButton.setFont(font)
        self.RefreshButton.setStyleSheet("QPushButton {\n"
" font: 700 10pt \"Sitka\";\n"
"    color: black;\n"
"    background:  rgb(245, 245, 245);\n"
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
        self.RefreshButton.setObjectName("RefreshButton")
        self.SellProductButton = QtWidgets.QPushButton(self.centralwidget)
        self.SellProductButton.setGeometry(QtCore.QRect(30, 30, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.SellProductButton.setFont(font)
        self.SellProductButton.setStyleSheet("QPushButton {\n"
"    font: 700 9pt \"Sitka\";\n"
"    color: black;\n"
"    background:  rgb(245, 245, 245);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: black;\n"
"    background: lightblue;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"")
        self.SellProductButton.setObjectName("SellProductButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1021, 671))
        self.label_2.setStyleSheet("background-image: url(:/serch_pic/josefin-HtCgLIDy-2U-unsplash.jpg);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/Bg/Background.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(-10, 160, 1001, 541))
        self.textBrowser.setStyleSheet("QFrame {\n"
"    \n"
"    background-color: #FAFAFA;\n"
"    border-radius: 50px;\n"
"}")
        self.textBrowser.setObjectName("textBrowser")
        self.PageLabel = QtWidgets.QLabel(self.centralwidget)
        self.PageLabel.setGeometry(QtCore.QRect(430, 590, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.PageLabel.setFont(font)
        self.PageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PageLabel.setObjectName("PageLabel")
        self.Label = QtWidgets.QLabel(self.centralwidget)
        self.Label.setGeometry(QtCore.QRect(80, 120, 811, 20))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.Label.setFont(font)
        self.Label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Label.setObjectName("Label")
        self.label_2.raise_()
        self.textBrowser.raise_()
        self.ProductFrame1.raise_()
        self.ProductFrame3.raise_()
        self.ProductFrame2.raise_()
        self.ProductFrame4.raise_()
        self.ProductFrame5.raise_()
        self.RightButton.raise_()
        self.LeftButton.raise_()
        self.BrandLabel.raise_()
        self.CartButton.raise_()
        self.RefreshButton.raise_()
        self.SellProductButton.raise_()
        self.PageLabel.raise_()
        self.Label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ProductDescription1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Franklin Gothic Medium Cond\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.BuyingButton1.setText(_translate("MainWindow", "0 Bath"))
        self.ProductAmount1.setText(_translate("MainWindow", "Buy: 1"))
        self.ProductIncrease1.setText(_translate("MainWindow", "+"))
        self.ProductDecrease1.setText(_translate("MainWindow", "-"))
        self.ProductDescription3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Franklin Gothic Medium Cond\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.BuyingButton3.setText(_translate("MainWindow", "0 Bath"))
        self.ProductAmount3.setText(_translate("MainWindow", "Buy: 1"))
        self.ProductIncrease3.setText(_translate("MainWindow", "+"))
        self.ProductDecrease3.setText(_translate("MainWindow", "-"))
        self.ProductDescription2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Franklin Gothic Medium Cond\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.BuyingButton2.setText(_translate("MainWindow", "0 Bath"))
        self.ProductAmount2.setText(_translate("MainWindow", "Buy: 1"))
        self.ProductIncrease2.setText(_translate("MainWindow", "+"))
        self.ProductDecrease2.setText(_translate("MainWindow", "-"))
        self.ProductDescription4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Franklin Gothic Medium Cond\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.BuyingButton4.setText(_translate("MainWindow", "0 Bath"))
        self.ProductAmount4.setText(_translate("MainWindow", "Buy: 1"))
        self.ProductIncrease4.setText(_translate("MainWindow", "+"))
        self.ProductDecrease4.setText(_translate("MainWindow", "-"))
        self.ProductDescription5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Franklin Gothic Medium Cond\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.BuyingButton5.setText(_translate("MainWindow", "0 Bath"))
        self.ProductAmount5.setText(_translate("MainWindow", "Buy: 1"))
        self.ProductIncrease5.setText(_translate("MainWindow", "+"))
        self.ProductDecrease5.setText(_translate("MainWindow", "-"))
        self.BrandLabel.setText(_translate("MainWindow", "Fresh"))
        self.CartButton.setText(_translate("MainWindow", "View Cart"))
        self.RefreshButton.setText(_translate("MainWindow", "Refresh"))
        self.SellProductButton.setText(_translate("MainWindow", "Sell Product"))
        self.PageLabel.setText(_translate("MainWindow", "Page: 0/0"))
        self.Label.setText(_translate("MainWindow", "Welcome to Fresh! We only have fresh stuff here. All the items are organic & natural."))
import Bg_rc
import pic_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
