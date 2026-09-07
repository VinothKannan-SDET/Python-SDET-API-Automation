import logging
import os

from utilities.security_utils import sanitize_payload


def get_logger(name):
    """
    Create and return a configured logger.

    :param name: Logger name
    :return: Configured logger instance
    """

    os.makedirs("logs", exist_ok=True)

    safe_data = sanitize_payload(name)
    logger = logging.getLogger(safe_data)

    if not logger.handlers:

        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(
            "logs/api_automation.log",
            encoding="utf-8"
        )

        console_handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger