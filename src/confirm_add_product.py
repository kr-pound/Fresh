from PyQt5 import QtCore, QtGui, QtWidgets

from _confirm_add_product_design import Ui_MainWindow as Ui_confirmAddProductWindow

class ConfirmAddProductWindow(QtWidgets.QMainWindow, Ui_confirmAddProductWindow):
    search = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        #super the class to setup the Ui
        super(ConfirmAddProductWindow, self).__init__(parent)
        self.setupUi(self)
        #after push the button --> close
        self.CloseButton.clicked.connect(self.searchTransfer)

    def searchTransfer(self):
        self.search.emit()
        self.close()