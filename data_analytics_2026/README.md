# Data Analytics 2026

A comprehensive SQL-based data analytics project focused on business intelligence techniques and analytical patterns using Databricks and Apache Spark SQL.

> **📝 Note**: This project is a continuation of the [**Bike Lakehouse 2026**](../bike_lakehouse_2026/README.md) module from the `databricks_bootcamp_2026` repository. While the Bike Lakehouse project focused on ETL pipeline development and Medallion Architecture, this module emphasizes analytical SQL techniques and business intelligence reporting using the Gold layer data.

---

## 📚 Project Overview

This module provides hands-on experience with advanced SQL analytics patterns commonly used in business intelligence and data analysis. Each notebook demonstrates a specific analytical technique applied to the bike sales dataset established in the Bike Lakehouse project.

### Learning Objectives

- Master SQL analytical patterns for business intelligence
- Understand when and how to apply different analysis types
- Build production-ready analytical reports
- Develop proficiency with window functions, aggregations, and segmentation
- Create actionable insights from dimensional data models

---

## 📂 Project Structure

```
data_analytics_2026/
├── 00_ dimensions&measures.ipynb           # Foundational concepts: dimensions vs measures
├── 01_database_exploration.ipynb           # Database schema and metadata exploration
├── 02_dimensions_exploration.ipynb         # Dimension table analysis techniques
├── 03_date_range_exploration.ipynb         # Temporal boundary analysis
├── 04_measures_exploration.ipynb           # Key performance metrics calculation
├── 05_magnitude_analysis.ipynb             # Data quantification by dimensions
├── 06_ranking_analysis.ipynb               # Performance ranking techniques
├── 07_contribution_analysis.ipynb          # Percentage contribution calculations
├── 08_cumulative_analysis.sql.ipynb        # Running totals and moving averages
├── 09_growth_analysis.ipynb                # Year-over-year growth metrics
├── 10_cohort_analysis.ipynb                # Time-based cohort analysis
├── 11_data_segmentation..ipynb             # Customer and product segmentation
├── 12_report_customers.ipynb               # Customer analytics report
└── 13_report_products.ipynb                # Product performance report
```

---

## 🎓 Module Contents

### Foundation Concepts

#### **00. Dimensions & Measures**
- Understanding the difference between dimensions and measures
- When to aggregate vs when to filter
- Building blocks of analytical queries

#### **01. Database Exploration**
- **Purpose**: Explore database structure, tables, and schemas
- **Techniques**: 
  - Using `INFORMATION_SCHEMA.TABLES` for metadata discovery
  - Inspecting table columns and data types
  - Understanding data relationships
- **Best For**: Initial data discovery and documentation

---

### Exploration Techniques

#### **02. Dimensions Exploration**
- **Purpose**: Analyze categorical data and unique values
- **SQL Functions**: `DISTINCT`, `ORDER BY`
- **Use Cases**: 
  - Identifying unique countries, categories, or customer segments
  - Understanding data cardinality
  - Validating dimension table completeness

#### **03. Date Range Exploration**
- **Purpose**: Determine temporal boundaries of datasets
- **SQL Functions**: `MIN()`, `MAX()`, `DATEDIFF()`
- **Insights Provided**:
  - First and last transaction dates
  - Data coverage period (e.g., "3 years of sales data")
  - Identifying data gaps

#### **04. Measures Exploration (Key Metrics)**
- **Purpose**: Calculate high-level aggregated metrics
- **SQL Functions**: `COUNT()`, `SUM()`, `AVG()`
- **Common Metrics**:
  - Total sales revenue
  - Average order value
  - Total number of customers/products/transactions
- **Value**: Quick snapshot of business performance

---

### Core Analytical Patterns

#### **05. Magnitude Analysis**
- **Purpose**: Quantify data grouped by specific dimensions
- **Pattern**: `Aggregated [Measure] BY [Dimension]`
- **SQL Functions**: `SUM()`, `COUNT()`, `AVG()`, `GROUP BY`, `ORDER BY`
- **Examples**:
  - Total Sales by Country
  - Total Quantity by Product Category
  - Average Order Value by Customer
  - Total Orders by Month
- **Business Value**: Understand distribution and identify high-impact segments

#### **06. Ranking Analysis**
- **Purpose**: Rank items based on performance metrics
- **Pattern**: `Rank [Dimension] BY Aggregated [Measure]`
- **SQL Functions**: `RANK()`, `DENSE_RANK()`, `ROW_NUMBER()`, `TOP`
- **Examples**:
  - Top 5 Products by Revenue
  - Bottom 3 Customers by Order Count
  - Rank Countries by Total Sales
- **Business Value**: Identify top performers and underperformers for strategic focus

#### **07. Contribution Analysis**
- **Purpose**: Calculate percentage contribution of parts to the whole
- **Pattern**: `[Dimension] Contribution to Total [Measure]`
- **SQL Techniques**: Percentage calculations with window functions
- **Examples**:
  - Product category contribution to total revenue
  - Country-wise sales share
  - Customer segment revenue mix
- **Business Value**: Portfolio analysis and resource allocation decisions

