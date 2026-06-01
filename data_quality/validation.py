def check_required_columns(df, required_columns):
    """
    Validate that all required columns exist in a DataFrame.
    """
    missing = [col for col in required_columns if col not in df.columns]

    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    return True


def check_nulls(df, columns):
    """
    Validate that selected columns do not contain null values.
    """
    null_columns = [col for col in columns if df[col].isnull().any()]

    if null_columns:
        raise ValueError(f"Null values found in columns: {null_columns}")

    return True


def check_positive_values(df, columns):
    """
    Validate that selected numeric columns contain positive values.
    """
    invalid_columns = [col for col in columns if (df[col] <= 0).any()]

    if invalid_columns:
        raise ValueError(f"Invalid non-positive values found: {invalid_columns}")

    return True