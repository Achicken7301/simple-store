from database.Database import Database
from database.Customer import Customer
from database.Product import Product
from database.InvoiceDetail import InvoiceDetail


class Invoice(Database):
    def __init__(self) -> None:
        super().__init__()
        self.connect()
        self.table = "invoice"
        self.column_FK_cus_id = "cus_id"
        self.column_create_date = "create_date"
        self.column_paid_date = "paid_date"

        self.interest_rate = 0.03

        self.seperated_by_bold = "**{:,} VND**"
        self.seperated_by = "{:,.0f}"

        self.c = Customer()
        self.p = Product()

        self.i_d = InvoiceDetail()

        self.connect()
        self.mycursor = self.mydb.cursor()

    # TODO: Inefficient query, need to be optimize for large amount of data
    def getAllInvoice(self, cus_name: str):
        """
        Search by name: UNIQUE *NOTE: not optimize

        Return [(invoice.id, invoice.create_date)]
        """
        i = Invoice()
        self.mycursor.execute(
            f"""SELECT distinct i.id AS invoice_id, i.create_date
                FROM invoice_detail AS i_d
                JOIN invoice AS i ON i.id = i_d.FK_i_id
                JOIN customer AS c ON c.id = i.cus_id
                WHERE c.name = '{cus_name}'
                ORDER BY i.create_date ASC
                """
        )
        return self.mycursor.fetchall()

    def getAllProductFromInvoice(self, invoice_id: int):
        """
        INPUT invoice.id
        
        RETURN all products with invoice.id
        """
        query = f"""
                SELECT	p.name AS p_name, 
                        FORMAT(i_d.curr_unit_price, 0), 
                        i_d.quantity,
                        FORMAT(i_d.quantity * i_d.curr_unit_price, 0)
                FROM invoice_detail AS i_d
                JOIN invoice AS i ON i.id = i_d.FK_i_id
                JOIN product AS p ON p.product_id = i_d.FK_p_id
                WHERE i.id = {invoice_id}
                """
        self.mycursor.execute(query)
        return self.mycursor.fetchall()
        
    def addP2Invoice(self, query_data: dict):
        # INSERT AND UPDATE NEW PRICE
        i = Invoice()
        insert_query = f"""INSERT INTO {i.table}    ({i.table}.{i.column_FK_cus_id}, 
                                                    {i.table}.{i.column_FK_p_id}, 
                                                    {i.table}.{i.column_curr_unit_price}, 
                                                    {i.table}.{i.column_quantity},
                                                    {i.table}.{i.column_create_date})
                            VALUES ((SELECT {self.c.column_id} FROM {self.c.table} WHERE NAME = '{query_data["c_name"]}'), 
                                    (SELECT {self.p.column_id} FROM {self.p.table} WHERE NAME = '{query_data['p_name']}'),
                                    {query_data['p_unit_price']}, 
                                    {query_data['p_quantity']},
                                    STR_TO_DATE('{query_data['i_create_date']}', "%d-%m-%Y %H:%i:%s"))"""

        self.mycursor.execute(insert_query)
        self.mydb.commit()

    def updateTotal(self, name: str):
        i = Invoice()
        query = f"""
            SELECT
            SUM({i.table}.{i.column_curr_unit_price} * {i.table}.{i.column_quantity}),
            SUM((({i.table}.{i.column_curr_unit_price} * {i.table}.{i.column_quantity}) * (DATEDIFF(CURRENT_TIMESTAMP, {i.table}.{i.column_create_date}) / 30) * {self.interest_rate}))
            FROM {i.table}
            INNER JOIN {self.c.table} ON {i.table}.{i.column_FK_cus_id} = {self.c.table}.{self.c.column_id}
            INNER JOIN {self.p.table} ON {i.table}.{i.column_FK_p_id} = {self.p.table}.{self.p.column_id}
            WHERE customer.name = '{name}' AND {i.column_paid_date} IS NULL
            """
        self.mycursor.execute(query)
        myresult = self.mycursor.fetchall()
        return myresult
