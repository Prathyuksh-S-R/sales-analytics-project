Q1 — Sales by Region
SELECT Region,
       SUM(Sales) AS TotalSales
FROM orders
GROUP BY Region
ORDER BY TotalSales DESC;


Q2 — Profit by Category
SELECT Category,
       SUM(Profit) AS TotalProfit
FROM orders
GROUP BY Category
ORDER BY TotalProfit DESC;


Q3 — Furniture Sub-Category Profit
SELECT `Sub-Category`,
       SUM(Profit) AS TotalProfit
FROM orders
WHERE Category = 'Furniture'
GROUP BY `Sub-Category`
ORDER BY TotalProfit ASC;


Q4 — Discount vs Profit
SELECT `Sub-Category`,
       AVG(Discount) AS AvgDiscount,
       SUM(Profit) AS TotalProfit
FROM orders
WHERE Category = 'Furniture'
GROUP BY `Sub-Category`
ORDER BY AvgDiscount DESC;
