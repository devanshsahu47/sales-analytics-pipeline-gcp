SELECT
  Country,
  SUM(Quantity * UnitPrice) AS total_revenue
FROM
  `project-101-466110.SALES.ORDERS`
WHERE
  Country != 'United Kingdom'
  AND Quantity > 0
  AND UnitPrice > 0
GROUP BY
  Country
ORDER BY
  total_revenue DESC;