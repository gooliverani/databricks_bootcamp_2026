# Databricks notebook source
# MAGIC %md
# MAGIC #Date Range Exploration
# MAGIC #####Purpose:
# MAGIC - To determine the temporal boundaries of key data points.
# MAGIC - To understand the range of historical data.
# MAGIC 	
# MAGIC #####SQL Functions Used:
# MAGIC - MIN(), MAX(), DATEDIFF()

# COMMAND ----------

# MAGIC %md
# MAGIC ####Find the date of the first and last order
# MAGIC ####How many years of sales are avaiable

# COMMAND ----------

query = """
SELECT
    MIN(order_date) AS first_order_date,
    MAX(order_date) AS last_order_date,
    DATEDIFF(year, MIN(order_date), MAX(order_date)) AS order_range_year
FROM gold.fact_sales
"""
df = spark.sql(query)

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ####Determine the first and last order date and the total duration in months

# COMMAND ----------

query = """
SELECT
    MIN(order_date) AS first_order_date,
    MAX(order_date) AS last_order_date,
    DATEDIFF(month, MIN(order_date), MAX(order_date)) AS order_range_month
FROM gold.fact_sales
"""
df = spark.sql(query)

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ####Find the youngest and oldest customer based on birthdate

# COMMAND ----------

query = """
SELECT
    MIN(birthdate) AS oldest_birthdate,
    DATEDIFF(year, MIN(birthdate), GETDATE()) AS oldest_age,
    MAX(birthdate) AS youngest_birthdate,
    DATEDIFF(year, MAX(birthdate), GETDATE()) AS youngest_age
FROM gold.dim_customers
"""
df = spark.sql(query)

df.display()