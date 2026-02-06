# Databricks notebook source
# MAGIC %md
# MAGIC #Product Report
# MAGIC #####Purpose:
# MAGIC - This report consolidates key product metrics and behaviors.
# MAGIC 	
# MAGIC #####Highlights:
# MAGIC 1. Gathers essential fields such as product name, category, subcategory, and cost.
# MAGIC 2. Segments products by revenue to identify High-Performers, Mid-Range, or Low-Performers.
# MAGIC 3. Aggregates product-level metrics:
# MAGIC - total orders
# MAGIC - total sales
# MAGIC - total quantity sold
# MAGIC - total customers (unique)
# MAGIC - lifespan (in months)
# MAGIC 4. Calculates valuable KPIs:
# MAGIC - recency (months since last sale)
# MAGIC - average order revenue (AOR)
# MAGIC - average monthly revenue

# COMMAND ----------

# MAGIC %md
# MAGIC ####Create Report: gold.report_products

# COMMAND ----------

query = """
CREATE OR REPLACE VIEW gold.report_products AS

WITH base_query AS (
/*---------------------------------------------------------------------------
1) Base Query: Retrieves core columns from fact_sales and dim_products
---------------------------------------------------------------------------*/
    SELECT
	    f.order_number,
        f.order_date,
		f.customer_key,
        f.sales_amount,
        f.quantity,
        p.product_key,
        p.product_name,
        p.category,
        p.subcategory,
        p.product_cost
    FROM gold.fact_sales AS f
    LEFT JOIN gold.dim_products AS p
        ON f.product_key = p.product_key
    WHERE order_date IS NOT NULL  -- only consider valid sales dates
),

product_aggregations AS (
/*---------------------------------------------------------------------------
2) Product Aggregations: Summarizes key metrics at the product level
---------------------------------------------------------------------------*/
SELECT
    product_key,
    product_name,
    category,
    subcategory,
    product_cost,
    DATEDIFF(MONTH, MIN(order_date), MAX(order_date)) AS lifespan,
    MAX(order_date) AS last_sale_date,
    COUNT(DISTINCT order_number) AS total_orders,
	COUNT(DISTINCT customer_key) AS total_customers,
    SUM(sales_amount) AS total_sales,
    SUM(quantity) AS total_quantity,
	ROUND(AVG(CAST(sales_amount AS FLOAT) / NULLIF(quantity, 0)),0) AS avg_selling_price
FROM base_query

GROUP BY
    product_key,
    product_name,
    category,
    subcategory,
    product_cost
ORDER BY
    product_key,
    product_name,
    category,
    subcategory,
    product_cost
)

/*---------------------------------------------------------------------------
  3) Final Query: Combines all product results into one output
---------------------------------------------------------------------------*/
SELECT 
	product_key,
	product_name,
	category,
	subcategory,
	product_cost,
	last_sale_date,
	DATEDIFF(MONTH, last_sale_date, GETDATE()) AS recency_in_months,
	CASE
		WHEN total_sales > 50000 THEN 'High-Performer'
		WHEN total_sales >= 10000 THEN 'Mid-Range'
		ELSE 'Low-Performer'
	END AS product_segment,
	lifespan,
	total_orders,
	total_sales,
	total_quantity,
	total_customers,
	avg_selling_price,
	-- Average Order Revenue (AOR)
	CASE 
		WHEN total_orders = 0 THEN 0
		ELSE ROUND(total_sales / total_orders, 0)
	END AS avg_order_revenue,

	-- Average Monthly Revenue
	CASE
		WHEN lifespan = 0 THEN total_sales
		ELSE ROUND(total_sales / lifespan, 0)
	END AS avg_monthly_revenue

FROM product_aggregations 
"""
df = spark.sql(query)

df.display()

# COMMAND ----------

query = """
SELECT * FROM gold.report_products
"""
df = spark.sql(query)

df.display()