from pyspark.sql.types import StructType


def validate_schema(dataframe, expected_schema: StructType):
    """
    Validate PySpark DataFrame schema.
    """

    actual_schema = dataframe.schema

    if actual_schema != expected_schema:
        raise ValueError(
            f"Schema mismatch.\nExpected: {expected_schema}\nActual: {actual_schema}"
        )

    return True


def compare_column_names(dataframe, expected_columns):
    """
    Validate DataFrame column names.
    """

    actual_columns = dataframe.columns

    missing_columns = [
        col for col in expected_columns
        if col not in actual_columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns detected: {missing_columns}"
        )

    return True