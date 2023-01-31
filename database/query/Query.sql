INSERT INTO invoice (cus_id, create_date)
VALUES ('4', CURRENT_TIMESTAMP())


INSERT INTO invoice_detail (FK_i_id, FK_p_id, quantity, curr_unit_price)
VALUE (1,2,1,970000)


SELECT	p.name AS p_name, 
			i_d.curr_unit_price AS unit_price, 
			i_d.quantity
FROM invoice_detail AS i_d
JOIN invoice AS i ON i.id = i_d.FK_i_id
JOIN product AS p ON p.product_id = i_d.FK_p_id
WHERE i.id = 4182


SELECT i.id AS invoice_id, i.create_date, COUNT(i.id) AS total_p
FROM invoice_detail AS i_d
JOIN invoice AS i ON i.id = i_d.FK_i_id
JOIN customer AS c ON c.id = i.cus_id
WHERE c.name = 'Kyle Garcia'
GROUP BY i.id
