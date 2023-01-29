INSERT INTO invoice AS i

SELECT c.c_name p.p_name FROM invoice AS i
INNER JOIN customer AS c ON i.cus_id = i.c_id
INNER JOIN product AS p ON i.p_id = i.product_id
WHERE c.c_name = 'test'

INSERT INTO invoice (invoice.cus_id, invoice.p_id, invoice.curr_unit_price, invoice.quantity, invoice.create_date)
VALUES ((SELECT id FROM customer WHERE NAME = 'test'), 
		(SELECT product_id FROM product WHERE NAME = 'Denise Contreras'),
		875000, 
		1, 
		"2023-01-29 17:18:48")
		
SELECT STR_TO_DATE('15-6-2022 17:50:48', "%d-%m-%Y %H:%i:%s")
SELECT STR_TO_DATE("10-17-2021 15:40:10", "%m-%d-%Y %H:%i:%s");

UPDATE product
SET unit_price = 100000
WHERE NAME = 'Denise Contreras'

SELECT id FROM customer WHERE NAME = 'test'
SELECT product_id FROM product WHERE NAME = 'Gene Craig'


SELECT product.name, invoice.quantity,invoice.curr_unit_price, invoice.create_date,invoice.curr_unit_price * invoice.quantity AS total_price,
	(DATEDIFF(CURRENT_TIMESTAMP, invoice.create_date)/30) AS week_diff
FROM invoice
INNER JOIN customer ON invoice.cus_id = customer.id
INNER JOIN product ON invoice.p_id = product.product_id
WHERE customer.name = '7 Viên Ngọc Rồng'



SELECT DATEDIFF(CURRENT_TIMESTAMP, '2023-01-10 00:00:00') AS daysdiff
SELECT CURRENT_TIMESTAMP
INSERT INTO invoice (cus_id, p_id, curr_unit_price)
VALUES (44, 22, 106000)

CREATE TABLE test(
test_id INT AUTO_INCREMENT,
test_date DATETIME DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (test_id)
)

ALTER TABLE invoice
ALTER COLUMN quantity SET DEFAULT 1

ALTER TABLE product AUTO_INCREMENT = 1


INSERT INTO customer (customer_name)
VALUE ("căng hải")

SELECT product_name FROM product
ORDER BY last_update DESC


ALTER TABLE customer
ADD UNIQUE (customer_name)

SELECT * FROM product
WHERE product_name = 'Jeremy Johnson'
LIMIT 1

INSERT INTO invoice (cus_id, p_id, curr_unit_price, quantity, create_date)
VALUES (4,12,10000,4,2021-01-27)


ALTER TABLE test
ADD COLUMN username VARCHAR(50) UNIQUE

SELECT * FROM customer
WHERE customer_name LIKE "%Robert%"


SELECT * FROM customer
WHERE c_name LIKE '%Alan%'
LIMIT 1

INSERT INTO test (test_date, username)
VALUE ('2000-01-02 01:02:03', 'abc1')
