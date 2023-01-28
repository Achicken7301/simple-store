from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialogButtonBox

# Load model
from database.Product import Product

# Load UI
from ui.ui_add_p_dlg import Ui_AddProduct


class AddProductView(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_AddProduct()
        self.ui.setupUi(self)
        
        self.ui.unit_price_input.textChanged.connect(self.on_unit_price_input)
        self.p = Product()
        

    def on_unit_price_input(self, text):
        if text.isdigit():
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
            self.ui.unit_price_warnin_input.hide()
            self.ui.seperate_unit_price.show()   
            self.ui.seperate_unit_price.setText(self.p.seperated_by_bold.format(int(text)))            
        else:
            self.ui.seperate_unit_price.hide()
            self.ui.unit_price_warnin_input.show()
            self.ui.unit_price_warnin_input.setText("**Giá tiền không hợp lệ!!!**")
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
            

    def add(self, p_infos: dict):
        self.p.add(p_infos)
