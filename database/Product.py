from database.Database import Database


class Product(Database):
    def __init__(self) -> None:
        super().__init__()
        self.connect()

        self.table = "product"
        self.column_id = "product_id"
        self.column_name = "p_name"
        self.column_unit_price = "p_unit_price"
        self.column_location = "p_location"
        self.column_last_update = "last_update"
        
        self.seperated_by_bold = "**{:,} VND**"
        self.seperated_by = "{:,} VND"
        
        self.mycursor = self.mydb.cursor()

    def get_all_p_names(self):
        
        self.mycursor.execute(f"""SELECT {self.column_name} FROM {self.table}""")
        myresult = self.mycursor.fetchall()
        return myresult

    def get_p_name(self, value: str):
        self.mycursor.execute(
            f"""SELECT {self.column_name} 
            FROM {self.table} 
            WHERE {self.column_name} LIKE '%{value}%'"""
        )
        myresult = self.mycursor.fetchall()
        return myresult

    def add(self, infos):
        query = f"""INSERT INTO {self.table} ({self.column_name}, {self.column_unit_price}) 
                    VALUE ('{infos["name"]}', {infos["unit_price"]})"""
        self.mycursor.execute(query)
        self.mydb.commit()

    def get_per_product(self, name: str):
        query = f"""SELECT {self.column_name}, {self.column_unit_price}, {self.column_location} FROM {self.table}
                    WHERE {self.column_name} = '{name}'
                    LIMIT 1
                """
        self.mycursor.execute(query)
        myresult = self.mycursor.fetchall()
        return myresult

    def tuple2list(self, tuple: tuple):
        complete = []
        for result in tuple:
            complete.append(result[0])
        return complete
