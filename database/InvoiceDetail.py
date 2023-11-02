from database.Database import Database


class InvoiceDetail(Database):
    def __init__(self) -> None:
        super().__init__()

        self.table = "invoice_detail"
        self.column_FK_i_id = "FK_i_id"
        self.column_FK_p_id = "FK_p_id"
        self.column_quantity = "quantity"
        self.column_curr_unit_price = "curr_unit_price"

    def get_date_from_invoice(self, invoice_id):
        pass
