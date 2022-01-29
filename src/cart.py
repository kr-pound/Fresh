from PyQt5 import QtCore, QtGui, QtWidgets
from _cart_design import Ui_MainWindow as Ui_CartWindow
from __product import CartProductClass

from os import environ

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

class CartWindow(QtWidgets.QMainWindow, Ui_CartWindow):
    search = QtCore.pyqtSignal()
    checkout = QtCore.pyqtSignal()

    #list of product object in the cart
    buy_list = [None] * 6
    page = 1

    cpClass = CartProductClass

    def __init__(self, parent=None):
        #super the class to setup the Ui
        super(CartWindow, self).__init__(parent)
        self.setupUi(self)
        #after push the button --> go back
        self.BackButton.clicked.connect(self.searchTransfer)
        self.pushButton_2.clicked.connect(self.checkoutTransfer)

        #cart load button
        self.ReloadButton.clicked.connect(self.reload)

        #change cart page
        self.LeftButton.clicked.connect(self.leftTransfer)
        self.RightButton.clicked.connect(self.rightTransfer)

        #delete button
        self.DeleteButton1.clicked.connect(self.delete_index0)
        self.DeleteButton2.clicked.connect(self.delete_index1)
        self.DeleteButton3.clicked.connect(self.delete_index2)
        self.DeleteButton4.clicked.connect(self.delete_index3)
        self.DeleteButton5.clicked.connect(self.delete_index4)
        self.DeleteButton6.clicked.connect(self.delete_index5)

        self.clear_cart_label()

        #set style sheet of price label
        self.CartProductPrice1.setStyleSheet("color: darkblue;")
        self.CartProductPrice2.setStyleSheet("color: darkblue;")
        self.CartProductPrice3.setStyleSheet("color: darkblue;")
        self.CartProductPrice4.setStyleSheet("color: darkblue;")
        self.CartProductPrice5.setStyleSheet("color: darkblue;")
        self.CartProductPrice6.setStyleSheet("color: darkblue;")

    
    @QtCore.pyqtSlot()
    def searchTransfer(self):
        #clear cart
        self.clear_cart_label()
        self.page = 1

        self.search.emit()
        self.close()

    @QtCore.pyqtSlot()
    def checkoutTransfer(self):
        self.checkout.emit()


    def reload(self):
        self.clear_cart_label()

        buy_count = 0
        self.cpClass.buy_list = [None] * 6

        for product in self.cpClass.product:
            #add more cart space
            if (product != None):

                if (product.buy_amount > 0):
                    if (self.cpClass.buy_list[-1] != None):
                        self.cpClass.buy_list += [None] * 6

                    #put product object into buy_list
                    self.cpClass.buy_list[buy_count] = product
                    buy_count += 1
            else:
                break

        #label note in CartWindow
        print("Cart Data: ", end="")
        print(self.cpClass.buy_list)

        self.label_product_cart_detail()
    
    #cart data label
    def label_product_cart_detail(self):
        while(len(self.cpClass.buy_list) // 6 < self.page):
            self.page -= 1

        page_index = self.page - 1
        delete_text = "Delete"

        total_price = 0

        if (self.cpClass.buy_list[0 + page_index * 6] != None):
            self.CartProductLabel1.setText(self.cpClass.buy_list[0 + page_index * 6].name)
            self.CartProductAmount1.setText("Buy: " + str(self.cpClass.buy_list[0 + page_index * 6].buy_amount))
            self.CartProductPrice1.setText("Price: " + str(self.cpClass.buy_list[0 + page_index * 6].price *
                                            self.cpClass.buy_list[0 + page_index * 6].buy_amount))
            self.DeleteButton1.setText(delete_text)
            self.CartProductPicture1.setStyleSheet("image: url(:/icon/Icon/" + self.cpClass.buy_list[0 + page_index * 6].picture + ");")
        if (self.cpClass.buy_list[1 + page_index * 6] != None):
            self.CartProductLabel2.setText(self.cpClass.buy_list[1 + page_index * 6].name)
            self.CartProductAmount2.setText("Buy: " + str(self.cpClass.buy_list[1 + page_index * 6].buy_amount))
            self.CartProductPrice2.setText("Price: " + str(self.cpClass.buy_list[1 + page_index * 6].price *
                                            self.cpClass.buy_list[1 + page_index * 6].buy_amount))
            self.DeleteButton2.setText(delete_text)
            self.CartProductPicture2.setStyleSheet("image: url(:/icon/Icon/" + self.cpClass.buy_list[1 + page_index * 6].picture + ");")
        if (self.cpClass.buy_list[2 + page_index * 6] != None):
            self.CartProductLabel3.setText(self.cpClass.buy_list[2 + page_index * 6].name)
            self.CartProductAmount3.setText("Buy: " + str(self.cpClass.buy_list[2 + page_index * 6].buy_amount))
            self.CartProductPrice3.setText("Price: " + str(self.cpClass.buy_list[2 + page_index * 6].price *
                                            self.cpClass.buy_list[2 + page_index * 6].buy_amount))
            self.DeleteButton3.setText(delete_text)
            self.CartProductPicture3.setStyleSheet("image: url(:/icon/Icon/" + self.cpClass.buy_list[2 + page_index * 6].picture + ");")
        if (self.cpClass.buy_list[3 + page_index * 6] != None):
            self.CartProductLabel4.setText(self.cpClass.buy_list[3 + page_index * 6].name)
            self.CartProductAmount4.setText("Buy: " + str(self.cpClass.buy_list[3 + page_index * 6].buy_amount))
            self.CartProductPrice4.setText("Price: " + str(self.cpClass.buy_list[3 + page_index * 6].price *
                                            self.cpClass.buy_list[3 + page_index * 6].buy_amount))
            self.DeleteButton4.setText(delete_text)
            self.CartProductPicture4.setStyleSheet("image: url(:/icon/Icon/" + self.cpClass.buy_list[3 + page_index * 6].picture + ");")
        if (self.cpClass.buy_list[4 + page_index * 6] != None):
            self.CartProductLabel5.setText(self.cpClass.buy_list[4 + page_index * 6].name)
            self.CartProductAmount5.setText("Buy: " + str(self.cpClass.buy_list[4 + page_index * 6].buy_amount))
            self.CartProductPrice5.setText("Price: " + str(self.cpClass.buy_list[4 + page_index * 6].price *
                                            self.cpClass.buy_list[4 + page_index * 6].buy_amount))
            self.DeleteButton5.setText(delete_text)
            self.CartProductPicture5.setStyleSheet("image: url(:/icon/Icon/" + self.cpClass.buy_list[4 + page_index * 6].picture + ");")
        if (self.cpClass.buy_list[5 + page_index * 6] != None):
            self.CartProductLabel6.setText(self.cpClass.buy_list[5 + page_index * 6].name)
            self.CartProductAmount6.setText("Buy: " + str(self.cpClass.buy_list[5 + page_index * 6].buy_amount))
            self.CartProductPrice6.setText("Price: " + str(self.cpClass.buy_list[5 + page_index * 6].price *
                                            self.cpClass.buy_list[5 + page_index * 6].buy_amount))
            self.DeleteButton6.setText(delete_text)
            self.CartProductPicture6.setStyleSheet("image: url(:/icon/Icon/" + self.cpClass.buy_list[5 + page_index * 6].picture + ");")

        page_index = 0
        #calculate each price and sum together
        while(1):
            if(len(self.cpClass.buy_list) // 6 < page_index + 1):
                break

            if (self.cpClass.buy_list[0 + page_index * 6] != None):
                total_price += (self.cpClass.buy_list[0 + page_index * 6].price * self.cpClass.buy_list[0 + page_index * 6].buy_amount)
            if (self.cpClass.buy_list[1 + page_index * 6] != None):
                total_price += (self.cpClass.buy_list[1 + page_index * 6].price * self.cpClass.buy_list[1 + page_index * 6].buy_amount)
            if (self.cpClass.buy_list[2 + page_index * 6] != None):
                total_price += (self.cpClass.buy_list[2 + page_index * 6].price * self.cpClass.buy_list[2 + page_index * 6].buy_amount)
            if (self.cpClass.buy_list[3 + page_index * 6] != None):
                total_price += (self.cpClass.buy_list[3 + page_index * 6].price * self.cpClass.buy_list[3 + page_index * 6].buy_amount)
            if (self.cpClass.buy_list[4 + page_index * 6] != None):
                total_price += (self.cpClass.buy_list[4 + page_index * 6].price * self.cpClass.buy_list[4 + page_index * 6].buy_amount)
            if (self.cpClass.buy_list[5 + page_index * 6] != None):
                total_price += (self.cpClass.buy_list[5 + page_index * 6].price * self.cpClass.buy_list[5 + page_index * 6].buy_amount)

            else:
                break

            page_index += 1

        #set other label texts
        self.TotalLabel.setText("Total: " + str(total_price))
        self.cpClass.total_price = total_price

        self.PageLabel.setText("Page: " + str(self.page) + "/" + str(len(self.cpClass.buy_list)//6))


    def clear_cart_label(self):
        cleared_label = ""
        cleared_amount = ""
        cleared_price = ""
        cleared_button = ""
        cleared_picture = ""

        self.CartProductLabel1.setText(cleared_label)
        self.CartProductLabel2.setText(cleared_label)
        self.CartProductLabel3.setText(cleared_label)
        self.CartProductLabel4.setText(cleared_label)
        self.CartProductLabel5.setText(cleared_label)
        self.CartProductLabel6.setText(cleared_label)

        self.CartProductAmount1.setText(cleared_amount)
        self.CartProductAmount2.setText(cleared_amount)
        self.CartProductAmount3.setText(cleared_amount)
        self.CartProductAmount4.setText(cleared_amount)
        self.CartProductAmount5.setText(cleared_amount)
        self.CartProductAmount6.setText(cleared_amount)

        self.CartProductPrice1.setText(cleared_price)
        self.CartProductPrice2.setText(cleared_price)
        self.CartProductPrice3.setText(cleared_price)
        self.CartProductPrice4.setText(cleared_price)
        self.CartProductPrice5.setText(cleared_price)
        self.CartProductPrice6.setText(cleared_price)

        self.DeleteButton1.setText(cleared_button)
        self.DeleteButton2.setText(cleared_button)
        self.DeleteButton3.setText(cleared_button)
        self.DeleteButton4.setText(cleared_button)
        self.DeleteButton5.setText(cleared_button)
        self.DeleteButton6.setText(cleared_button)

        self.CartProductPicture1.setStyleSheet(cleared_picture)
        self.CartProductPicture2.setStyleSheet(cleared_picture)
        self.CartProductPicture3.setStyleSheet(cleared_picture)
        self.CartProductPicture4.setStyleSheet(cleared_picture)
        self.CartProductPicture5.setStyleSheet(cleared_picture)
        self.CartProductPicture6.setStyleSheet(cleared_picture)

        self.TotalLabel.setText("")
        self.PageLabel.setText("Page: 1/1")

    #change the page of product show
    def rightTransfer(self):
        if (self.page * 6 < len(self.cpClass.buy_list)):
            self.page += 1

            #reset product info
            self.reload()
    
    def leftTransfer(self):
        if (self.page > 1):
            self.page -= 1

            #reset product info
            self.reload()

    #delete function
    def delete_index0(self):
        self.cart_index = ((self.page - 1) * 6) + 0
        if (self.cart_index < len(self.cpClass.buy_list)) and (self.cpClass.buy_list[self.cart_index] != None):
            self.cpClass.buy_list[self.cart_index].buy_amount = 0
        self.reload()
    def delete_index1(self):
        self.cart_index = ((self.page - 1) * 6) + 1
        if (self.cart_index < len(self.cpClass.buy_list)) and (self.cpClass.buy_list[self.cart_index] != None):
            self.cpClass.buy_list[self.cart_index].buy_amount = 0
        self.reload()
    def delete_index2(self):
        self.cart_index = ((self.page - 1) * 6) + 2
        if (self.cart_index < len(self.cpClass.buy_list)) and (self.cpClass.buy_list[self.cart_index] != None):
            self.cpClass.buy_list[self.cart_index].buy_amount = 0
        self.reload()
    def delete_index3(self):
        self.cart_index = ((self.page - 1) * 6) + 3
        if (self.cart_index < len(self.cpClass.buy_list)) and (self.cpClass.buy_list[self.cart_index] != None):
            self.cpClass.buy_list[self.cart_index].buy_amount = 0
        self.reload()
    def delete_index4(self):
        self.cart_index = ((self.page - 1) * 6) + 4
        if (self.cart_index < len(self.cpClass.buy_list)) and (self.cpClass.buy_list[self.cart_index] != None):
            self.cpClass.buy_list[self.cart_index].buy_amount = 0
        self.reload()
    def delete_index5(self):
        self.cart_index = ((self.page - 1) * 6) + 5
        if (self.cart_index < len(self.cpClass.buy_list)) and (self.cpClass.buy_list[self.cart_index] != None):
            self.cpClass.buy_list[self.cart_index].buy_amount = 0
        self.reload()

        


