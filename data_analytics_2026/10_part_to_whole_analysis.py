# Databricks notebook source
# MAGIC %md
# MAGIC #Part-to-Whole Analysis
# MAGIC #####Purpose:
# MAGIC - To compare performance or metrics across dimensions or time periods.
# MAGIC - To evaluate differences between categories.
# MAGIC - Useful for A/B testing or regional comparisons.
# MAGIC 	
# MAGIC #####SQL Functions Used:
# MAGIC - SUM(), AVG(): Aggregates values for comparison.
# MAGIC - Window Functions: SUM() OVER() for total calculations.
# MAGIC ##### ([Measure] / Total [Measure]) * 100 By [Dimension] (to get %)
# MAGIC - (Sales / Total Sales) * 100 By Category
# MAGIC - (Quantity / Total Quantity) * 100 By Country

# COMMAND ----------

# MAGIC %md
# MAGIC ####Which categories contribute the most to overall sales?

# COMMAND ----------

query = """
-- CTE
WITH category_sales AS (
    SELECT
        p.category,
        SUM(f.sales_amount) AS total_sales
    FROM gold.fact_sales AS f
    LEFT JOIN gold.dim_products AS p
        ON p.product_key = f.product_key
    GROUP BY category
)
SELECT
    category,
    total_sales,
    SUM(total_sales) OVER () AS overall_sales,
    CONCAT(ROUND((CAST (total_sales AS FLOAT) / SUM(total_sales) OVER ()) * 100, 2), '%') AS percentage_of_total
FROM category_sales
ORDER BY total_sales DESC
"""
df = spark.sql(query)

df.display()