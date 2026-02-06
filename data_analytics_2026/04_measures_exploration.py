# Databricks notebook source
# MAGIC %md
# MAGIC #Measures Exploration (Key Metrics)
# MAGIC #####Purpose:
# MAGIC - To calculate aggregated metrics (e.g., totals, averages) for quick insights.
# MAGIC - To identify overall trends or spot anomalies.
# MAGIC 	
# MAGIC #####SQL Functions Used:
# MAGIC - COUNT(), SUM(), AVG()

# COMMAND ----------

# MAGIC %md
# MAGIC ####Find the Total Sales

# COMMAND ----------

query = """
SELECT SUM(sales_amount) AS total_sales FROM gold.fact_sales
"""
df = spark.sql(query)

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ####Find how many items are sold

# COMMAND ----------

query = """
SELECT SUM(quantity) AS total_quantity FROM gold.fact_sales
"""
df = spark.sql(query)

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ####Find the average selling price

# COMMAND ----------

query = """
SELECT ROUND(AVG(price), 0) AS avg_price FROM gold.fact_sales
"""
df = spark.sql(query)

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ####Find the Total number of Orders

# COMMAND ----------

query = """
SELECT COUNT(order_number) AS total_orders FROM gold.fact_sales
"""
df = spark.sql(query)

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ##### - First eliminate duplicates then count Orders

# COMMAND ----------

query = """
SELECT COUNT(DISTINCT order_number) AS total_orders FROM gold.fact_sales
"""
df = spark.sql(query)

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Find orders with more than one item

# COMMAND ----------

# DBTITLE 1,Query orders with more than one item
query = """
SELECT * FROM gold.fact_sales
WHERE order_number IN (
    SELECT order_number FROM gold.fact_sales
    GROUP BY order_number
    HAVING COUNT(*) > 1
)
"""
df = spark.sql(query)

df.limit(10).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ####Find the total number of products

# COMMAND ----------

query = """
SELECT COUNT(product_key) AS total_products FROM gold.dim_products
"""
df = spark.sql(query)

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###### - Always check if numbers are the same

# COMMAND ----------

query = """
SELECT COUNT(DISTINCT product_key) AS total_products FROM gold.dim_products
"""
df = spark.sql(query)

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ####Find the total number of customers

# COMMAND ----------

query = """
SELECT COUNT(customer_key) AS total_customers FROM gold.dim_customers
"""
df = spark.sql(query)

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ####Find the total number of customers that has placed an order 
# MAGIC   - There can be some customers that just registered without placing order

# COMMAND ----------

query = """
SELECT COUNT(DISTINCT customer_key) AS total_customers FROM gold.fact_sales
"""
df = spark.sql(query)

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ####Generate a Report that shows all key metrics of the business (Big numbers)

# COMMAND ----------

query = """
SELECT 'Total Sales' AS measure_name, SUM(sales_amount) AS measure_value FROM gold.fact_sales
UNION ALL
SELECT 'Total Quantity' AS measure_name, SUM(quantity) AS measure_value FROM gold.fact_sales
UNION ALL
SELECT 'Average Price', ROUND(AVG(price), 0) FROM gold.fact_sales
UNION ALL
SELECT 'Total Orders', COUNT(DISTINCT order_number) FROM gold.fact_sales
UNION ALL
SELECT 'Total Products', COUNT(DISTINCT product_name) FROM gold.dim_products
UNION ALL
SELECT 'Total Customers', COUNT(customer_key) FROM gold.dim_customers
"""
df = spark.sql(query)

df.display()