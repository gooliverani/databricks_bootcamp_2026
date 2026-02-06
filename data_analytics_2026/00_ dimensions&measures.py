# Databricks notebook source
# MAGIC %md
# MAGIC #Dimensions & Measures

# COMMAND ----------

# MAGIC %md
# MAGIC ####Retrieve a list of unique categories of products
# MAGIC - ##### Dimension (Make no sense to aggregate)

# COMMAND ----------

query = """
SELECT DISTINCT
    category
FROM gold.dim_products
"""
df = spark.sql(query)

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ####Retrieve a list of unique sales amount
# MAGIC - ##### Measure (Make sense to aggregate)

# COMMAND ----------

query = """
SELECT DISTINCT
    sales_amount
FROM gold.fact_sales
"""
df = spark.sql(query)

df.limit(5).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ####Retrieve a list of unique product names
# MAGIC - ##### Dimension (Make no sense to aggregate)

# COMMAND ----------

query = """
SELECT DISTINCT
    product_name
FROM gold.dim_products
"""
df = spark.sql(query)

df.limit(5).display()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Retrieve a list of unique quantity of sales
# MAGIC - ##### Measure (Make sense to aggregate)

# COMMAND ----------

query = """
SELECT DISTINCT
    quantity
FROM gold.fact_sales
"""
df = spark.sql(query)

df.limit(5).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ####'birthdate' is Dimension (Make no sense to aggregate)
# MAGIC ####But when you calculate the age from the 'birthdate' it's Measure
# MAGIC - ##### Measure (Make sense to aggregate)

# COMMAND ----------

query = """
SELECT DISTINCT
    ROUND(AVG(DATEDIFF(year, birthdate, GETDATE())), 0) AS Avg_Age
FROM gold.dim_customers
"""
df = spark.sql(query)

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ####Retrieve a list of unique customer id's
# MAGIC - ##### Dimension (Make no sense to aggregate)

# COMMAND ----------

query = """
SELECT DISTINCT
    customer_id
FROM gold.dim_customers
"""
df = spark.sql(query)

df.limit(5).display()