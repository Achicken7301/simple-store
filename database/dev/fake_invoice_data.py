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
start = time.time()
for i in range(5000):
    date_diff = faker.date_time_between(start_date='-5y', end_date='now')
    mycursor.execute(
        f"""
    INSERT INTO invoice (cus_id, p_id, curr_unit_price, quantity, create_date)
        VALUES ({random.randrange(5, 1000, 1)}, {random.randrange(1, 1000, 1)}, {random.randrange(50000, 1100000, 1000)}, {random.randrange(1, 10, 1)}, '{date_diff}')
    """
    )

    mydb.commit()
end = time.time()
print(end-start)