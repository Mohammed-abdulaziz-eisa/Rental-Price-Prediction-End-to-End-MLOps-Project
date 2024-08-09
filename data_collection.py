import pandas as pd 
from config import settings
from loguru import logger 
def load_data(path = settings.data_file_name):
    #print("Loading CSV file...")
    # for short message we can use info 
    logger.info(f"Loading CSV file at path {path}")
    return pd.read_csv(path)
# # test 
# df = load_data()
# print(df)