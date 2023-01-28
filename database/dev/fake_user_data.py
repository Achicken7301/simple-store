from faker import Faker
import mysql.connector

faker = Faker(["vi_VN", 'ja_JP'])

print(faker.name())

# mydb = mysql.connector.connect(
#     host="localhost", user="root", password="", database="store"
# )

# mycursor = mydb.cursor()
# for i in range(10):
#     mycursor.execute(
#         f"""
#     INSERT INTO user (user_name) 
#     VALUE ("{faker.name()}")
#     """
#     )

#     mydb.commit()