#### **08. Cumulative Analysis**
- **Purpose**: Track performance over time cumulatively
- **Pattern**: `Aggregating [Cumulative Measure] BY [Date Dimension]`
- **SQL Functions**: `SUM() OVER()`, `AVG() OVER()` with window frames
- **Examples**:
  - Running Total Sales by Year
  - Moving Average of Sales by Month
  - Cumulative Customer Acquisition
- **Business Value**: Growth trajectory visualization and trend identification

#### **09. Growth Analysis**
- **Purpose**: Measure period-over-period changes
- **Pattern**: `[Measure] Growth Between [Time Period A] and [Time Period B]`
- **SQL Techniques**: `LAG()`, `LEAD()`, percentage change calculations
- **Examples**:
  - Year-over-year revenue growth
  - Month-over-month sales change
  - Product category growth rate
- **Business Value**: Identify growth trends and acceleration/deceleration patterns

#### **10. Cohort Analysis**
- **Purpose**: Analyze behavior of groups over time
- **Pattern**: `[Measure] BY [Cohort] OVER [Time Period]`
- **SQL Techniques**: Date-based grouping, retention calculations
- **Examples**:
  - Customer retention by signup month
  - Product performance by launch quarter
  - Sales behavior by customer acquisition cohort
- **Business Value**: Understanding long-term customer/product behavior patterns

#### **11. Data Segmentation**
- **Purpose**: Group data into meaningful categories for targeted insights
- **Pattern**: `[Measure] BY [Measure]` (with custom logic)
- **SQL Functions**: `CASE` statements, `GROUP BY`
- **Examples**:
  - Customers by Age Range (18-25, 26-35, etc.)
  - Products by Sales Performance (High/Medium/Low)
  - Orders by Size (Small/Medium/Large)
- **Business Value**: Targeted marketing, personalization, and strategic decision-making

---

### Production Reports

#### **12. Customer Report** (`report_customers.ipynb`)
A comprehensive customer analytics dashboard consolidating:
- Customer demographics and profile information
- Behavioral segmentation (High-Value, Regular, Occasional, At-Risk)
- Aggregated metrics:
  - Total orders per customer
  - Total spend (lifetime value)
  - Average order value
  - Customer lifespan (months active)
- Key Performance Indicators:
  - Recency (months since last purchase)
  - Frequency (orders per month)
  - Monetary value (average monthly spend)
- **RFM Analysis Ready**: Structured for Recency, Frequency, Monetary segmentation

#### **13. Product Report** (`report_products.ipynb`)
A comprehensive product performance report featuring:
- Product catalog details (name, category, subcategory, cost)
- Revenue-based segmentation (High-Performers, Mid-Range, Low-Performers)
- Aggregated product-level metrics:
  - Total orders
  - Total sales revenue
  - Total quantity sold
  - Total unique customers
  - Product lifespan (months in market)
- Calculated KPIs:
  - Recency (months since last sale)
  - Average Order Revenue (AOR)
  - Average Monthly Revenue
- **Strategic Value**: Product portfolio optimization, inventory planning, and sunset decisions

---

## 🚀 Getting Started

### Prerequisites
- Completed setup from [**Bike Lakehouse 2026**](../bike_lakehouse_2026/README.md)
- Access to the Gold layer dimensional model:
  - `gold.dim_customers` - Customer dimension
  - `gold.dim_products` - Product dimension
  - `gold.fact_sales` - Sales fact table
- Databricks workspace with SQL capabilities
- Basic SQL knowledge recommended

### Setup Instructions

1. **Ensure Gold Layer is Available**
   ```sql
   -- Verify Gold layer tables exist
   SHOW TABLES IN gold;
   ```

2. **Run Notebooks in Sequence**
   - Start with `00_dimensions&measures.ipynb` to understand core concepts
   - Progress through exploration notebooks (01-04)
   - Study analytical pattern notebooks (05-11)
   - Review production reports (12-13)

3. **Experimentation Encouraged**
   - Modify queries to explore different dimensions
   - Create your own variations of analysis patterns
   - Combine techniques from multiple notebooks

---

## 📊 Analysis Patterns Quick Reference

| Analysis Type | When to Use | Key SQL Functions | Output Example |
|--------------|-------------|-------------------|----------------|
| **Magnitude** | Understand distribution across categories | `SUM()`, `COUNT()`, `GROUP BY` | "Sales by Country" |
| **Ranking** | Identify top/bottom performers | `RANK()`, `ROW_NUMBER()`, `TOP` | "Top 5 Products by Revenue" |
| **Contribution** | Calculate percentage shares | Window functions, division | "Product X = 23% of revenue" |
| **Cumulative** | Track running totals over time | `SUM() OVER()`, `AVG() OVER()` | "YTD Sales Trend" |
| **Growth** | Measure period-over-period change | `LAG()`, `LEAD()`, `%` calc | "15% YoY growth" |
| **Cohort** | Analyze groups over time | Date grouping, retention | "2023 Q1 cohort retention" |
| **Segmentation** | Create custom categories | `CASE`, `GROUP BY` | "Customers by Age Range" |

---

## 🎯 Key Learning Outcomes

