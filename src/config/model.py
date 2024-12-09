"""
This module sets up the ML model configuration.

It utilizes Pydantic's BaseSettings for configuration management,
allowing settings to be read from environment variables and a .env file.
"""

from pydantic import DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class ModelSettings(BaseSettings):
    """
    ML model configuration settings for the application.

    Attributes:
        model_config (SettingsConfigDict): Model config, Load from .env file.
        model_path (DirectoryPath): Path to the model directory.
        model_name (str): Name of the model file.
    """

    model_config = SettingsConfigDict(
        env_file="config/.env",
        env_file_encoding="UTF-8",
        extra="ignore",
        protected_namespaces=("settings_",),
    )

    model_path: DirectoryPath
    model_name: str


model_setting = ModelSettings()
