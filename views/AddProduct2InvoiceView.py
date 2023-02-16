from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialogButtonBox, QCompleter

from ui.ui_add_p2invoice_V2 import Ui_p2Invoice

from database.Product import Product
from database.Invoice import Invoice


class AddProduct2Invoice(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_p2Invoice()
        self.ui.setupUi(self)

        # self.ui.unit_price_input.setEnabled(False)
        self.ui.p_name_input.textChanged.connect(self.on_p_name_input)
        self.ui.new_unit_price_input.textChanged.connect(self.on_new_unit_price_input)
        self.ui.create_date.setDateTime(QtCore.QDateTime.currentDateTime())

        self.p = Product()
        r = self.p.get_all_p_names()
        names = self.p.tuple2list(r)
        completer = QCompleter(names)
        self.ui.p_name_input.setCompleter(completer)

        # Initiate disable OK buttonBox
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)

    def addp2Invoice(self, query_data: dict):
        print(query_data)
        Invoice().addP2Invoice(query_data)

    def on_p_name_input(self, p_name):
        """GET THE PRICE
        r = [('Amy Wells', 313000, '1')]
        print(data[0][1]) #OUTPUT: 313000
        """
        if len(p_name):
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)

        r = self.p.get_per_product(p_name)
        if len(r):
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
            [(_, price, _)] = r
            self.ui.unit_price_input.setText(price)

            # Clear new_unit_price value
            self.ui.new_unit_price_input.clear()

    def on_new_unit_price_input(self, text):
        """
        ONLY GOD KNOW HOW TO SET UI LIKE THIS LOL...
        """
        if text.isdigit():
            # unit_price must clear
            self.ui.unit_price_input.clear()

            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)

            self.ui.new_unit_price_warning.show()
            self.ui.new_unit_price_warning.setText(
                self.p.seperated_by_bold.format(int(text))
            )
        else:
            self.ui.new_unit_price_warning.show()
            if len(self.ui.new_unit_price_input.text()) == 0:
                self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
                self.ui.new_unit_price_warning.hide()
            else:
                self.ui.new_unit_price_warning.setText("**Giá tiền không hợp lệ!!!**")
                self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
