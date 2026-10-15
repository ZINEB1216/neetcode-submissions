-- Write your query below
SELECT seller_name
FROM seller
LEFT JOIN orders
ON orders.seller_id = seller.seller_id and sale_date between '2020-01-01' and '2020-12-31'
WHERE sale_date is NULL
Order BY seller_name;