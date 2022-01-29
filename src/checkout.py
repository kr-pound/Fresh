from PyQt5 import QtCore, QtGui, QtWidgets
from _checkout_design import Ui_MainWindow as Ui_CheckoutWindow
from __product import CartProductClass

from os import environ

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

class CheckoutWindow(QtWidgets.QMainWindow, Ui_CheckoutWindow):
    cart = QtCore.pyqtSignal()

    cpClass = CartProductClass

    def __init__(self, parent=None):
        #super the class to setup the Ui
        super(CheckoutWindow, self).__init__(parent)
        self.setupUi(self)
        #after push the button --> close and print a bill
        self.CloseButton.clicked.connect(self.cartTransfer)
        self.BillButton.clicked.connect(self.billPrint)

    #close window and printing
    @QtCore.pyqtSlot()
    def cartTransfer(self):
        self.PriceLabel.setText("")

        self.cart.emit()
        self.close()

    def billPrint(self):
        self.PriceLabel.setText(str(self.cpClass.total_price))
        print("\n<<< Printing Bill >>>")

        #printing
        i = 0

        while(self.cpClass.buy_list[i] != None):
            print(self.cpClass.buy_list[i].name + "\t amount: " + str(self.cpClass.buy_list[i].buy_amount) +
                "\t price: " + str(self.cpClass.buy_list[i].price * self.cpClass.buy_list[i].buy_amount) + " Baht")
            self.cpClass.buy_list[i].status = "yes"
            i += 1

        print("\nTotal Price: " + str(self.cpClass.total_price) + " Baht\n")
        
        '''
        #set sold status to "yes"
        for i in range(len(self.cpClass.buy_list)):
            if (self.cpClass.buy_list[i] != None):
                self.cpClass.buy_list[i].status = "yes"
        self.cpClass.update_status(CartProductClass)'''

        