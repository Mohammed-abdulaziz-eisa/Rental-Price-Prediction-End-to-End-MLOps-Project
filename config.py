# data_file_name ----> path to our csv file in collection.py
# model_path ------> the folder containing model config file 
# model_name ------> name of the model we should use 
from pydantic_settings import BaseSettings ,  SettingsConfigDict
from pydantic import DirectoryPath , FilePath 
from loguru import logger

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file = '.env' , env_file_encoding= 'UTF-8')
    data_file_name : FilePath
    model_path : DirectoryPath
    model_name : str 
    log_level : str

settings = Settings()
# to remove the console output from loguru showing it only in the log file
#logger.remove()
logger.add("app.log" , rotation= "1 day" , retention= "2 days" , compression= "zip" , level = settings.log_level)