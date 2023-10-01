-- Question 1:
-- We want to find out how the two stores compare in their count of rental orders during every month for all the years we have data for. 
-- Write a query that returns the store ID for the store, the year and month and the number of rental orders each store has fulfilled for that month. 
-- Your table should include a column for each of the following: year, month, store ID and count of rental orders fulfilled during that month.

-- Check Your Solution
-- The following table header provides a preview of what your table should look like. The count of rental orders is sorted in descending order.

-- HINT: One way to solve this query is the use of aggregations.

SELECT
    EXTRACT(MONTH FROM r.rental_date) AS rental_month,
    EXTRACT(YEAR FROM r.rental_date) AS rental_year,
    s.store_id,
    COUNT(*) AS count_rentals
FROM
    rental AS r
JOIN
    staff AS sf
    ON r.staff_id = sf.staff_id
JOIN 
    store AS s
    ON s.store_id = sf.store_id
GROUP BY
    rental_month, rental_year, s.store_id
ORDER BY
    rental_month, rental_year, s.store_id, count_rentals;