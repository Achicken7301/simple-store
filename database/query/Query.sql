SELECT customer.customer_name, product.product_name, invoice.curr_unit_price, invoice.quantity, invoice.create_date
FROM invoice
INNER JOIN customer ON invoice.cus_id = customer.customer_id
INNER JOIN product ON invoice.p_id = product.product_id
WHERE customer.customer_name = 'Aaron Williamson'


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
