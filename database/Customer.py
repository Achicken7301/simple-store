from database.Database import Database


class Customer(Database):
    def __init__(self) -> None:
        super().__init__()
        self.table = "customer"
        self.column_id = "id"
        self.column_name = "name"

        self.connect()
        self.mycursor = self.mydb.cursor()

    def get_all(self):
        self.mycursor.execute(
            f"""   
                SELECT {self.column_name} FROM {self.table} 
                ORDER BY {self.column_name} ASC
            """
        )
        return self.mycursor.fetchall()

    def get_name(self, value: str):
        self.mycursor.execute(
            f"""
                SELECT {self.column_name} FROM {self.table} 
                WHERE {self.column_name} LIKE '%{value}%'
            """
        )
        return self.mycursor.fetchall()

    def get_per_cus(self, name: str):
        self.mycursor.execute(
            f"""
                SELECT {self.column_name} FROM {self.table} 
                WHERE {self.column_name} = '{name}'
                LIMIT 1
            """
        )
        return self.mycursor.fetchall()

    def add_cus(self, infos):
        query = f"""INSERT INTO {Customer().table} ({self.column_name}) VALUE ('{infos["name"]}')"""
        self.mycursor.execute(query)
        self.mydb.commit()
