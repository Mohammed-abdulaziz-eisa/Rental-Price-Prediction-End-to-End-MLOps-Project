"""
This module sets up the logger configuration.

It utilizes Pydantic's BaseSettings for configuration management,
allowing settings to be read from environment variables and a .env file.
"""

from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict


class LoggerSettings(BaseSettings):
    """
    Logger Settings configuration for the application.

    Attributes:
        model_config (SettingsConfigDict): Model config, Load from .env file.
        log_level (str): Logging level for the application.
    """

    model_config = SettingsConfigDict(
        env_file="config/.env",
        env_file_encoding="UTF-8",
        extra="ignore",
        protected_namespaces=("settings_",),
    )

    log_level: str


def configure_logging(log_level: str) -> None:
    """
    Configure the logging for the application.

    Arg:
        log_level (str): The log level to be set for the logger.

    Returns:
        None
    """

    # to remove the console output from loguru showing it only in the log file
    # logger.remove()
    logger.add(
        "logs/app.log",
        rotation="1 week",
        retention="2 weeks",
        level=log_level,
    )


# intializing the setting an logging configure
configure_logging(log_level=LoggerSettings().log_level)
