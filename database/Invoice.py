from database.Database import Database
from database.Customer import Customer
from database.Product import Product

class Invoice(Customer, Product):
    
    def __init__(self) -> None:
        super().__init__()
        self.connect()
        self.table = "invoice"
        self.column_FK_cus_id = "cus_id"
        self.column_FK_p_id = "p_id"
        self.column_curr_unit_price = "curr_unit_price"
        self.column_quantity = "quantity"
        self.column_create_date = "create_date"
        self.column_paid_date = "paid_date"
        
        self.c = Customer()
        self.p = Product()
        
        
        
    # TODO: Inefficient query, need to be optimize for large amount of data
    def get(self, name):
        mycursor = self.mydb.cursor()
        mycursor.execute(f"""SELECT {self.p.table}.{self.p.column_name}, {self.table}.{self.column_curr_unit_price}, {self.table}.{self.column_quantity}, {self.table}.{self.column_create_date}
                            FROM {self.table}
                            INNER JOIN {self.c.table} ON {self.table}.{self.column_FK_cus_id} = {self.c.table}.{self.c.column_id}
                            INNER JOIN {self.p.table} ON {self.table}.{self.column_FK_p_id} = {self.p.table}.{self.p.column_id}
                            WHERE {self.c.table}.{self.c.column_name} = '{name}'
                            ORDER BY {self.column_create_date} ASC
                            """)
        myresult = mycursor.fetchall()
        return myresult
        