# Databricks notebook source
# MAGIC %md
# MAGIC #Data Segmentation Analysis
# MAGIC #####Purpose:
# MAGIC - To group data into meaningful categories for targeted insights.
# MAGIC - For customer segmentation, product categorization, or regional analysis.
# MAGIC 	
# MAGIC #####SQL Functions Used:
# MAGIC - CASE: Defines custom segmentation logic.
# MAGIC - GROUP BY: Groups data into segments.
# MAGIC ##### [Measure] By [Measure]
# MAGIC - Total Products By Sales Range
# MAGIC - Total Customers By Age

# COMMAND ----------

# MAGIC %md
# MAGIC ###Segment products into cost ranges and count how many products fall into each segment

# COMMAND ----------

query = """
WITH product_segments AS (
    SELECT
        product_key,
        product_name,
        product_cost,
        CASE
            WHEN product_cost < 100 THEN 'Below 100'
            WHEN product_cost BETWEEN 100 AND 500 THEN '100-500'
            WHEN product_cost BETWEEN 500 AND 1000 THEN '500-1000'
            ELSE 'Above 1000'
        END AS cost_range
    FROM gold.dim_products
)
SELECT
    cost_range,
    COUNT(product_key) AS total_products
FROM product_segments
GROUP BY cost_range
ORDER BY total_products DESC
"""
df = spark.sql(query)

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ####Group customers into three segments based on their spending behavior:
# MAGIC - VIP: Customers with at least 12 months of history and spending more than €5,000.
# MAGIC - Regular: Customers with at least 12 months of history but spending €5,000 or less.
# MAGIC - New: Customers with a lifespan less than 12 months.
# MAGIC ####And find the total number of customers by each group

# COMMAND ----------

query = """
WITH customer_spending AS (
    SELECT
        c.customer_key,
        SUM(f.sales_amount) AS total_spending,
        MIN(order_date) AS first_order,
        MAX(order_date) AS last_order,
        (YEAR(MAX(order_date)) - YEAR(MIN(order_date))) * 12 + (MONTH(MAX(order_date)) - MONTH(MIN(order_date))) AS lifespan
    FROM gold.fact_sales AS f
    LEFT JOIN gold.dim_customers AS c
        ON f.customer_key = c.customer_key
    GROUP BY c.customer_key
)
SELECT
    customer_segment,
    COUNT(customer_key) AS total_customers
FROM (
    SELECT
        customer_key,
        CASE
            WHEN lifespan >= 12 AND total_spending > 5000 THEN 'VIP'
            WHEN lifespan >= 12 AND total_spending <= 5000 THEN 'Regular'
            ELSE 'New'
        END AS customer_segment
    FROM customer_spending
) AS t
GROUP BY customer_segment
ORDER BY total_customers DESC
"""
df = spark.sql(query)

df.display()
