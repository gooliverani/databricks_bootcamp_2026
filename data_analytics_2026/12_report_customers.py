# Databricks notebook source
# MAGIC %md
# MAGIC #Customer Report
# MAGIC #####Purpose:
# MAGIC - This report consolidates key customer metrics and behaviors
# MAGIC 	
# MAGIC #####Highlights:
# MAGIC 1. Gathers essential fields such as names, ages, and transaction details.
# MAGIC 2. Segments customers into categories (VIP, Regular, New) and age groups.
# MAGIC 3. Aggregates customer-level metrics:
# MAGIC - total orders
# MAGIC - total sales
# MAGIC - total quantity purchased
# MAGIC - total products
# MAGIC - lifespan (in months)
# MAGIC 4. Calculates valuable KPIs:
# MAGIC - recency (months since last order)
# MAGIC - average order value
# MAGIC - average monthly spend

# COMMAND ----------

# MAGIC %md
# MAGIC ###Create Report: gold.report_customers 

# COMMAND ----------

# DBTITLE 1,Create gold.report_customers view
query = """
CREATE OR REPLACE VIEW gold.report_customers AS

-- 1) Base Query: Retrieves core columns from tables
WITH base_query AS (
    SELECT
        f.order_number,
        f.product_key,
        f.order_date,
        f.sales_amount,
        f.quantity,
        c.customer_key,
        c.customer_number,
        CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
        YEAR(CURRENT_DATE()) - YEAR(c.birthdate) AS age
    FROM gold.fact_sales AS f
    LEFT JOIN gold.dim_customers AS c
        ON c.customer_key = f.customer_key
    WHERE order_date IS NOT NULL
),
-- 2) Customer Aggregations: Summarizes key metrics at the customer level
customer_aggregation AS (
    SELECT
        customer_key,
        customer_number,
        customer_name,
        age,
        COUNT(DISTINCT order_number) AS total_orders,
        SUM(sales_amount) AS total_sales,
        SUM(quantity) AS total_quantity,
        COUNT(DISTINCT product_key) AS total_products,
        MAX(order_date) AS last_order_date,
        (YEAR(MAX(order_date)) - YEAR(MIN(order_date))) * 12 + (MONTH(MAX(order_date)) - MONTH(MIN(order_date))) AS lifespan
    FROM base_query
    GROUP BY customer_key, customer_number, customer_name, age
    ORDER BY customer_key, customer_number, customer_name, age
)
-- Final query
SELECT
    customer_key,
    customer_number,
    customer_name,
    age,
    CASE
        WHEN age < 20 THEN 'Under 20'
        WHEN age BETWEEN 20 AND 29 THEN '20-29'
        WHEN age BETWEEN 30 AND 39 THEN '30-39'
        WHEN age BETWEEN 40 AND 49 THEN '40-49'
        ELSE '50 and above'
    END AS age_group,
    CASE
        WHEN lifespan >= 12 AND total_sales > 5000 THEN 'VIP'
        WHEN lifespan >= 12 AND total_sales <= 5000 THEN 'Regular'
        ELSE 'New'
    END AS customer_segment,
    last_order_date,
    ROUND(MONTHS_BETWEEN(CURRENT_DATE(), last_order_date), 0) AS recency,
    total_orders,
    total_sales,
    total_quantity,
    total_products,
    lifespan,
    -- Compute average order value (AVO)
    CASE
        WHEN total_orders = 0 THEN 0    -- make sure to not devide with 0
        ELSE ROUND(total_sales / total_orders, 0)
    END AS avg_order_value,
    -- Compute average monthly spend
    CASE
        WHEN lifespan = 0 THEN total_sales
        ELSE ROUND(total_sales / lifespan, 0)
    END AS avg_monthly_spend
FROM customer_aggregation
"""
df = spark.sql(query)

df.display()

print("View 'report_customers' created successfully!")


# COMMAND ----------

# DBTITLE 1,Select All from the View
query = """
SELECT * FROM gold.report_customers
"""
df = spark.sql(query)

df.display()

# COMMAND ----------

# DBTITLE 1,Age Group Analysis
query = """
SELECT 
	age_group,
	COUNT(customer_number) AS total_customers,
	SUM(total_sales) AS total_sales
FROM gold.report_customers
GROUP BY age_group
"""
df = spark.sql(query)

df.display()

# COMMAND ----------

# DBTITLE 1,Customer count and sales by segment
query = """
SELECT 
	customer_segment,
	COUNT(customer_number) AS total_customers,
	SUM(total_sales) AS total_sales
FROM gold.report_customers
GROUP BY customer_segment
ORDER BY total_sales DESC
"""
df = spark.sql(query)

df.display()