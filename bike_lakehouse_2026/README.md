# Bike Lakehouse 2026

A Databricks Lakehouse project implementing the **Medallion Architecture** for bike data processing and analytics with automated pipeline orchestration.

## Project Structure

```
bike_lakehouse_2026/
├── bronze/                     # Raw data ingestion layer
│   ├── bronze.ipynb           # Bronze layer data loading (manual approach)
│   └── bronze(improved).ipynb # Bronze layer data loading (configuration-driven approach)
├── silver/                     # Cleaned and transformed data layer
│   ├── silver_orchestration.ipynb  # Silver layer orchestration notebook
│   ├── quality_checks_silver.ipynb # Data quality validation notebook
│   ├── crm/                   # CRM system transformations
│   │   ├── silver_crm_cust_info.ipynb    # CRM customer information processing
│   │   ├── silver_crm_prd_info.ipynb     # CRM product information processing
│   │   └── silver_crm_sales_details.ipynb # CRM sales transactions processing
│   └── erp/                   # ERP system transformations
│       ├── silver_erp_cust_az12.ipynb    # ERP customer master data processing
│       ├── silver_erp_loc_a101.ipynb     # ERP location data processing
│       └── silver_erp_px_cat_g1v2.ipynb  # ERP product category processing
├── gold/                       # Aggregated business-level data layer
│   ├── gold_orchestration.ipynb    # Gold layer orchestration notebook
│   ├── gold_dim_customers.ipynb    # Customer dimension table
│   ├── gold_dim_products.ipynb     # Product dimension table
│   ├── gold_fact_sales.ipynb       # Sales fact table
│   └── quality_checks_gold.ipynb   # Gold layer quality validation
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

#### Bronze Layer Ingestion Options

The project provides **two approaches** for data ingestion into the Bronze layer:

**Option 1: Manual Approach (`bronze.ipynb`)**
- Individual code blocks for each CSV file
- Explicit file-by-file loading with separate write operations
- Best for: Learning, debugging, or when you need fine-grained control over each ingestion
- Example structure:
  ```python
  # Load cust_info.csv
  df = spark.read.option("header", "true").csv("path/to/file.csv")
  df.write.mode("overwrite").saveAsTable("workspace.bronze.table_name")
  ```

**Option 2: Configuration-Driven Approach (`bronze(improved).ipynb`)** ✨ *Recommended*
- Uses a centralized `INGESTION_CONFIG` list to define all source files
- Iterates through configuration with a loop for dynamic processing
- Best for: Production use, maintainability, and scalability
- Benefits:
  - Single source of configuration for all ingestion rules
  - Easy to add new files by updating the config list
  - Consistent error handling across all files
  - Less code duplication
- Example structure:
  ```python
  INGESTION_CONFIG = [
      {"source": "crm", "path": "/path/to/file.csv", "table": "table_name"},
      ...
  ]
  for item in INGESTION_CONFIG:
      df = spark.read.option("header", "true").csv(item["path"])
      df.write.mode("overwrite").saveAsTable(f"workspace.bronze.{item['table']}")
  ```

### 🥈 Silver Layer
- Cleaned and validated data from multiple source systems
- Organized by source system (CRM and ERP) for better maintainability
- **CRM Tables**: 
  - `silver.crm_customers` - Customer information (from `crm_cust_info`)
  - `silver.crm_products` - Product catalog (from `crm_prd_info`)
  - `silver.crm_sales` - Sales transactions (from `crm_sales_details`)
- **ERP Tables**: 
  - `silver.erp_customers` - Customer master data (from `erp_cust_az12`)
  - `silver.erp_customer_location` - Location data (from `erp_loc_a101`)
  - `silver.erp_product_category` - Product category hierarchy (from `erp_px_cat_g1v2`)
- Data quality checks, deduplication, and standardization applied
- Orchestrated execution through `silver_orchestration.ipynb`

#### Silver Layer Quality Checks
The `quality_checks_silver.ipynb` notebook validates data quality before promotion to Gold layer:
- **Data Integrity**: Null or duplicate primary keys detection
- **Data Cleansing**: Unwanted spaces in string fields
- **Data Standardization**: Consistency across related fields
- **Business Rules**: Invalid date ranges and logical constraints
- **Cross-field Validation**: Data consistency between related fields

> **Best Practice**: Run quality checks after each Silver layer execution to ensure data quality before promoting to Gold layer

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
1. **Bronze Layer Task**: Ingests raw data from source files (uses `bronze.ipynb` by default)
2. **Silver Layer Task**: Executes after bronze completion, runs all silver transformations
3. **Gold Layer Task**: Executes after silver completion, builds dimensional model

> **Note**: To use the improved bronze ingestion approach in your pipeline, update the notebook path in `pipeline.json`, `pipeline.yaml`, or `pipeline.py` to point to `bronze(improved).ipynb` instead of `bronze.ipynb`.

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
2. **Bronze**: Execute `bronze/bronze.ipynb` OR `bronze/bronze(improved).ipynb` (recommended)
3. **Silver**: Run `silver/silver_orchestration.ipynb`
4. **Quality Checks**: Execute `silver/quality_checks_silver.ipynb` to validate Silver data
5. **Gold**: Execute `gold/gold_orchestration.ipynb`

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
5. Optionally switch to `bronze(improved).ipynb` for the bronze task

## Data Flow

```
Source Systems (CSV) → Bronze Layer → Silver Layer → Gold Layer
                           ↓              ↓              ↓
                      Raw Tables    Cleansed Tables  Star Schema
                                    + Quality Checks  (Dims & Facts)
```

## Data Quality Framework

The project implements comprehensive data quality checks at the Silver layer to ensure data integrity before promotion to the Gold layer.

### Silver Layer Quality Checks
The `quality_checks_silver.ipynb` notebook performs validation across all Silver tables with four types of checks:

1. **Primary Key Integrity**: 
   - NULL value detection in primary key columns
   - Duplicate primary key identification
   - Ensures unique identifiers for all records

2. **String Data Quality**: 
   - Leading/trailing space detection in string fields
   - Formatting consistency checks
   - Prevents data quality issues in downstream processing

3. **Date Validation**: 
   - Invalid date range detection (e.g., future dates, unrealistic historical dates)
   - Temporal consistency validation (e.g., start_date < end_date)
   - Ensures business rule compliance for time-based data

4. **Cross-field Consistency**: 
   - Relationship validation between related fields
   - Referential integrity checks across tables
   - Logical consistency verification (e.g., quantity * price = total)

### Usage Instructions
Run `quality_checks_silver.ipynb` after Silver layer processing to validate data before Gold layer promotion. Investigate and resolve any discrepancies found during the checks.

## Best Practices

### Data Quality
- **Always run quality checks after Silver processing**: Execute `quality_checks_silver.ipynb` after each Silver layer execution to catch data issues early
- **Investigate violations promptly**: Review and resolve any quality check failures before proceeding to Gold layer processing
- **Document data quality issues**: Track recurring problems and implement preventive measures in upstream processes

### Orchestration
- **Use orchestration notebooks for sequential execution**: Leverage `silver_orchestration.ipynb` and `gold_orchestration.ipynb` to ensure proper execution order
- **Implement dependency management**: Configure tasks to run only after successful completion of prerequisites
- **Monitor pipeline execution**: Review logs and status regularly to identify and resolve issues quickly

### Bronze Ingestion
- **Use configuration-driven approach for production**: Prefer `bronze(improved).ipynb` over manual approach for maintainability and scalability
- **Centralize configuration**: Keep all ingestion rules in a single configuration structure
- **Implement consistent error handling**: Ensure all ingestion processes handle errors uniformly

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
- For production deployments, use `bronze(improved).ipynb` for more maintainable code
- Quality checks are implemented at the Silver layer to catch data issues before Gold processing
- The Silver layer is organized by source system (CRM and ERP) for better maintainability

## License

This project is part of the [Databricks Bootcamp 2026](https://github.com/DataWithBaraa/databricks_bootcamp_2026) by https://www.datawithbaraa.com/