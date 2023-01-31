from faker import Faker
import mysql.connector
import random
faker = Faker(["vi_VN"])

print(faker.name())

mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="store"
)
mycursor = mydb.cursor()
for i in range(1000):
    unit_price = random.randrange(50000, 1100000, 1000)
    mycursor.execute(
        f"""
    INSERT INTO product(product_name, product_unit_price, product_location)
    VALUE ("{faker.name()}", {unit_price}, {random.randrange(1, 10, 1)})
    """
    )

    mydb.commit()
