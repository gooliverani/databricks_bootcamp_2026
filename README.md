# Databricks Bootcamp 2026

A comprehensive, end-to-end Data Lakehouse learning repository featuring production-grade data engineering and analytics projects built on Databricks. This bootcamp covers the complete data lifecycle—from raw data ingestion through advanced business intelligence reporting—using industry-standard tools and architectural patterns.

[![Databricks](https://img.shields.io/badge/Databricks-Lakehouse-FF3621?logo=databricks)](https://databricks.com/)
[![Apache Spark](https://img.shields.io/badge/Apache%20Spark-3.x-E25A1C?logo=apache-spark)](https://spark.apache.org/)
[![Delta Lake](https://img.shields.io/badge/Delta%20Lake-Enabled-00ADD8)](https://delta.io/)
[![Python](https://img.shields.io/badge/Python-PySpark-3776AB?logo=python)](https://spark.apache.org/docs/latest/api/python/)

---

## 🎯 Project Overview

This repository is designed for aspiring and current data engineers looking to build real-world skills with the Databricks platform. It demonstrates:

- **Medallion Architecture** (Bronze → Silver → Gold) for data quality progression
- **ETL/ELT Pipeline Development** with orchestration and error handling
- **Data Quality Management** with automated validation checks
- **Business Intelligence & Analytics** using advanced SQL patterns
- **Production Best Practices** including configuration-driven development, modular code, and comprehensive documentation

**Perfect for:**
- 📚 Learning Databricks and modern data engineering
- 💼 Building a data engineering portfolio
- 🎤 Preparing for data engineering interviews
- 🛠️ Understanding real-world lakehouse implementations

---

## 📂 Repository Structure

```
databricks_bootcamp_2026/
│
├── bike_lakehouse_2026/          # ETL Pipeline & Medallion Architecture Project
│   ├── bronze/                   # Raw data ingestion layer
│   ├── silver/                   # Data cleaning & transformation layer
│   ├── gold/                     # Business-level aggregated data layer
│   ├── docs/                     # Architecture & design documentation
│   └── README.md                 # Detailed project documentation
│
├── data_analytics_2026/          # Business Intelligence & SQL Analytics Project
│   ├── 00-13 notebooks           # Progressive SQL analytics tutorials
│   └── README.md                 # Detailed analytics documentation
│
├── datasets/                     # Sample data files (CSV format)
│
├── LICENSE                       # MIT License
└── README.md                     # This file
```

---

## 🏗️ Projects

### 1. [Bike Lakehouse 2026](./bike_lakehouse_2026/)

**Focus:** Data Engineering, ETL Pipelines, Medallion Architecture

A production-ready lakehouse implementation demonstrating end-to-end data engineering workflows for a bike sales business. This project simulates integrating data from multiple source systems (CRM and ERP) and transforming it into analytics-ready datasets.

#### Key Features:
- ✅ **Medallion Architecture** implementation (Bronze, Silver, Gold layers)
- ✅ **Automated Pipeline Orchestration** using Databricks Jobs
- ✅ **Data Quality Checks** at Silver and Gold layers
- ✅ **Multi-Source Data Integration** (CRM + ERP systems)
- ✅ **Configuration-Driven Development** for scalability
- ✅ **Star Schema Design** (Fact & Dimension tables)
- ✅ **Multiple Pipeline Configuration Formats** (JSON, YAML, Python SDK)

#### Technologies:
- PySpark for data transformations
- Delta Lake for ACID transactions
- Databricks Workflows for orchestration
- Unity Catalog for data governance

#### What You'll Learn:
- Building scalable ETL pipelines
- Implementing data quality frameworks
- Designing dimensional data models
- Orchestrating multi-notebook workflows
- Managing lakehouse metadata and governance

[➡️ View Bike Lakehouse Project Details](./bike_lakehouse_2026/README.md)

---

### 2. [Data Analytics 2026](./data_analytics_2026/)

**Focus:** Business Intelligence, SQL Analytics, Data Analysis

A comprehensive SQL analytics module that leverages the Gold layer data from the Bike Lakehouse project. This project teaches advanced analytical patterns used by data analysts and analytics engineers in real business scenarios.

#### Key Features:
- ✅ **14 Progressive Analytics Notebooks** covering fundamental to advanced techniques
- ✅ **Window Functions & Aggregations** for complex calculations
- ✅ **Time-Series Analysis** (YoY growth, cohorts, trends)
- ✅ **Customer & Product Segmentation** using SQL
- ✅ **Business Reporting** with production-ready SQL queries
- ✅ **Analytical Patterns** for magnitude, ranking, contribution, and cumulative analysis

#### Technologies:
- Apache Spark SQL
- SQL Window Functions
- Aggregation & Analytical Functions
- Common Table Expressions (CTEs)

#### What You'll Learn:
- Advanced SQL analytical techniques
- Building business intelligence reports
- Cohort and growth analysis
- Customer segmentation strategies
- Data-driven decision making

[➡️ View Data Analytics Project Details](./data_analytics_2026/README.md)

---

## 🚀 Getting Started

### Prerequisites

- **Databricks Account** (Community Edition or workspace access)
- **Basic Knowledge Of:**
  - Python fundamentals
  - SQL basics
  - Data warehousing concepts (helpful but not required)

### Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/gooliverani/databricks_bootcamp_2026.git
   ```

2. **Upload to Databricks:**
   - Navigate to your Databricks workspace
   - Go to **Workspace** → **Users** → [Your User]
   - Click **Import** and select the repository folder
   - Choose **Import as Git folder** or upload individual notebooks

3. **Initialize the Lakehouse:**
   - Open `bike_lakehouse_2026/init_lakehouse.ipynb`
   - Run all cells to set up databases and schemas
   - This creates the necessary Unity Catalog structures

4. **Load Sample Data:**
   - Upload CSV files from `datasets/` to Databricks DBFS or cloud storage
   - Update file paths in Bronze layer notebooks to match your storage location

5. **Run the Pipeline:**
   - **Manual Execution:** Run notebooks sequentially (Bronze → Silver → Gold)
   - **Automated Execution:** Use the provided `pipeline.json`, `pipeline.yaml`, or `pipeline.py` to create a Databricks Job

6. **Explore Analytics:**
   - After Gold layer is populated, open `data_analytics_2026/` notebooks
   - Run analytics notebooks sequentially to learn SQL patterns

---

## 📚 Learning Path

### **Recommended Order:**

| Step | Project | Focus Area | Time Estimate |
|------|---------|------------|---------------|
| 1️⃣ | Bike Lakehouse - Bronze Layer | Raw data ingestion | 2-3 hours |
| 2️⃣ | Bike Lakehouse - Silver Layer | Data cleaning & transformation | 4-6 hours |
| 3️⃣ | Bike Lakehouse - Gold Layer | Dimensional modeling | 3-4 hours |
| 4️⃣ | Bike Lakehouse - Orchestration | Pipeline automation | 2-3 hours |
| 5️⃣ | Data Analytics - Foundations | SQL basics & exploration | 2-3 hours |
| 6️⃣ | Data Analytics - Advanced | Analytical patterns | 6-8 hours |
| 7️⃣ | Data Analytics - Reporting | Business intelligence | 3-4 hours |

**Total Learning Time:** ~25-35 hours

---

## 🛠️ Key Concepts Covered

### Data Engineering Concepts:
- Medallion Architecture (Bronze, Silver, Gold)
- ETL vs ELT patterns
- Data quality and validation frameworks
- Incremental data processing
- Pipeline orchestration and scheduling
- Error handling and logging
- Configuration-driven development
- Star schema dimensional modeling

### Analytics Concepts:
- Dimensional vs measure analysis
- Magnitude, ranking, and contribution analysis
- Time-series and trend analysis
- Cohort analysis
- Customer segmentation
- Year-over-year growth calculations
- Cumulative metrics and moving averages
- Business reporting best practices

### Databricks Technologies:
- PySpark DataFrames and SQL
- Delta Lake and ACID transactions
- Databricks Workflows and Jobs
- Unity Catalog for governance
- Databricks notebooks and widgets
- DBFS and cloud storage integration

---

## 📖 Documentation

Each project includes comprehensive documentation:

- **[Bike Lakehouse README](./bike_lakehouse_2026/README.md)** - ETL pipeline architecture, layer details, orchestration guide
- **[Data Analytics README](./data_analytics_2026/README.md)** - Analytics patterns, SQL techniques, notebook descriptions

---

## 🎯 Use Cases & Applications

This bootcamp prepares you for real-world scenarios including:

- Building enterprise data lakes and lakehouses
- Implementing data quality frameworks
- Creating automated ETL/ELT pipelines
- Designing dimensional data models for analytics
- Developing business intelligence reports
- Performing customer and product analytics
- Conducting cohort and growth analysis

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve the bootcamp:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

---

## 🙋 Support & Questions

- **Issues:** Open an issue on GitHub for bugs or feature requests
- **Discussions:** Use GitHub Discussions for questions and community interaction
- **Author:** [@gooliverani](https://github.com/gooliverani)

---

## 🌟 Acknowledgments

This project is part of the comprehensive **Databricks Bootcamp 2026** course by **DataWithBaraa**. Special thanks to Baraa for creating excellent educational content on data engineering, analytics, SQL, and Databricks!

**Connect with DataWithBaraa:**
- 🎥 [YouTube Channel](https://www.youtube.com/@DataWithBaraa)
- 🌐 [Website](https://www.datawithbaraa.com/)
- 💻 [GitHub](https://github.com/DataWithBaraa)

---

## 🔗 Useful Resources

- [Databricks Documentation](https://docs.databricks.com/)
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [Delta Lake Documentation](https://docs.delta.io/)
- [Medallion Architecture Guide](https://www.databricks.com/glossary/medallion-architecture)

---

**⭐ If you find this bootcamp helpful, please star the repository!**