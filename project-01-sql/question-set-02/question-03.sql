-- Question 3
-- Finally, for each of these top 10 paying customers, I would like to find out the difference across their monthly payments during 2007. 
-- Please go ahead and write a query to compare the payment amounts in each successive month. Repeat this for each of these 10 paying customers. 
-- Also, it will be tremendously helpful if you can identify the customer name who paid the most difference in terms of payments.

-- Check your solution:
-- The customer Eleanor Hunt paid the maximum difference of $64.87 during March 2007 from $22.95 in February of 2007.

-- HINT: You can build on the previous questions query to add Window functions and aggregations to get the solution.

-- Version 01:
WITH t1 AS (
    SELECT 
        (first_name || ' ' || last_name) AS name, 
        c.customer_id, 
        p.amount, 
        p.payment_date
    FROM customer AS c
    JOIN payment AS p
    ON c.customer_id = p.customer_id
),
t2 AS (
    SELECT 
        t1.customer_id
    FROM t1
    GROUP BY t1.customer_id
    ORDER BY SUM(t1.amount) DESC
    LIMIT 10
),
t3 AS (
    SELECT 
        t1.name,
        DATE_PART('month', t1.payment_date) AS payment_month, 
        DATE_PART('year', t1.payment_date) AS payment_year,
        COUNT (*) AS count,
        SUM(t1.amount) as sum,
        SUM(t1.amount) AS total,
        LEAD(SUM(t1.amount)) OVER(PARTITION BY t1.name ORDER BY DATE_PART('month', t1.payment_date)) AS lead,
        LEAD(SUM(t1.amount)) OVER(PARTITION BY t1.name ORDER BY DATE_PART('month', t1.payment_date)) - SUM(t1.amount) AS lead_dif
    FROM t1
    JOIN t2
    ON t1.customer_id = t2.customer_id
    WHERE t1.payment_date BETWEEN '20070101' AND '20080101'
    GROUP BY t1.name, payment_month, payment_year
    ORDER BY t1.name, payment_month, payment_year
)
SELECT 
    t3.name, 
    t3.payment_month::INT, 
    t3.payment_year::INT,
    t3.count,
    t3.sum,
    t3.total,
    t3.lead,
    t3.lead_dif,
    CASE
    WHEN t3.lead_dif = (SELECT MAX(t3.lead_dif) FROM t3 ORDER BY 1 DESC LIMIT 1) THEN 'Maximum difference'
    ELSE NULL
    END AS is_max					
FROM t3
ORDER BY t3.name;