"""
This module sets up the database configuration.

It utilizes Pydantic's BaseSettings for configuration management,
allowing settings to be read from environment variables and a .env file.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine


class DbSettings(BaseSettings):
    """
    Database configuration settings for the application.
    
    Attributes:
        model_config (SettingConfigDict): Model config, Load from .env file.
        db_conn_str (str): Database connfication string.
        rent_apart_table_name (str): Name of rental apartments table in the database.
    """
    
    model_config = SettingsConfigDict(
        env_file='config/.env',
        env_file_encoding='UTF-8',
        extra='ignore',
        protected_namespaces=('settings_',),
    )
    
    db_conn_str: str
    rent_apart_table_name: str


db_settings = DbSettings()


engine= create_engine(db_settings.db_conn_str)
