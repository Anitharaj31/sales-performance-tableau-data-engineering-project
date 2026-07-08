-- Total Revenue

SELECT 
SUM(total_sales) AS total_revenue
FROM sales;


-- Revenue by Category

SELECT
category,
SUM(total_sales) AS revenue
FROM sales
GROUP BY category
ORDER BY revenue DESC;


-- Top Selling Products

SELECT
product,
SUM(quantity) AS units_sold,
SUM(total_sales) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC;


-- Customer Spending

SELECT
customer_id,
SUM(total_sales) AS total_spent
FROM sales
GROUP BY customer_id
ORDER BY total_spent DESC;


-- Daily Sales Trend

SELECT
order_date,
SUM(total_sales) AS daily_sales
FROM sales
GROUP BY order_date
ORDER BY order_date;
