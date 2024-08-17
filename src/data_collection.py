import pandas as pd 
#from config import settings
from loguru import logger 

from config.config import engine 
from db_model import RentApartments
from sqlalchemy import select 

def load_data(path):
    #print("Loading CSV file...")
    # for short message we can use info 
    logger.info(f"Loading CSV file at path {path}")
    return pd.read_csv(path)
# # test 
# df = load_data()
# print(df)


def load_data_from_db():
    logger.info("extracting the table from the database ...")
    query = select(RentApartments)
    return pd.read_sql(query , engine)