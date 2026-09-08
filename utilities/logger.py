"""Centralized framework logging."""

import logging
import os
from logging.handlers import RotatingFileHandler


def get_logger(name):
    """Create/reuse a rotating console + file logger."""
    os.makedirs("logs", exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if not logger.handlers:
        file_handler = RotatingFileHandler(
            "logs/api_automation.log",
            maxBytes=2_000_000,
            backupCount=3,
            encoding="utf-8",
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
