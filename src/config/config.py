"""
    This Module is used for configuring the application's settings.
    
    Setting Module is designed to handle the application's configuration and settings.
    including model configuration , data file paths , model names , log levels , 
    database connection string and table name. it's use Pydantic for validation 
    and management of the settings . the class is subclass of `BaseSettings`
    from Pydantic. Which ensures type of validation and settings management.
    
    Kay components:
        - model_config : Pydantic settings class for the model configuration for enviromnent 
                        variables in `.env` loading and encoding using `SettingsConfigDict`
        - model_path : Directory path where the model is stored in the filesystem
        - model_name : Name of the model.
        - log_level : Loging level for the connection string. 
        - db_conn_str : Database connections string.
        - rent_apart_table_name : Table name for rent apartment data.
        
    Logging is handled by loguru, with settings configured to output logs to a file 
    and save them in a log file called "app.log" in the current directory.
    
    Database connection string is used to connect to the database.
    
"""
from pydantic_settings import BaseSettings ,  SettingsConfigDict
from pydantic import DirectoryPath #, FilePath 
from loguru import logger
from sqlalchemy import create_engine

class Settings(BaseSettings):
    """
    Settings class for managing application configuaraiton and settings.
    
    Args:
        BaseSettings (BaseSettings): Pydantic settings class for settings management.
        
    Usage:
        - Instantiate the `Settings` class to load and validate configuration settings from
        the `config/.env` file.
        -  Configure Loguru for file-based logging and set up the SQLAlchemy engine for database. 
    """
    model_config = SettingsConfigDict(
        env_file = 'config/.env' ,
        env_file_encoding= 'UTF-8' ,
        protected_namespaces= ['settings_'],
        )
    #data_file_name : FilePath
    model_path : DirectoryPath
    model_name : str 
    log_level : str
    db_conn_str : str 
    rent_apart_table_name : str
    
    
def configure_logging(log_level: str) -> None:
    """
    Configure the logging for the application.

    Arg:
        log_level (str): The log level to be set for the logger.

    Return:
        None
    """

    # to remove the console output from loguru showing it only in the log file
    #logger.remove()
    logger.add(
        "logs/app.log" ,
        rotation= "1 week" ,
        retention= "2 weeks" ,
        level =log_level,
    )
    
# intializing the setting an logging configure 
settings = Settings()
configure_logging(log_level= settings.log_level)

# Create a database engine 
engine = create_engine(settings.db_conn_str)