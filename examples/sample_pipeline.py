import pandas as pd

from etl_logger.logger import create_logger
from data_quality.validation import (
    check_required_columns,
    check_nulls,
    check_positive_values,
)


def run_sample_pipeline():
    logger = create_logger("sample_pipeline")

    logger.info("Starting sample ETL pipeline")

    df = pd.DataFrame({
        "order_id": [1, 2, 3],
        "customer_id": ["C001", "C002", "C003"],
        "total_amount": [100, 250, 300],
    })

    required_columns = ["order_id", "customer_id", "total_amount"]

    check_required_columns(df, required_columns)
    check_nulls(df, required_columns)
    check_positive_values(df, ["total_amount"])

    logger.info("Data quality checks passed")
    logger.info("Sample ETL pipeline completed successfully")

    print("Sample pipeline executed successfully")


if __name__ == "__main__":
    run_sample_pipeline()