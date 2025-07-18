SELECT
  Description,
  SUM(Quantity * UnitPrice) AS total_revenue
FROM
  `project-101-466110.SALES.ORDERS`
WHERE
  Country != 'United Kingdom'
  AND Quantity > 0
  AND UnitPrice > 0
  AND Description IS NOT NULL
GROUP BY
  Description
ORDER BY
  total_revenue DESC
LIMIT 10;