/* Write your T-SQL query statement below */

WITH temp AS (
    SELECT book_id, SUM(
    CASE WHEN return_date IS NULL THEN 1
        ELSE 0 END) AS null_amounts
    FROM borrowing_records
    GROUP BY book_id
)
SELECT lb.book_id, lb.title, lb.author, lb.genre, lb.publication_year,
temp.null_amounts AS current_borrowers
FROM library_books as lb
JOIN temp ON lb.book_id = temp.book_id
WHERE lb.total_copies - temp.null_amounts = 0
ORDER BY current_borrowers DESC, lb.title ASC