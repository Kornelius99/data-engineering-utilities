import logging
from pathlib import Path


def create_logger(log_name: str = "etl_pipeline", log_dir: str = "logs"):
    """
    Create a reusable ETL logger.

    Args:
        log_name: Name of the logger and log file.
        log_dir: Directory where log files are stored.

    Returns:
        Configured logger object.
    """

    Path(log_dir).mkdir(exist_ok=True)

    logger = logging.getLogger(log_name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(f"{log_dir}/{log_name}.log")

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger