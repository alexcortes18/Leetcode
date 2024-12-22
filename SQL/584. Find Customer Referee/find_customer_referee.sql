-- SELECT c.name
-- FROM Customer c
-- WHERE c.referee_id != 2 or c.referee_id IS NULL

SELECT c.name
FROM Customer c
WHERE NOT EXISTS (
    SELECT 1
    FROM Customer ref
    WHERE ref.id = c.referee_id AND ref.id = 2
);
