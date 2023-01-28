import mysql.connector


class Database:
    def __init__(self) -> None:
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.port = "3306"
        self.database = "store"

    def connect(self):
        self.mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            port=self.port,
            database=self.database,
        )
