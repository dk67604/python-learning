import logging

def setup_file_logger(name: str, log_file: str) -> logging.Logger:
    """
    Set up a logger for file processing.

    Args:
        name (str): The name of the logger.
        log_file (str): The path to the log file.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '[%(asctime)s] [%(processName)s] [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.propagate = False
    return logger