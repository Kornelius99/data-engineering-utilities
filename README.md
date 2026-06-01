![Python](https://img.shields.io/badge/Python-Utilities-blue)
![PySpark](https://img.shields.io/badge/PySpark-Data_Engineering-orange)
![Airflow](https://img.shields.io/badge/Airflow-Orchestration-red)
![ETL](https://img.shields.io/badge/ETL-Framework-green)
![CI/CD](https://img.shields.io/badge/CI/CD-GitHub_Actions-black)

# Data Engineering Utilities

Reusable Python utilities for ETL logging, data quality validation, SQL review, PySpark schema validation, and Airflow ETL orchestration templates.

This repository demonstrates modular engineering utilities commonly used in modern Data Engineering and Cloud Analytics workflows.

---

## Overview

The goal of this project is to build reusable engineering components that can be integrated into:
- ETL pipelines
- Data platforms
- PySpark workflows
- Airflow orchestration
- Data quality frameworks
- Cloud analytics systems

Instead of writing one-off scripts, this repository focuses on reusable production-style utilities that support scalable engineering workflows.

---

## Project Status

✅ Active Engineering Utilities Repository  
✅ Modular Python Utilities  
✅ Data Quality Validation Framework  
✅ Reusable ETL Logging  
✅ Airflow DAG Templates  
✅ PySpark Validation Utilities  

---

## Utilities Included

### ETL Logger

Reusable logging utility for ETL pipelines.

Features:
- Centralized logging
- File-based logging
- Reusable configuration
- Pipeline monitoring support

Example:

```python
from etl_logger.logger import create_logger

logger = create_logger("my_pipeline")

logger.info("Pipeline started")
logger.error("Pipeline failed")
```

---

### Data Quality Checker

Validation helpers for:
- required columns,
- null checks,
- positive numeric checks,
- data quality enforcement.

Example:

```python
from data_quality.validation import (
    check_required_columns,
    check_nulls,
    check_positive_values
)

check_required_columns(df, ["order_id", "customer_id"])
check_nulls(df, ["order_id"])
check_positive_values(df, ["sales_amount"])
```

---

### SQL Query Checker

Basic SQL review automation utility.

Checks:
- SELECT * detection
- Missing WHERE clause detection
- Query review automation

Example:

```python
from sql_tools.query_checker import basic_sql_review

review = basic_sql_review(
    "SELECT * FROM sales"
)

print(review)
```

Example output:

```python
{
    "uses_select_star": True,
    "missing_where_clause": True
}
```

---

### Airflow DAG Template

Reusable Airflow ETL DAG template demonstrating:
- extract task
- transform task
- load task
- DAG orchestration

This template can be extended into production orchestration pipelines.

---

### PySpark Schema Validator

Reusable validation utilities for PySpark DataFrames.

Features:
- schema validation
- column validation
- reusable Spark quality checks

Example:

```python
from pyspark_utils.schema_validator import (
    validate_schema,
    compare_column_names
)
```

---

## Example Pipeline

The repository includes a sample ETL pipeline demonstrating how the utilities can be combined in real-world workflows.

Example:

```bash
python examples/sample_pipeline.py
```

This example demonstrates:
- logging,
- validation,
- reusable utility integration,
- pipeline execution flow.

---

## Repository Structure

```text
data-engineering-utilities/
│
├── etl_logger/
│   └── logger.py
│
├── data_quality/
│   └── validation.py
│
├── sql_tools/
│   └── query_checker.py
│
├── airflow_templates/
│   └── basic_etl_dag.py
│
├── pyspark_utils/
│   └── schema_validator.py
│
├── examples/
│   └── sample_pipeline.py
│
├── tests/
│
├── .github/workflows/
│
├── requirements.txt
└── README.md
```

---

## Tech Stack

- Python
- Pandas
- PySpark
- Apache Airflow
- Logging
- ETL Validation
- GitHub
- CI/CD Concepts

---

## Engineering Concepts Demonstrated

- Modular Python engineering
- Reusable utility development
- ETL framework design
- Data quality validation
- Logging & monitoring
- SQL automation
- Airflow orchestration
- PySpark validation workflows
- Production-style repository architecture

---

## Use Cases

These utilities can support:
- Data Engineering projects
- Cloud ETL workflows
- PySpark processing pipelines
- Airflow orchestration systems
- Analytics engineering workflows
- Data quality frameworks
- Enterprise reporting systems

---

## How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Example Pipeline

```bash
python examples/sample_pipeline.py
```

---

## Future Enhancements

- Great Expectations integration
- dbt utility templates
- Snowflake helper functions
- Databricks notebook templates
- Spark optimization utilities
- API ingestion utilities
- Kafka streaming helpers
- CI/CD automation workflows
- Unit test framework expansion

---

## Skills Demonstrated

- ETL Pipeline Engineering
- Python Engineering
- Data Quality Automation
- Airflow DAG Design
- PySpark Engineering
- Logging Frameworks
- Modular Architecture Design
- Reusable Engineering Components

---

## Related Projects

- Azure Data Platform
- AWS ETL Pipeline
- AQI Prediction Platform
- Healthcare FHIR Integration Pipeline

---

## Author

Korneli Pingula  
Senior Data Platform & Analytics Engineer

Specializing in:
- AWS
- Azure
- Databricks
- PySpark
- SQL
- Power BI
- Data Engineering
- Cloud Analytics

GitHub:
github.com/Kornelius99

LinkedIn:
linkedin.com/in/pingulakornelius
