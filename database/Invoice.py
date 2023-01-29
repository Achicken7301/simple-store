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

        self.interest_rate = 0.03

        self.c = Customer()
        self.p = Product()

        self.connect()
        self.mycursor = self.mydb.cursor()

    # TODO: Inefficient query, need to be optimize for large amount of data
    def get(self, cus_name):
        self.mycursor.execute(
            f"""SELECT {self.p.table}.{self.p.column_name}, {self.table}.{self.column_curr_unit_price}, {self.table}.{self.column_quantity}, {self.table}.{self.column_create_date}
                            FROM {self.table}
                            INNER JOIN {self.c.table} ON {self.table}.{self.column_FK_cus_id} = {self.c.table}.{self.c.column_id}
                            INNER JOIN {self.p.table} ON {self.table}.{self.column_FK_p_id} = {self.p.table}.{self.p.column_id}
                            WHERE {self.c.table}.{self.c.column_name} = '{cus_name}'
                            ORDER BY {self.column_create_date} ASC
                            """
        )
        myresult = self.mycursor.fetchall()
        return myresult

    def addP2Invoice(self, query_data: dict):
        # INSERT AND UPDATE NEW PRICE
        i = Invoice()
        insert_query = f"""INSERT INTO {i.table}({i.table}.{i.column_FK_cus_id}, 
                                                    {i.table}.{i.column_FK_p_id}, 
                                                    {i.table}.{i.column_curr_unit_price}, 
                                                    {i.table}.{i.column_quantity},
                                                    {i.table}.{i.column_create_date})
                            VALUES ((SELECT {self.c.column_id} FROM {self.c.table} WHERE NAME = '{query_data["c_name"]}'), 
                                    (SELECT {self.p.column_id} FROM {self.p.table} WHERE NAME = '{query_data['p_name']}'),
                                    {query_data['p_unit_price']}, 
                                    {query_data['p_quantity']},
                                    STR_TO_DATE('{query_data['i_create_date']}', "%d-%m-%Y %H:%i:%s"))"""

        update_query = f"""UPDATE {self.p.table}
                            SET {self.p.column_unit_price} = {query_data['p_unit_price']}
                            WHERE NAME = '{query_data['p_name']}' """
        self.mycursor.execute(insert_query)
        self.mycursor.execute(update_query)
        self.mydb.commit()
