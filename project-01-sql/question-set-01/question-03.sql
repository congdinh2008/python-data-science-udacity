-- Question 3
-- Finally, provide a table with the family-friendly film category, each of the quartiles, 
-- and the corresponding count of movies within each combination of film category for each corresponding rental duration category. 
-- The resulting table should have three columns:
--      Category
--      Rental length category
--      Count

-- Check Your Solution
-- The following table header provides a preview of what your table should look like. The Count column should be sorted first by Category and then by Rental Duration category.

-- HINT: One way to solve this question requires the use of Percentiles, Window functions and Case statements.

-- Version 01:ACCESS
WITH FamilyFriendlyMovies AS (
    SELECT
        c.name AS category_name,
        f.rental_duration,
        NTILE(4) OVER (ORDER BY f.rental_duration) AS standard_quartile
    FROM
        category AS c
    JOIN
        film_category AS fc
        ON c.category_id = fc.category_id 
        AND c.name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')
    JOIN
        film AS f
        ON f.film_id = fc.film_id
)
SELECT
    ffm.category_name,
    ffm.standard_quartile,
    COUNT(*) AS "Movie Count"
FROM
    FamilyFriendlyMovies AS ffm
GROUP BY
    ffm.category_name, ffm.standard_quartile
ORDER BY
    ffm.category_name, ffm.standard_quartile;


-- Version 02:

WITH FamilyFriendlyMovies AS (
    SELECT
        c.name AS category_name,
        f.rental_duration,
        NTILE(4) OVER (ORDER BY f.rental_duration) AS standard_quartile
    FROM
        category AS c
    JOIN
        film_category AS fc
        ON c.category_id = fc.category_id 
        AND c.name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')
    JOIN
        film AS f
        ON f.film_id = fc.film_id
)
SELECT
    ffm.category_name,
    ffm.standard_quartile,
    CASE
        WHEN ffm.standard_quartile = 1 THEN 'First Quartile'
        WHEN ffm.standard_quartile = 2 THEN 'Second Quartile'
        WHEN ffm.standard_quartile = 3 THEN 'Third Quartile'
        ELSE 'Final Quartile'
    END AS "Rental Duration Quartile",
    COUNT(*) AS "Movie Count"
FROM
    FamilyFriendlyMovies AS ffm
GROUP BY
    ffm.category_name, ffm.standard_quartile
ORDER BY
    ffm.category_name, ffm.standard_quartile;
