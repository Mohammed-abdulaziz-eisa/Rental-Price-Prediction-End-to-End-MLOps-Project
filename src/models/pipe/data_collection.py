"""
    This module is responsible for loading data into our data pipeline, utilizing SQLAlchemy ORM for database interaction.

    The primary function, `load_data_from_db`, extracts data from the specified database table and returns it as a pandas DataFrame. 
    The process involves constructing a query to select data from the `RentApartments` table and executing it through the SQLAlchemy engine. 
    The resulting data is then loaded into pandas for further analysis.

    Logging is implemented with Loguru to track the data extraction process, providing insights into the operation's status and any potential issues.
"""

import pandas as pd 

#from config import settings
from loguru import logger 
from sqlalchemy import select 

from config.config import engine 
from db.db_model import RentApartments


def load_data(path):
    #print("Loading CSV file...")
    # for short message we can use info 
    logger.info(f"Loading CSV file at path {path}")
    return pd.read_csv(path)



def load_data_from_db():
    """
    Extracts data from the specified database table and returns it as a pandas DataFrame.
    
    The function first constructs a query to select all rows from the `RentApartments` table.
    Then, it executes the query using the SQLAlchemy engine and returns the resulting DataFrame.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the extracted data.
    """
    logger.info("extracting the table from the database ...")
    query = select(RentApartments)
    return pd.read_sql(query , engine)
