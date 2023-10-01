-- Question 2
-- Now we need to know how the length of rental duration of these family-friendly movies compares to the duration that all movies are rented for. 
-- Can you provide a table with the movie titles and divide them into 4 levels (first_quarter, second_quarter, third_quarter, and final_quarter) 
-- based on the quartiles (25%, 50%, 75%) of the average rental duration(in the number of days) for movies across all categories? 
-- Make sure to also indicate the category that these family-friendly movies fall into.

-- Check Your Solution
-- The data are not very spread out to create a very fun looking solution, but you should see something like the following if you correctly split your data. 
-- You should only need the category, film_category, and film tables to answer this and the next questions. 

-- HINT: One way to solve it requires the use of percentiles, Window functions, subqueries or temporary tables.

-- Version 01: 

WITH FamilyMovies AS (
    SELECT
        f.title AS film_title,
        c.name AS category_name,
        f.rental_duration
    FROM
        category AS c
    JOIN
        film_category AS fc
        ON c.category_id = fc.category_id
        AND c.name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')
    JOIN
        film AS f
        ON f.film_id = fc.film_id
    ORDER BY
        category_name, film_title
)
, Quartiles AS (
    SELECT
        *,
        NTILE(4) OVER (ORDER BY rental_duration) AS standard_quartile
    FROM
        FamilyMovies
)
SELECT 
    *
FROM
    Quartiles;




-- Version 02:

WITH FamilyMovies AS (
    SELECT
        f.title AS film_title,
        c.name AS category_name,
        f.rental_duration
    FROM
        category AS c
    JOIN
        film_category AS fc
        ON c.category_id = fc.category_id
        AND c.name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')
    JOIN
        film AS f
        ON f.film_id = fc.film_id
    ORDER BY
        category_name, film_title
)
, Quartiles AS (
    SELECT
        *,
        NTILE(4) OVER (ORDER BY rental_duration) AS standard_quartile
    FROM
        FamilyMovies
)
SELECT
    *,
    CASE
        WHEN standard_quartile = 1 THEN 'first_quarter'
        WHEN standard_quartile = 2 THEN 'second_quarter'
        WHEN standard_quartile = 3 THEN 'third_quarter'
        ELSE 'final_quarter'
    END AS rental_duration_quartile
FROM
    Quartiles;