"""
This module provides functionality for preparing a dataset for ML model.

It consists of functions to load data from a database,
encode categorical columns, and parse specific columns for further processing.
"""

import pandas as pd
import re

from loguru import logger
from sklearn.preprocessing import LabelBinarizer

from models.pipe.data_collection import load_data_from_db


def prepare_data() -> pd.DataFrame:
    """
    Prepares the dataset for the machine learning pipeline by executing
    the necessary preprocessing steps.

        The function performs the following operations:
        1. Loads the preprocessed dataset from the database.
        2. Encodes categorical features using one-hot encoding.
        3. Parses and processes the garden data column.
        4. Binarizes specified columns to convert them into a binary format.

    Returns:
        DataFrame: A pandas DataFrame containing the fully prepared data,
        which is ready for model training.
    """
    # make logger object to use it in the script
    logger.info("Starting up preprocessing Pipeline")
    # 1. load preprocessed dataset
    dataframe = load_data_from_db()
    # 2. encode categorical data
    data_encoded = encode_cat_cols(dataframe)
    # 3. parse the garden data
    df = parse_garden_col(data_encoded)
    # 4. binarize the data
    df = binarize_df(df)

    return df


def encode_cat_cols(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Encodes categorical features into a binary format using one-hot encoding.

    This function targets specific columns that require encoding to avoid
    issues with multicollinearity.
    The `pandas.get_dummies` function is used to perform the encoding.

    Args:
        data (DataFrame): The DataFrame containing data to be encoded.

    Returns:
        DataFrame: The DataFrame with encoded categorical features.
    """
    cols = ["balcony", "parking", "furnished", "garage", "storage"]
    logger.info(f"Dummy encoding the data {cols}")
    # print("Step 2 : Dummy encoding the data...")
    return pd.get_dummies(dataframe, columns=cols, drop_first=True)


# def parse_garden_col(data):
#     print("Parsing the garden data...")
#     for i in range(len(data)):
#         if data.garden[i]=='Not present':
#             data.garden[i]=0
#         else:
#             data.garden[i] = int(re.findall(r'\d+', data.garden[i])[0])
#     return data
def parse_garden_col(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Parses and transforms the 'garden' column from textual data to
    a numerical format.

    The function identifies whether a garden is present and extracts the size
    of the garden if applicable.
    The `re` module is utilized to find numerical values in the textual data.

    Args:
        data (DataFrame): Containing the 'garden' column to be parsed.

    Returns:
        DataFrame: The DataFrame with column transformed to numerical format.
    """
    logger.info("Parsing the garden data...")
    dataframe["garden"] = dataframe["garden"].apply(
        lambda x: 0 if x == "Not present" else int(re.findall(r"\d+", x)[0])
    )
    return dataframe


def binarize_df(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Converts specified columns into a binary format.

    The function uses the `LabelBinarizer` from `sklearn.preprocessing` to
    transform columns into binary values.
    This is particularly useful for features that are already binary
    but represented as categorical variables.

    Args:
        data (DataFrame): The DataFrame containing columns to be binarized.

    Returns:
        DataFrame: The DataFrame with binarized columns.
    """
    # print("Step 3 : Binarizing the data...")
    binarizer_col = dataframe[
        [
         "balcony_yes",
         "storage_yes",
         "parking_yes",
         "furnished_yes",
         "garage_yes"
         ]
    ]
    logger.info(f"Binarizing the data {binarizer_col}")
    label_binarizer = LabelBinarizer()
    for col in binarizer_col:
        dataframe[col] = label_binarizer.fit_transform(dataframe[col])
    return dataframe


# # test the script
# baseline_data = prepare_data()
# print(baseline_data)
# output


# import pandas as pd
# import re
# from sklearn.preprocessing import LabelBinarizer
# from data_collection import load_data

# # this script will make tree main steps

# # 1-  laoding the dataset
# # 2- encoding the data
# # 3- PARSING THE GRADEN DATA

# def prepare_data():

#     data = load_data()
#     data_encoded = encoded_cat_cols(data)
#     df = parse_garden_col(data_encoded)
#     baseline_data = binarizer_df (df)

#     return baseline_data


# def encoded_cat_cols(data):
#     return pd.get_dummies(data ,
#                           columns = ['balcony' ,
#                                       'storage' ,
#                                       'parking' ,
#                                       'furnished',
#                                        'garden'],
#                           drop_first= True ,
#                           prefix_sep= '_')


# def parse_garden_col(data):
#     for i in range(len(data)):
#         if data.garden[i]=='Not present':
#             data.garden[i]=0
#         else:
#             data.garden[i] = int(re.findall(r'\d+', data.garden[i])[0])
#     return data


# def binarizer_df(data):
#     binarizer_col = data[['balcony_yes' ,
#                           'storage_yes' ,
#                           'parking_yes',
#                           'furnished_yes',
#                           'garden_yes']]
#     label_binarizer =  LabelBinarizer()
#     for col in binarizer_col:
#         data[col] = label_binarizer.fit_transform(data[col])

#     return data


# # test the script
# baseline_data = prepare_data()
# print(baseline_data)
