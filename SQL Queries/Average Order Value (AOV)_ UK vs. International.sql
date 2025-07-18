SELECT
  CASE
    WHEN Country = 'United Kingdom'
    THEN 'UK Market'
    ELSE 'International Market'
  END AS market_segment,
  SUM(Quantity * UnitPrice) / COUNT(DISTINCT InvoiceNo) AS average_order_value
FROM
  `project-101-466110.SALES.ORDERS`
WHERE
  Quantity > 0 AND UnitPrice > 0
GROUP BY
  market_segment;