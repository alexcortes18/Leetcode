-- Learning the syntax for functions.
-- IF Statements NOT allowed inside the Return statement.

CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    IF @N < 1
    BEGIN
        RETURN NULL;
    END

    RETURN (
        /* Write your T-SQL query statement below. */
        SELECT DISTINCT salary
        FROM Employee
        ORDER BY salary DESC
        OFFSET (@N -1) ROW FETCH NEXT 1 ROW ONLY
    );
END