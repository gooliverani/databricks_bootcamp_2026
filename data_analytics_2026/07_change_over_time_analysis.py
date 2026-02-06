# Databricks notebook source
# MAGIC %md
# MAGIC #Change Over Time Analysis
# MAGIC #####Purpose:
# MAGIC - To track trends, growth, and changes in key metrics over time.
# MAGIC - For time-series analysis and identifying seasonality.
# MAGIC - To measure growth or decline over specific periods.
# MAGIC 	
# MAGIC #####SQL Functions Used:
# MAGIC - Date Functions: DATEPART(), trunc(), date_format()
# MAGIC - Aggregate Functions: SUM(), COUNT(), AVG()
# MAGIC ##### Aggregating [Measure] By [Date Dimension]
# MAGIC - Total Sales By Year
# MAGIC - Average Cost By Month

# COMMAND ----------

# MAGIC %md
# MAGIC ###Analyse sales performance over time

# COMMAND ----------

# MAGIC %md
# MAGIC ####Quick Date Functions

# COMMAND ----------

query = """
SELECT
    YEAR(order_date) AS order_year,
    MONTH(order_date) AS order_month,
    SUM(sales_amount) as total_sales,
    COUNT(DISTINCT customer_key) AS total_customers,
    SUM(quantity) AS total_quantity
FROM gold.fact_sales
WHERE order_date IS NOT NULL
GROUP BY YEAR(order_date), MONTH(order_date)
ORDER BY YEAR(order_date), MONTH(order_date)
"""
df = spark.sql(query)

df.limit(10).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ####trunk()

# COMMAND ----------

query = """
SELECT
  trunc(order_date, 'MM') AS order_date,
  SUM(sales_amount) as total_sales,
  COUNT(DISTINCT customer_key) AS total_customers,
  SUM(quantity) AS total_quantity
FROM gold.fact_sales
WHERE order_date IS NOT NULL
GROUP BY trunc(order_date, 'MM')
ORDER BY trunc(order_date, 'MM')
"""
df = spark.sql(query)

df.limit(10).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ####date_format()

# COMMAND ----------

# DBTITLE 1,FORMAT()
from pyspark.sql.functions import date_format

query = """
SELECT
    trunc(order_date, 'MM') AS order_month,
    SUM(sales_amount) as total_sales,
    COUNT(DISTINCT customer_key) AS total_customers,
    SUM(quantity) AS total_quantity
FROM gold.fact_sales
WHERE order_date IS NOT NULL
GROUP BY trunc(order_date, 'MM')
ORDER BY trunc(order_date, 'MM')
"""
df = spark.sql(query)

df = df.withColumn('order_month_fmt', date_format(df.order_month, 'yyyy-MMM'))
df.limit(10).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ####How many new customers were added each year

# COMMAND ----------

# DBTITLE 1,Cell 10
query = """
SELECT
    trunc(create_date, 'YEAR') AS create_year,
    COUNT(customer_key) AS total_customers
FROM gold.dim_customers
GROUP BY trunc(create_date, 'YEAR')
ORDER BY trunc(create_date, 'YEAR')
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