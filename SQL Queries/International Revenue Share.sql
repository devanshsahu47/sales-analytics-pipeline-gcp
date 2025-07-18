SELECT
  (SUM(CASE WHEN Country != 'United Kingdom' THEN (Quantity * UnitPrice) ELSE 0 END) / SUM(Quantity * UnitPrice)) * 100 AS international_revenue_share_percent
FROM
  `project-101-466110.SALES.ORDERS`
WHERE
  Quantity > 0 AND UnitPrice > 0;