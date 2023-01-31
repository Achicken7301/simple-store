from faker import Faker
import mysql.connector
import random
import time
from datetime import date

faker = Faker(["vi_VN"])
mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="store"
)
mycursor = mydb.cursor()
print( faker.date_time_between(start_date="-3y", end_date="now"))

for i in range(10000):
    date_diff = faker.date_time_between(start_date="-3y", end_date="now")
    mycursor.execute(
        f"""
        INSERT INTO invoice (cus_id, create_date)
        VALUES ({random.randrange(4, 1000, 1)}, '{date_diff}')
        """
    )

    mydb.commit()
