# Databricks notebook source
# MAGIC %md
# MAGIC #Dimensions Exploration
# MAGIC #####Purpose:
# MAGIC - To explore the structure of dimension tables.
# MAGIC 	
# MAGIC #####SQL Functions Used:
# MAGIC - DISTINCT
# MAGIC - ORDER BY

# COMMAND ----------

# MAGIC %md
# MAGIC ####Retrieve a list of unique countries from which customers originate

# COMMAND ----------

query = """
SELECT DISTINCT 
    country 
FROM gold.dim_customers
ORDER BY country
"""
df = spark.sql(query)

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ####Retrieve a list of unique categories, subcategories, and products

# COMMAND ----------

query = """
SELECT DISTINCT 
    category, 
    subcategory, 
    product_name
FROM gold.dim_products
ORDER BY category, subcategory, product_name
"""
df = spark.sql(query)

df.limit(10).display()