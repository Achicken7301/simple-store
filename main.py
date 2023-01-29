from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QEvent, QObject
from PyQt5.QtWidgets import QMenu, QMessageBox, QTableWidgetItem, QDialogButtonBox
import sys

# Load ui
from ui.ui_main import Ui_MainWindow

# Database
from database.Customer import Customer
from database.Product import Product
from database.Invoice import Invoice

# Load View
from views.AddCusView import AddCusView
from views.AddProductView import AddProductView
from views.AddProduct2InvoiceView import AddProduct2Invoice
from views.ErrorView import WarningView


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Load the UI Page
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        """
        CUSTOMER
        """
        # Load all cus data
        cus = Customer()
        datas = cus.get_all()
        for d in datas:
            self.ui.cus_list.addItems(d)

        # search user bar
        self.ui.cus_search_bar.textChanged.connect(self.on_cus_search_bar)
        self.ui.cus_list.itemDoubleClicked.connect(self.on_cus_list_widget)
        self.ui.cus_list.installEventFilter(self)

        # Add cus btn
        self.ui.add_cus.clicked.connect(self.on_add_cus)

        """
        PRODUCT
        """
        # Load product data
        product = Product()
        products = product.get_all_p_names()
        for p in products:
            self.ui.p_list.addItems(p)

        # search product bar
        self.ui.p_search_bar.textChanged.connect(self.on_p_search_bar)
        self.ui.p_list.itemDoubleClicked.connect(self.on_p_list_widget)
        self.ui.p_list.installEventFilter(self)

        # Add product btn
        self.ui.add_p.clicked.connect(self.on_add_p)

        """
        INVOICE
        """
        self.cus_choosed = False
        self.ui.add_p2invoice.clicked.connect(self.on_add_p2invoice)

    def on_add_p2invoice(self):
        # Create a buffer for query
        query = dict()
        
        if self.cus_choosed:
            dlg = AddProduct2Invoice()
            if dlg.exec():
                query["c_name"] = self.cus_name
                query["p_name"] = dlg.ui.p_name_input.text()
                query["p_quantity"] = int(dlg.ui.p_quantity_input.text())
                query["i_create_date"] = dlg.ui.create_date.text()

                # Check if new price
                if len(dlg.ui.new_unit_price_input.text()):
                    query["p_unit_price"] = float(
                        dlg.p.de_seperated(dlg.ui.new_unit_price_input.text())
                    )
                else:
                    query["p_unit_price"] = float(
                        dlg.p.de_seperated(dlg.ui.unit_price_input.text())
                    )
                
                dlg.addp2Invoice(query)
                # update Invoice
                self.update_table_widget(query["c_name"])

            else:
                print("Cancel")
        else:
            WarningView(
                "Vui lòng chọn khách hàng!!!\nDouble Click vào bảng danh sách khách hàng."
            )

    # https://www.youtube.com/watch?v=2Ie-EBwJOZU
    def eventFilter(self, source: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.ContextMenu and source is self.ui.cus_list:
            cus_menu = QMenu()
            cus_menu.addAction("Edit", self.cus_edit)
            cus_menu.addAction("Delete", self.cus_delete)
            cus_menu.exec_(event.globalPos())
            return True
        elif event.type() == QEvent.ContextMenu and source is self.ui.p_list:
            p_menu = QMenu()
            p_menu.addAction("Edit", self.p_edit)
            p_menu.addAction("Delete", self.p_delete)
            p_menu.exec_(event.globalPos())
            return True

        return super().eventFilter(source, event)

    """
    CRUD PRODUCT
    """

    def on_add_p(self):
        print("add_p clicked")
        dlg = AddProductView()
        dlg.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        p_data = dict()

        if dlg.exec():
            p_data["name"] = dlg.ui.p_name_input.text()
            p_data["unit_price"] = dlg.ui.unit_price_input.text()
            if len(p_data["unit_price"]) > 0 and len(p_data["name"]) > 0:
                dlg.add(p_data)
                print(f"Added {p_data}")
            else:
                print("Input Nothing!!")
        else:
            print("Cancel")

    def p_edit(self):
        pass

    def p_delete(self):
        pass

    """
    CRUD CUSTOMER
    """

    def on_add_cus(self):
        print("add_cus clicked")
        dlg = AddCusView()
        cus_data = dict()

        if dlg.exec():
            cus_data["name"] = dlg.ui.cus_name_input.text()
            if len(cus_data["name"]) > 0:
                print(type(cus_data["name"]))
                dlg.add(cus_data)
                print(f"Added customer: {cus_data}")
            else:
                print("Input Nothing!!")
        else:
            print("Cancel")

    def cus_delete(self):
        WarningView(
            "Xóa khách hàng sẽ xóa hết tất cả hóa đơn liên quan\nBạn có chắc chắn không?"
        )

    def cus_edit(self):
        print("cus_edit")

    def on_p_list_widget(self, text):
        print(f"Product '{text.text()}' is selected")
        p = Product()
        p_infos = p.get_per_product(text.text())
        for p_info in p_infos:
            self.ui.p_name.setText(f"# {p_info[0]}")
            self.ui.p_unit_price.setText(f"**{p.seperated_by.format(p_info[1])}**")
            self.ui.p_location.setText(f"**{p_info[2]}**")

    def on_p_search_bar(self, text):
        self.ui.p_list.clear()
        product = Product()
        products = product.get_p_name(value=text)
        for p in products:
            self.ui.p_list.addItems(p)

    def on_cus_list_widget(self, text):
        # Add Condition for p2Invoice
        self.cus_choosed = True
        self.cus_name = text.text()  # Use this to query

        print(f"Customer '{text.text()}' is selected")
        self.ui.invoice_name.setText(f"# Tên Khách Hàng: {text.text()}")

        # Run SQL QUERY FROM INVOICE table
        self.update_table_widget(text.text())

    def update_table_widget(self, name):
        invoice = Invoice()
        invoices = invoice.get(name)

        # Add data to table widget
        labels = ["Tên sản phẩm", "Đơn giá (VND)", "Số lượng", "Ngày mua"]
        self.ui.invoice_table.setRowCount(0)
        self.ui.invoice_table.setColumnCount(len(labels))
        self.ui.invoice_table.setHorizontalHeaderLabels(labels)
        self.ui.invoice_table.setSortingEnabled(True)

        # DONT KNOW HOW, BUT IT WORKS https://www.youtube.com/watch?v=_QKVDfVyRbM
        for row_number, row_data in enumerate(invoices):
            self.ui.invoice_table.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.ui.invoice_table.setItem(
                    row_number, column_number, QTableWidgetItem(str(data))
                )

    def on_cus_search_bar(self, text):
        self.ui.cus_list.clear()
        cus = Customer()
        datas = cus.get_name(value=text)
        for data in datas:
            self.ui.cus_list.addItems(data)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Store")
    window.show()

    app_icon = QtGui.QIcon()
    app_icon.addFile("icon/boss.png", QtCore.QSize(64, 64))
    app.setWindowIcon(app_icon)

    sys.exit(app.exec_())
