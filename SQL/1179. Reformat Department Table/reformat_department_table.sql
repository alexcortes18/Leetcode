/* Write your T-SQL query statement below */

SELECT 
    id,
    ISNULL([Jan], NULL) AS Jan_Revenue,
    ISNULL([Feb], NULL) AS Feb_Revenue,
    ISNULL([Mar], NULL) AS Mar_Revenue,
    ISNULL([Apr], NULL) AS Apr_Revenue,
    ISNULL([May], NULL) AS May_Revenue,
    ISNULL([Jun], NULL) AS Jun_Revenue,
    ISNULL([Jul], NULL) AS Jul_Revenue,
    ISNULL([Aug], NULL) AS Aug_Revenue,
    ISNULL([Sep], NULL) AS Sep_Revenue,
    ISNULL([Oct], NULL) AS Oct_Revenue,
    ISNULL([Nov], NULL) AS Nov_Revenue,
    ISNULL([Dec], NULL) AS Dec_Revenue
FROM (
    SELECT id, revenue, month
    FROM Department
) AS SourceTable
PIVOT (
    MAX(revenue) 
    FOR month IN ([Jan], [Feb], [Mar], [Apr], [May], [Jun], [Jul], [Aug], [Sep], [Oct], [Nov], [Dec])
) AS PivotTable;


-- for this one i didn't really have an idea so this is just ChatGPT code and I tried to understand it.
-- apparently it is very slow