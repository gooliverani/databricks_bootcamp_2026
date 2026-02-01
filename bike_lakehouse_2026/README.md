# Bike Lakehouse 2026

A Databricks Lakehouse project implementing the **Medallion Architecture** for bike data processing and analytics with automated pipeline orchestration.

## Project Structure

```
bike_lakehouse_2026/
├── bronze/                     # Raw data ingestion layer
│   └── bronze.ipynb           # Bronze layer data loading notebook
├── silver/                     # Cleaned and transformed data layer
│   ├── silver_orchestration.ipynb  # Silver layer orchestration notebook
│   ├── crm/                   # CRM system transformations
│   └── erp/                   # ERP system transformations
├── gold/                       # Aggregated business-level data layer
│   ├── gold_orchestration.ipynb    # Gold layer orchestration notebook
│   ├── gold_dim_customers.ipynb    # Customer dimension table
│   ├── gold_dim_products.ipynb     # Product dimension table
│   └── gold_fact_sales.ipynb       # Sales fact table
├── init_lakehouse.ipynb       # Initialization notebook for lakehouse setup
├── pipeline.json              # Databricks job configuration (JSON format)
├── pipeline.yaml              # Databricks job configuration (YAML format)
├── pipeline.py                # Databricks job configuration (Python SDK)
└── README.md
```

## Architecture Overview

This project follows the **Medallion Architecture** pattern with automated orchestration:

### 🥉 Bronze Layer
- Raw data ingestion from source systems (CRM and ERP)
- Data stored in its original format with minimal transformations
- Loads customer information, product details, and sales data from CSV files
- Serves as the single source of truth for raw data

### 🥈 Silver Layer
- Cleaned and validated data from multiple source systems
- **CRM Tables**: Customer info, product info, and sales details
- **ERP Tables**: Customer data, location, and product category information
- Data quality checks, deduplication, and standardization applied
- Orchestrated execution through `silver_orchestration.ipynb`

### 🥇 Gold Layer
- Business-level dimensional modeling with star schema design
- **Dimension Tables**:
  - `dim_customers`: Unified customer master data
  - `dim_products`: Product catalog with category hierarchy
- **Fact Tables**:
  - `fact_sales`: Sales transactions with foreign keys to dimensions
- Optimized for reporting, dashboards, and business intelligence
- Orchestrated execution through `gold_orchestration.ipynb`

## Pipeline Orchestration

The project includes automated Databricks job configurations in multiple formats:

### Pipeline Configuration Files
- **`pipeline.json`**: Native Databricks job definition
- **`pipeline.yaml`**: YAML format for easier version control and readability
- **`pipeline.py`**: Python SDK implementation for programmatic job management

### Pipeline Workflow
1. **Bronze Layer Task**: Ingests raw data from source files
2. **Silver Layer Task**: Executes after bronze completion, runs all silver transformations
3. **Gold Layer Task**: Executes after silver completion, builds dimensional model

### Pipeline Features
- **Scheduled Execution**: Runs daily (configurable interval)
- **Sequential Dependencies**: Each layer waits for the previous to complete
- **Performance Optimized**: Configured for optimal resource utilization
- **Queue Enabled**: Supports concurrent run queuing

## Getting Started

### Prerequisites
- Databricks workspace access
- Datasets included in repository volumes
- Appropriate permissions to create databases, tables, and jobs
- Databricks SDK 0.70.0 or higher (for Python pipeline deployment)

### Setup
1. Clone this repository to your Databricks workspace
2. Run `init_lakehouse.ipynb` to initialize the lakehouse infrastructure (databases, schemas, volumes)
3. Deploy the pipeline using one of the configuration files:
   - **Option A**: Import `pipeline.json` directly in Databricks Workflows UI
   - **Option B**: Deploy using Databricks Asset Bundles with `pipeline.yaml`
   - **Option C**: Run `pipeline.py` to create/update the job programmatically

### Manual Execution
If you prefer to run notebooks manually:
1. **Initialize**: Run `init_lakehouse.ipynb`
2. **Bronze**: Execute `bronze/bronze.ipynb`
3. **Silver**: Run `silver/silver_orchestration.ipynb`
4. **Gold**: Execute `gold/gold_orchestration.ipynb`

## Pipeline Deployment

### Using Python SDK
```python
# Install the Databricks SDK
%pip install --upgrade databricks-sdk==0.70.0

# Run the pipeline.py script to create or update the job
# Update the job_id in pipeline.py or use w.jobs.create() for new jobs
```

### Using Databricks CLI with YAML
```bash
# Deploy using Databricks Asset Bundles
databricks bundle deploy -t production
```

### Using Workflows UI
1. Navigate to Databricks Workflows
2. Click "Create Job"
3. Import the `pipeline.json` configuration
4. Adjust notebook paths to match your workspace location

## Data Flow

```
Source Systems (CSV) → Bronze Layer → Silver Layer → Gold Layer
                           ↓              ↓              ↓
                      Raw Tables    Cleansed Tables  Star Schema
                                                     (Dims & Facts)
```

## Contributing

1. Create a feature branch from `main`
2. Make your changes following the existing Medallion Architecture patterns
3. Test your notebooks in a development environment
4. Update pipeline configurations if adding new notebooks
5. Submit a pull request for review

## Notes

- Orchestration notebooks (`silver_orchestration.ipynb` and `gold_orchestration.ipynb`) use `dbutils.notebook.run()` to execute transformation notebooks in sequence
- The pipeline is configured to pause if any task fails (using `run_if: ALL_SUCCESS`)
- Performance target is set to `PERFORMANCE_OPTIMIZED` for faster execution
- Adjust notebook paths in pipeline configurations to match your workspace structure

## License

This project is part of the [Databricks Bootcamp 2026](https://github.com/DataWithBaraa/databricks_bootcamp_2026) by https://www.datawithbaraa.com/