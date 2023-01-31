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

date_diff = faker.date_time_between(start_date="-3y", end_date="now")
for i in range(50000):
    try:
        mycursor.execute(
            f"""
            
            INSERT INTO invoice_detail (FK_i_id, FK_p_id, quantity, curr_unit_price)
            VALUE ({random.randrange(1, 10000, 1)},{random.randrange(4, 1000, 1)},{random.randrange(1, 10, 1)},{random.randrange(1000, 1000000, 1000)})
            """
        )
    except Exception as e:
        print("Trùng dữ liệu")

    mydb.commit()