By completing this module, you will be able to:

✅ **Foundational Skills**
- Distinguish between dimensions and measures
- Explore database schemas and understand data relationships
- Identify temporal boundaries and data coverage

✅ **Analytical Techniques**
- Apply 7 core analytical patterns to real-world business questions
- Use window functions for advanced aggregations
- Build ranking and contribution analyses
- Calculate cumulative metrics and growth rates
- Perform cohort and segmentation analysis

✅ **Business Intelligence**
- Create production-ready customer and product reports
- Structure data for RFM (Recency, Frequency, Monetary) analysis
- Generate actionable insights from dimensional models
- Communicate findings through well-structured SQL reports

✅ **Best Practices**
- Write maintainable and performant SQL queries
- Choose appropriate analysis patterns for business questions
- Document analytical logic clearly
- Design reports that support decision-making

---

## 🔗 Integration with Bike Lakehouse

This module **extends** the Bike Lakehouse 2026 project by:

```
Bike Lakehouse 2026              →    Data Analytics 2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    ━━━━━━━━━━━━━━━━━━━━━━━━━
Bronze → Silver → Gold Tables     →    SQL Analytics Patterns
(Data Engineering Focus)          →    (Business Intelligence Focus)

Gold Layer Output:                     Analytics Input:
├── dim_customers                 →    Customer Reports
├── dim_products                  →    Product Reports  
└── fact_sales                    →    Sales Analysis
```

### Data Flow
1. **Bike Lakehouse** processes raw data through Bronze → Silver → Gold
2. **Data Analytics** consumes Gold layer tables for analysis
3. Reports and insights feed back into business decision-making

---

## 📖 Recommended Learning Path

### For Beginners
1. Start with **00-04**: Build foundational understanding
2. Focus on **05 (Magnitude)** and **06 (Ranking)**: Master basic aggregations
3. Review **12-13**: See how patterns combine in production reports
4. Experiment with variations on simpler patterns

### For Intermediate Users
1. Quick review of **00-01**: Refresh core concepts
2. Deep dive into **07-10**: Advanced analytical patterns
3. Study **11**: Segmentation for customer analytics
4. Customize **12-13**: Adapt reports for your use cases

### For Advanced Users
1. Combine multiple patterns into complex analyses
2. Optimize query performance for large datasets
3. Create new analytical patterns not covered
4. Build additional production reports using the framework

---

## 🛠️ Technologies Used

- **Apache Spark SQL**: Primary query engine
- **Databricks Notebooks**: Interactive development environment
- **Delta Lake Tables**: Gold layer dimensional model from Bike Lakehouse
- **Window Functions**: Advanced analytical capabilities
- **Common Table Expressions (CTEs)**: Query organization and readability

---

## 📝 Best Practices

### Query Performance
- **Use appropriate filters**: Limit data scanned with `WHERE` clauses
- **Partition awareness**: Leverage date partitioning in fact tables
- **Aggregation strategy**: Pre-aggregate when possible
- **Index utilization**: Ensure dimension keys are optimized

### Code Quality
- **Clear naming**: Use descriptive aliases for measures and dimensions
- **Comments**: Explain complex business logic
- **CTEs for readability**: Break complex queries into logical steps
- **Consistent formatting**: Follow SQL style guidelines

### Analytical Rigor
- **Validate assumptions**: Check for NULL values and data quality issues
- **Understand context**: Know the business meaning of each metric
- **Cross-reference**: Validate totals across different aggregations
- **Document limitations**: Note any data gaps or known issues

---

## 🙏 Acknowledgments

This project is part of the comprehensive **Databricks Bootcamp 2026** course by **DataWithBaraa**. Special thanks to Baraa for creating excellent educational content on data analytics, SQL, and Databricks!

**Connect with DataWithBaraa:**
- 🎥 [YouTube Channel](https://www.youtube.com/@DataWithBaraa)
- 🌐 [Website](https://www.datawithbaraa.com/)
- 💻 [GitHub](https://github.com/DataWithBaraa)

---

## 📧 Contact

For questions, suggestions, or contributions:
- **Open an issue** in this repository
- **Fork and submit a pull request** with improvements
- **Share your own analytical patterns** built using this framework

---

## 🔗 Related Projects

- **[Bike Lakehouse 2026](../bike_lakehouse_2026/README.md)**: Data engineering foundation (Bronze → Silver → Gold)
- **Databricks Bootcamp 2026**: Complete bootcamp curriculum

---

## 📄 License

This project is part of educational content. Please refer to the repository license for usage terms.

---

**⭐ If you find this project helpful for learning SQL analytics, please consider giving it a star!**

---

## 🗺️ Quick Navigation

| Section | Link |
|---------|------|
| Project Overview | [↑ Top](#data-analytics-2026) |
| Module Contents | [📚 Jump](#-module-contents) |
| Analysis Patterns | [📊 Reference](#-analysis-patterns-quick-reference) |
| Getting Started | [🚀 Setup](#-getting-started) |
| Learning Path | [📖 Guide](#-recommended-learning-path) |
| Acknowledgments | [🙏 Credits](#-acknowledgments) |
