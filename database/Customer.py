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
        myresult = self.mycursor.fetchall()
        return myresult

    def get_name(self, value: str):
        self.mycursor.execute(
            f"""
                SELECT {self.column_name} FROM {self.table} 
                WHERE {self.column_name} LIKE '%{value}%'
            """
        )
        myresult = self.mycursor.fetchall()
        return myresult
    
    def get_per_cus(self, name:str):
        self.mycursor.execute(
            f"""
                SELECT {self.column_name} FROM {self.table} 
                WHERE {self.column_name} = '{name}'
                LIMIT 1
            """
        )
        myresult = self.mycursor.fetchall()
        return myresult

    def add(self, infos):
        query = f"""INSERT INTO {self.table} ({self.column_name}) VALUE ('{infos["name"]}')"""
        self.mycursor.execute(query)
        self.mydb.commit()
