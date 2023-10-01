-- Question 2
-- We would like to know who were our top 10 paying customers, how many payments they made on a monthly basis during 2007, and what was the amount of the monthly payments. 
-- Can you write a query to capture the customer name, month and year of payment, and total payment amount for each month by these top 10 paying customers?

-- Check your Solution:
-- The following table header provides a preview of what your table should look like. The results are sorted first by customer name and then for each month. 
-- As you can see, total amounts per month are listed for each customer.

-- HINT: One way to solve is to use a subquery, limit within the subquery, and use concatenation to generate the customer name.

-- Version 01: 
WITH TopPayingCustomers AS (
    -- Subquery to find the top 10 paying customers
    SELECT 
        c.first_name || ' ' || c.last_name AS fullname, 
        SUM(p.amount) AS amount_total
    FROM 
        customer c
    JOIN 
        payment p
        ON p.customer_id = c.customer_id
    WHERE 
        p.payment_date BETWEEN '2007-01-01' AND '2008-01-01'
    GROUP BY 
        fullname
    ORDER BY 
        amount_total DESC
    LIMIT 10
)
SELECT 
    DATE_TRUNC('month', p.payment_date) AS pay_mon, 
    c.first_name || ' ' || c.last_name AS fullname, 
    COUNT(p.amount) AS pay_countpermon, 
    SUM(p.amount) AS pay_amount
FROM 
    customer c
JOIN 
    payment p
    ON p.customer_id = c.customer_id
WHERE 
    c.first_name || ' ' || c.last_name IN (SELECT fullname FROM TopPayingCustomers)
    AND p.payment_date BETWEEN '2007-01-01' AND '2008-01-01'
GROUP BY 
    pay_mon, fullname
ORDER BY 
    fullname, pay_mon, pay_countpermon;


-- Version 02:
SELECT 
    DATE_TRUNC('month', p.payment_date) pay_mon, c.first_name || ' ' || c.last_name AS fullname, 
    COUNT(p.amount) AS pay_countpermon, 
    SUM(p.amount) AS pay_amount
FROM customer c
JOIN payment p
    ON p.customer_id = c.customer_id
WHERE 
    c.first_name || ' ' || c.last_name IN (
        SELECT t1.fullname
        FROM (
            SELECT 
                c.first_name || ' ' || c.last_name AS fullname, 
                SUM(p.amount) as amount_total
            FROM customer c
            JOIN payment p
            ON p.customer_id = c.customer_id
            GROUP BY fullname
            ORDER BY amount_total DESC
            LIMIT 10
        ) t1) 
        AND (p.payment_date BETWEEN '2007-01-01' AND '2008-01-01')
GROUP BY fullname, pay_mon
ORDER BY fullname, pay_mon, pay_countpermon;
