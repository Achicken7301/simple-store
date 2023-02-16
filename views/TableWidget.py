from PyQt5.QtWidgets import QTableWidget


class InvoiceTable(QTableWidget):
    def __init__(self, name) -> None:
        super().__init__()
        self.setObjectName(str(name))
        self.cellClicked.connect(self.handleCellClicked)
        
    def handleCellClicked(self, row, column):
        item = self.item(row, column)
        print(f"Table {self.objectName()}, cell ({row}, {column}) clicked: {item.text()}")
