# Bike Lakehouse 2026

A Databricks Lakehouse project implementing the **Medallion Architecture** for bike data processing and analytics.

## Project Structure

```
bike_lakehouse_2026/
├── bronze/              # Raw data ingestion layer
├── silver/              # Cleaned and transformed data layer
├── gold/                # Aggregated business-level data layer
├── init_lakehouse.ipynb # Initialization notebook for lakehouse setup
└── README.md
```

## Architecture Overview

This project follows the **Medallion Architecture** pattern:

### 🥉 Bronze Layer
- Raw data ingestion from source systems
- Data stored in its original format
- Minimal transformations applied
- Serves as the single source of truth for raw data

### 🥈 Silver Layer
- Cleaned and validated data
- Data quality checks and transformations applied
- Standardized schemas and data types
- Ready for analytics and reporting

### 🥇 Gold Layer
- Business-level aggregations
- Optimized for reporting and dashboards
- Domain-specific data models
- Ready for consumption by end users and applications

## Getting Started

### Prerequisites
- Databricks workspace access
- Datasets are included in this repository
- Appropriate permissions to create databases and tables

### Setup
1. Clone this repository to your Databricks workspace
2. Run `init_lakehouse.ipynb` to initialize the lakehouse infrastructure
3. Execute the bronze, silver, and gold layer notebooks in sequence

## Usage

1. **Initialize**: Run `init_lakehouse.ipynb` to set up the required databases, schemas, and storage locations
2. **Ingest**: Execute bronze layer notebooks to load raw data
3. **Transform**: Run silver layer notebooks to clean and standardize data
4. **Aggregate**: Execute gold layer notebooks to create business-ready datasets

## Contributing

1. Create a feature branch from `main`
2. Make your changes following the existing patterns
3. Test your notebooks in a development environment
4. Submit a pull request for review

## License

This project is part of the [Databricks Bootcamp 2026](https://github.com/DataWithBaraa/databricks_bootcamp_2026) by https://www.datawithbaraa.com/