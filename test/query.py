import mysql.connector
import datetime

host = "localhost"
user = "root"
password = ""
port = "3306"
database = "store"

mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    port=port,
    database=database,
)

mycursor = mydb.cursor()

query = """SELECT 	i.id AS invoice_id,
                    i.create_date AS create_date,
                    p.name AS p_name, 
                    i_d.curr_unit_price AS unit_price, 
                    i_d.quantity,
                    c.name AS cus_name
            FROM invoice_detail AS i_d
            JOIN invoice AS i ON i.id = i_d.FK_i_id
            JOIN product AS p ON p.product_id = i_d.FK_p_id
            JOIN customer AS c ON c.id = i.cus_id
            WHERE i.id = 5 """

mycursor.execute(query)
results = mycursor.fetchall()
print(results)
