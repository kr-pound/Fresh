from PyQt5 import QtCore, QtGui, QtWidgets
from _sell_product_design import Ui_MainWindow as Ui_SellProductWindow
from __database import database

from os import environ

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

class SellProductWindow(QtWidgets.QMainWindow, Ui_SellProductWindow):
    confirm_add_product = QtCore.pyqtSignal()

    name = None
    price = 0
    detail = None
    category = None
    amount = 0

    #db = database

    def __init__(self, parent=None):
        #super the class to setup the Ui
        super(SellProductWindow, self).__init__(parent)
        self.setupUi(self)

        #Transfer to Search page
        self.ConfirmButton.clicked.connect(self.receiveData)

    @QtCore.pyqtSlot()
    def confirmAddProductTransfer(self):
        print("Successfully added data")
        print("The product store will be update on the next time runs\n")

        self.confirm_add_product.emit()
        self.close()

    def receiveData(self):
        self.name = self.NameLineEdit.text()
        self.price = self.PriceLineEdit.text()
        self.detail = self.DetailTextEdit.toPlainText()

        self.veg = self.VegetableCategory.isChecked()
        self.fruit = self.FruitCategory.isChecked()
        self.daily_product = self.DailyProductCategory.isChecked()
        self.otop = self.OTOPCategory.isChecked()

        self.clear_lineEdit()

        if (self.price == '') or (self.price.isnumeric() == False):
            print("Wrong Input")
        else:
            self.price = int(self.price)

            self.submitData()
            self.confirmAddProductTransfer()

    #clear line edit after push button
    def clear_lineEdit(self):
        cleared_text = ""

        self.NameLineEdit.setText(cleared_text)
        self.PriceLineEdit.setText(cleared_text)
        self.DetailTextEdit.setPlainText(cleared_text)

    #send data to __database.py
    def submitData(self):
        database.product_name = self.name
        database.product_price = self.price
        database.product_detail = self.detail

        database.product_veg = self.veg
        database.product_fruit = self.fruit
        database.product_daily_product = self.daily_product
        database.product_otop = self.otop

        database.push_product(database)
        

        
