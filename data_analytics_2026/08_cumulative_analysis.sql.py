# Databricks notebook source
# MAGIC %md
# MAGIC #Cumulative Analysis
# MAGIC #####Purpose:
# MAGIC - To calculate running totals or moving averages for key metrics.
# MAGIC - To track performance over time cumulatively.
# MAGIC - Useful for growth analysis or identifying long-term trends.
# MAGIC 	
# MAGIC #####SQL Functions Used:
# MAGIC - Window Functions: SUM() OVER(), AVG() OVER()
# MAGIC ##### Aggregating [Cumulative Measure] By [Date Dimension]
# MAGIC - Running Total Sales By Year
# MAGIC - Moving Average of Sales By Month

# COMMAND ----------

# MAGIC %md
# MAGIC ####Calculate the total sales per year and the running total of sales over time

# COMMAND ----------

query = """
SELECT
    order_date,
    total_sales,
SUM(total_sales) OVER (ORDER BY order_date) AS running_total_sales, -- window function
ROUND(AVG(avg_price) OVER (ORDER BY order_date), 0) AS moving_average_price  -- window function
FROM
(
    SELECT
        trunc(order_date, 'year') AS order_date,
        SUM(sales_amount) AS total_sales,
        AVG(price) AS avg_price
    FROM gold.fact_sales
    WHERE order_date IS NOT NULL
    GROUP BY trunc(order_date, 'year')
) AS t
"""
df = spark.sql(query)

df.display()

# COMMAND ----------

query = """

"""
df = spark.sql(query)

df.display()

# COMMAND ----------

query = """

"""
df = spark.sql(query)

df.display()

# COMMAND ----------

query = """

"""
df = spark.sql(query)

df.display()

# COMMAND ----------

query = """

"""
df = spark.sql(query)

df.display()