from PyQt5 import QtCore, QtGui, QtWidgets
from _search_design import Ui_MainWindow as Ui_SearchWindow
from __product import CartProductClass

from os import environ

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

class SearchWindow(QtWidgets.QMainWindow, Ui_SearchWindow):
    cart = QtCore.pyqtSignal()
    sell_product = QtCore.pyqtSignal()

    page = 1
    #the buying of product id
    buy_index = None

    cpClass = CartProductClass()

    #buy amount show in product search
    buy_amount0 = 0
    buy_amount1 = 0
    buy_amount2 = 0
    buy_amount3 = 0
    buy_amount4 = 0
    
    def __init__(self, parent=None):
        #super the class to setup the Ui
        super(SearchWindow, self).__init__(parent)
        self.setupUi(self)

        #after push the button --> view cart or sell product page
        self.CartButton.clicked.connect(self.cartTransfer)
        self.SellProductButton.clicked.connect(self.sellProductTransfer)

        #set page label
        self.PageLabel.setText("Page: 0/0")
        
        #product label color
        self.ProductLabel1.setStyleSheet("color: darkgreen;")
        self.ProductLabel2.setStyleSheet("color: darkgreen;")
        self.ProductLabel3.setStyleSheet("color: darkgreen;")
        self.ProductLabel4.setStyleSheet("color: darkgreen;")
        self.ProductLabel5.setStyleSheet("color: darkgreen;")

        #change pages to show product info
        self.RightButton.clicked.connect(self.rightTransfer)
        self.LeftButton.clicked.connect(self.leftTransfer)

        #increment button
        self.ProductIncrease1.clicked.connect(self.increment0)
        self.ProductIncrease2.clicked.connect(self.increment1)
        self.ProductIncrease3.clicked.connect(self.increment2)
        self.ProductIncrease4.clicked.connect(self.increment3)
        self.ProductIncrease5.clicked.connect(self.increment4)

        #decrement button
        self.ProductDecrease1.clicked.connect(self.decrement0)
        self.ProductDecrease2.clicked.connect(self.decrement1)
        self.ProductDecrease3.clicked.connect(self.decrement2)
        self.ProductDecrease4.clicked.connect(self.decrement3)
        self.ProductDecrease5.clicked.connect(self.decrement4)

        #buying button push --> send object to buy method
        self.BuyingButton1.clicked.connect(self.buy_index0)
        self.BuyingButton2.clicked.connect(self.buy_index1)
        self.BuyingButton3.clicked.connect(self.buy_index2)
        self.BuyingButton4.clicked.connect(self.buy_index3)
        self.BuyingButton5.clicked.connect(self.buy_index4)

        #insert product info
        self.RefreshButton.clicked.connect(self.refreshData)

        self.cpClass.label_product_detail(1, 5, self.cpClass.product)
        self.set_product_detail()

    @QtCore.pyqtSlot()
    def cartTransfer(self):
        #set and re-label amount to the same as object product
        self.set_buy_amount()
        self.amount_label0()
        self.amount_label1()
        self.amount_label2()
        self.amount_label3()
        self.amount_label4()

        self.cart.emit()
        self.close()

    @QtCore.pyqtSlot()
    def sellProductTransfer(self):
        #set and re-label amount to the same as object product
        self.set_buy_amount()
        self.amount_label0()
        self.amount_label1()
        self.amount_label2()
        self.amount_label3()
        self.amount_label4()

        self.sell_product.emit()

    def refreshData(self):
        #set the data from database
        self.cpClass.label_product_detail(1, 5, self.cpClass.product)
        self.set_product_detail()
        self.page = 1
        self.PageLabel.setText("Page: " + str(self.page) + "/" + str(len(self.cpClass.product)//5))

    def refreshTickMark(self):
        self.cpClass.label_product_detail(self.page, 5, self.cpClass.product)
        self.set_product_detail()

    #change the page of product show
    def rightTransfer(self):
        if (self.page * 5 < len(self.cpClass.product_list)):
            self.page += 1

            #reset product info
            self.cpClass.clear_label_product_detail()
            self.set_product_detail()
            self.cpClass.label_product_detail(self.page, 5, self.cpClass.product)
            self.set_product_detail()

            self.set_buy_amount()
    
    def leftTransfer(self):
        if (self.page > 1):
            self.page -= 1

            #reset product info
            self.cpClass.clear_label_product_detail()
            self.set_product_detail()
            self.cpClass.label_product_detail(self.page, 5, self.cpClass.product)
            self.set_product_detail()

            self.set_buy_amount()

    #generated buy id & set buy_amount in each product object
    def buy_index0(self):
        self.buy_index = ((self.page - 1) * 5) + 0
        if (self.buy_index < len(self.cpClass.product_list)):
            if(self.ProductAmount1.text() != ""):
                self.cpClass.product[self.buy_index].buy_amount = int(self.ProductAmount1.text().split()[-1])
            print("<<< Updated: " + self.cpClass.product[self.buy_index].name + " >>>" +
                "\tBuy Amount: " + str(self.cpClass.product[self.buy_index].buy_amount))
        self.refreshTickMark()
    def buy_index1(self):
        self.buy_index = ((self.page - 1) * 5) + 1
        if (self.buy_index < len(self.cpClass.product_list)):
            if(self.ProductAmount2.text() != ""):
                self.cpClass.product[self.buy_index].buy_amount = int(self.ProductAmount2.text().split()[-1])
            print("<<< Updated: " + self.cpClass.product[self.buy_index].name + " >>>" +
                "\tBuy Amount: " + str(self.cpClass.product[self.buy_index].buy_amount))
        self.refreshTickMark()
    def buy_index2(self):
        self.buy_index = ((self.page - 1) * 5) + 2
        if (self.buy_index < len(self.cpClass.product_list)):
            if(self.ProductAmount3.text() != ""):
                self.cpClass.product[self.buy_index].buy_amount = int(self.ProductAmount3.text().split()[-1])
            print("<<< Updated: " + self.cpClass.product[self.buy_index].name + " >>>" +
                "\tBuy Amount: " + str(self.cpClass.product[self.buy_index].buy_amount))
        self.refreshTickMark()
    def buy_index3(self):
        self.buy_index = ((self.page - 1) * 5) + 3
        if (self.buy_index < len(self.cpClass.product_list)):
            if(self.ProductAmount4.text() != ""):
                self.cpClass.product[self.buy_index].buy_amount = int(self.ProductAmount4.text().split()[-1])
            print("<<< Updated: " + self.cpClass.product[self.buy_index].name + " >>>" +
                "\tBuy Amount: " + str(self.cpClass.product[self.buy_index].buy_amount))
        self.refreshTickMark()
    def buy_index4(self):
        self.buy_index = ((self.page - 1) * 5) + 4
        if (self.buy_index < len(self.cpClass.product_list)):
            if(self.ProductAmount5.text() != ""):
                self.cpClass.product[self.buy_index].buy_amount = int(self.ProductAmount5.text().split()[-1])
            print("<<< Updated: " + self.cpClass.product[self.buy_index].name + " >>>" +
                "\tBuy Amount: " + str(self.cpClass.product[self.buy_index].buy_amount))
        self.refreshTickMark()


    #label product amount
    def amount_label0(self):
        self.buy_index = ((self.page - 1) * 5) + 0
        if (self.buy_index < len(self.cpClass.product_list)):
            self.ProductAmount1.setText("Buy: " + str(self.buy_amount0))
    def amount_label1(self):
        self.buy_index = ((self.page - 1) * 5) + 1
        if (self.buy_index < len(self.cpClass.product_list)):
            self.ProductAmount2.setText("Buy: " + str(self.buy_amount1))
    def amount_label2(self):
        self.buy_index = ((self.page - 1) * 5) + 2
        if (self.buy_index < len(self.cpClass.product_list)):
            self.ProductAmount3.setText("Buy: " + str(self.buy_amount2))
    def amount_label3(self):
        self.buy_index = ((self.page - 1) * 5) + 3
        if (self.buy_index < len(self.cpClass.product_list)):
            self.ProductAmount4.setText("Buy: " + str(self.buy_amount3))
    def amount_label4(self):
        self.buy_index = ((self.page - 1) * 5) + 4
        if (self.buy_index < len(self.cpClass.product_list)):
            self.ProductAmount5.setText("Buy: " + str(self.buy_amount4))


    #increment button
    def increment0(self):
        self.buy_index = ((self.page - 1) * 5) + 0
        if (self.buy_index < len(self.cpClass.product_list)):
            self.buy_amount0 += 1
            self.amount_label0()
    def increment1(self):
        self.buy_index = ((self.page - 1) * 5) + 1
        if (self.buy_index < len(self.cpClass.product_list)):
            self.buy_amount1 += 1
            self.amount_label1()
    def increment2(self):
        self.buy_index = ((self.page - 1) * 5) + 2
        if (self.buy_index < len(self.cpClass.product_list)):
            self.buy_amount2 += 1
            self.amount_label2()
    def increment3(self):
        self.buy_index = ((self.page - 1) * 5) + 3
        if (self.buy_index < len(self.cpClass.product_list)):
            self.buy_amount3 += 1
            self.amount_label3()
    def increment4(self):
        self.buy_index = ((self.page - 1) * 5) + 4
        if (self.buy_index < len(self.cpClass.product_list)):
            self.buy_amount4 += 1
            self.amount_label4()

    #decrement button
    def decrement0(self):
        self.buy_index = ((self.page - 1) * 5) + 0
        if (self.buy_index < len(self.cpClass.product_list)) and (self.buy_amount0 > 0):
            self.buy_amount0 -= 1
            self.amount_label0()
    def decrement1(self):
        self.buy_index = ((self.page - 1) * 5) + 1
        if (self.buy_index < len(self.cpClass.product_list)) and (self.buy_amount1 > 0):
            self.buy_amount1 -= 1
            self.amount_label1()
    def decrement2(self):
        self.buy_index = ((self.page - 1) * 5) + 2
        if (self.buy_index < len(self.cpClass.product_list)) and (self.buy_amount2 > 0):
            self.buy_amount2 -= 1
            self.amount_label2()
    def decrement3(self):
        self.buy_index = ((self.page - 1) * 5) + 3
        if (self.buy_index < len(self.cpClass.product_list)) and (self.buy_amount3 > 0):
            self.buy_amount3 -= 1
            self.amount_label3()
    def decrement4(self):
        self.buy_index = ((self.page - 1) * 5) + 4
        if (self.buy_index < len(self.cpClass.product_list)) and (self.buy_amount4 > 0):
            self.buy_amount4 -= 1
            self.amount_label4()

    #set buy_amount to the same as object value of that product
    def set_buy_amount(self):
        if (self.cpClass.product[((self.page - 1) * 5) + 0] != None):
            self.buy_amount0 = self.cpClass.product[((self.page - 1) * 5) + 0].buy_amount
        if (self.cpClass.product[((self.page - 1) * 5) + 1] != None):
            self.buy_amount1 = self.cpClass.product[((self.page - 1) * 5) + 1].buy_amount
        if (self.cpClass.product[((self.page - 1) * 5) + 2] != None):
            self.buy_amount2 = self.cpClass.product[((self.page - 1) * 5) + 2].buy_amount
        if (self.cpClass.product[((self.page - 1) * 5) + 3] != None):
            self.buy_amount3 = self.cpClass.product[((self.page - 1) * 5) + 3].buy_amount
        if (self.cpClass.product[((self.page - 1) * 5) + 4] != None):
            self.buy_amount4 = self.cpClass.product[((self.page - 1) * 5) + 4].buy_amount

    #label product information
    def set_product_detail(self):
        self.ProductLabel1.setText(self.cpClass.productLabel1)
        self.BuyingButton1.setText(self.cpClass.buyingButton1)
        self.ProductDescription1.setText(self.cpClass.productDescription1)
        self.ProductAmount1.setText(self.cpClass.productAmount1)
        self.ProductPicture1.setStyleSheet("image: url(:/icon/Icon/" + self.cpClass.productPicture1 + ");")
        self.TickMark1.setStyleSheet("image: url(:/icon/Icon/" + self.cpClass.productTick1 + ");")

        self.ProductLabel2.setText(self.cpClass.productLabel2)
        self.BuyingButton2.setText(self.cpClass.buyingButton2)
        self.ProductDescription2.setText(self.cpClass.productDescription2)
        self.ProductAmount2.setText(self.cpClass.productAmount2)
        self.ProductPicture2.setStyleSheet(self.cpClass.productPicture2)
        self.ProductPicture2.setStyleSheet("image: url(:/icon/Icon/" + self.cpClass.productPicture2 + ");")
        self.TickMark2.setStyleSheet("image: url(:/icon/Icon/" + self.cpClass.productTick2 + ");")

        self.ProductLabel3.setText(self.cpClass.productLabel3)
        self.BuyingButton3.setText(self.cpClass.buyingButton3)
        self.ProductDescription3.setText(self.cpClass.productDescription3)
        self.ProductAmount3.setText(self.cpClass.productAmount3)
        self.ProductPicture3.setStyleSheet(self.cpClass.productPicture3)
        self.ProductPicture3.setStyleSheet("image: url(:/icon/Icon/" + self.cpClass.productPicture3 + ");")
        self.TickMark3.setStyleSheet("image: url(:/icon/Icon/" + self.cpClass.productTick3 + ");")

        self.ProductLabel4.setText(self.cpClass.productLabel4)
        self.BuyingButton4.setText(self.cpClass.buyingButton4)
        self.ProductDescription4.setText(self.cpClass.productDescription4)
        self.ProductAmount4.setText(self.cpClass.productAmount4)
        self.ProductPicture4.setStyleSheet(self.cpClass.productPicture4)
        self.ProductPicture4.setStyleSheet("image: url(:/icon/Icon/" + self.cpClass.productPicture4 + ");")
        self.TickMark4.setStyleSheet("image: url(:/icon/Icon/" + self.cpClass.productTick4 + ");")

        self.ProductLabel5.setText(self.cpClass.productLabel5)
        self.BuyingButton5.setText(self.cpClass.buyingButton5)
        self.ProductDescription5.setText(self.cpClass.productDescription5)
        self.ProductAmount5.setText(self.cpClass.productAmount5)
        self.ProductPicture5.setStyleSheet(self.cpClass.productPicture5)
        self.ProductPicture5.setStyleSheet("image: url(:/icon/Icon/" + self.cpClass.productPicture5 + ");")
        self.TickMark5.setStyleSheet("image: url(:/icon/Icon/" + self.cpClass.productTick5 + ");")

        self.PageLabel.setText("Page: " + str(self.page) + "/" + str(len(self.cpClass.product)//5))

    
    
        
