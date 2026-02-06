# Databricks notebook source
# MAGIC %md
# MAGIC #Database Exploration
# MAGIC #####Purpose:
# MAGIC - To explore the structure of the database, including the list of tables and their schemas.
# MAGIC - To inspect the columns and metadata for specific tables.
# MAGIC
# MAGIC #####Table Used:
# MAGIC - INFORMATION_SCHEMA.TABLES
# MAGIC - INFORMATION_SCHEMA.COLUMNS

# COMMAND ----------

# MAGIC %md
# MAGIC ####Retrieve a list of all tables in the database

# COMMAND ----------

# DBTITLE 1,Retrieve all tables in database
query = """
SELECT 
    TABLE_CATALOG, 
    TABLE_SCHEMA, 
    TABLE_NAME, 
    TABLE_TYPE
FROM information_schema.tables
"""
df = spark.sql(query)

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ####Retrieve all columns for a specific table (dim_customers)

# COMMAND ----------

query = """
SELECT 
    COLUMN_NAME, 
    DATA_TYPE, 
    IS_NULLABLE, 
    CHARACTER_MAXIMUM_LENGTH
FROM information_schema.columns
WHERE TABLE_NAME = 'dim_customers'
"""
df = spark.sql(query)

df.display()