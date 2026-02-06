# Databricks notebook source
# MAGIC %md
# MAGIC #Ranking Analysis
# MAGIC #####Purpose:
# MAGIC - To rank items (e.g., products, customers) based on performance or other metrics.
# MAGIC - To identify top performers or laggards.
# MAGIC 	
# MAGIC #####SQL Functions Used:
# MAGIC - Window Ranking Functions: RANK(), DENSE_RANK(), ROW_NUMBER(), TOP
# MAGIC - Clauses: GROUP BY, ORDER BY
# MAGIC ##### Rank [Dimension] By Aggregated [Measure]
# MAGIC - Rank Countries By Total Sales
# MAGIC - Top 5 Products By Quantity
# MAGIC - Bottom 3 Customers By Total Orders

# COMMAND ----------

# MAGIC %md
# MAGIC ####Which 5 products Generating the Highest Revenue?
# MAGIC - Simple Ranking

# COMMAND ----------

query = """
SELECT
    p.product_name,
    SUM(f.sales_amount) AS total_renenue
FROM gold.fact_sales AS f
LEFT JOIN gold.dim_products AS p
    ON p.product_key = f.product_key
GROUP BY p.product_name
ORDER BY total_renenue DESC
LIMIT 5
"""
df = spark.sql(query)

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC - Complex but Flexibly Ranking Using Window Functions

# COMMAND ----------

query = """
SELECT *
FROM (
    SELECT
        p.product_name,
        SUM(f.sales_amount) AS total_renenue,
        ROW_NUMBER() OVER (ORDER BY SUM(f.sales_amount) DESC) AS rank_products
    FROM gold.fact_sales AS f
    LEFT JOIN gold.dim_products AS p
        ON p.product_key = f.product_key
    GROUP BY p.product_name
) AS t
WHERE rank_products <= 5
"""
df = spark.sql(query)

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ####What are the 5 worst-performing products in terms of sales?

# COMMAND ----------

# DBTITLE 1,What are the 5 worst-performing products in terms of sales?
query = """
SELECT
    p.product_name,
    SUM(f.sales_amount) AS total_renenue
FROM gold.fact_sales AS f
LEFT JOIN gold.dim_products AS p
    ON p.product_key = f.product_key
GROUP BY p.product_name
ORDER BY total_renenue
LIMIT 5
"""
df = spark.sql(query)

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ####Find the top 10 customers who have generated the highest revenue

# COMMAND ----------

query = """
SELECT
    c.customer_key,
    c.first_name,
    c.last_name,
    SUM(f.sales_amount) AS total_revenue
FROM gold.fact_sales AS f
LEFT JOIN gold.dim_customers AS c
    ON c.customer_key = f.customer_key
GROUP BY
    c.customer_key,
    c.first_name,
    c.last_name
ORDER BY total_revenue DESC
LIMIT 10
"""
df = spark.sql(query)

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ####The 3 customers with the fewest orders placed

# COMMAND ----------

query = """
SELECT
    c.customer_key,
    c.first_name,
    c.last_name,
    COUNT(DISTINCT order_number) AS total_orders
FROM gold.fact_sales AS f
LEFT JOIN gold.dim_customers AS c
    ON c.customer_key = f.customer_key
GROUP BY
    c.customer_key,
    c.first_name,
    c.last_name
ORDER BY total_orders
LIMIT 3
"""
df = spark.sql(query)

df.display()