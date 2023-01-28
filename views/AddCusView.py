from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialogButtonBox

# Load model
from database.Customer import Customer

from ui.ui_add_cus_dlg import Ui_AddCus


class AddCusView(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_AddCus()
        self.ui.setupUi(self)

        self.ui.cus_name_input.textChanged.connect(self.on_cus_name_input)

    def on_cus_name_input(self, name: str):
        cus = Customer()
        result = cus.get_per_cus(name)
        if len(result):
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)

            self.ui.cus_input_warning.show()
            self.ui.cus_input_warning.setText(
                "**Tên người dùng đã được sử dụng. Vui lòng nhập tên khác!!!**"
            )
        else:
            self.ui.cus_input_warning.hide()
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)

    def add(self, cus_infos: dict):
        cus = Customer()
        cus.add(cus_infos)
