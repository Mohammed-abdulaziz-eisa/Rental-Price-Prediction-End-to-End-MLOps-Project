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
    Prepares the dataset for the machine learning pipeline by executing the necessary preprocessing steps.

        The function performs the following operations:
        1. Loads the preprocessed dataset from the database.
        2. Encodes categorical features using one-hot encoding.
        3. Parses and processes the garden data column.
        4. Binarizes specified columns to convert them into a binary format.

    Returns:
        DataFrame: A pandas DataFrame containing the fully prepared data, ready for model training.
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

    This function targets specific columns that require encoding to avoid issues with multicollinearity.
    The `pandas.get_dummies` function is used to perform the encoding.

    Args:
        data (DataFrame): The DataFrame containing the categorical data to be encoded.

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
    Parses and transforms the 'garden' column from textual data to a numerical format.

    The function identifies whether a garden is present and extracts the size of the garden if applicable.
    The `re` module is utilized to find numerical values within the textual data.

    Args:
        data (DataFrame): The DataFrame containing the 'garden' column to be parsed.

    Returns:
        DataFrame: The DataFrame with the 'garden' column transformed into a numerical format.
    """
    logger.info("Parsing the garden data...")
    dataframe["garden"] = dataframe["garden"].apply(
        lambda x: 0 if x == "Not present" else int(re.findall(r"\d+", x)[0])
    )
    return dataframe


def binarize_df(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Converts specified columns into a binary format.

    The function uses the `LabelBinarizer` from `sklearn.preprocessing` to transform columns into binary values.
    This is particularly useful for features that are already binary but represented as categorical variables.

    Args:
        data (DataFrame): The DataFrame containing columns to be binarized.

    Returns:
        DataFrame: The DataFrame with binarized columns.
    """
    # print("Step 3 : Binarizing the data...")
    binarizer_col = dataframe[
        ["balcony_yes", "storage_yes", "parking_yes", "furnished_yes", "garage_yes"]
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

"""
Step 1 : Loading the data...
Step 2 : Dummy encoding the data...
Step 3 : Binarizing the data...
                                       address   area  constraction_year  rooms  bedrooms  bathrooms  ...  rent balcony_yes parking_yes furnished_yes garage_yes  storage_yes
0     1071 HN Amsterdam (Cornelis Schuytbuurt)  167.0               1870      3         2          2  ...  4500           1           0             1          0            0
1       1071 HK Amsterdam (Concertgebouwbuurt)  150.0               1890      3         2          2  ...  3450           1           1             1          0            0
2       1071 HK Amsterdam (Concertgebouwbuurt)  150.0               1890      3         2          2  ...  3450           1           1             1          0            0
3         1071 WV Amsterdam (Hondecoeterbuurt)   90.0               1923      3         2          1  ...  2000           1           0             1          0            0
4         1071 WV Amsterdam (Hondecoeterbuurt)  104.0               1923      3         2          1  ...  3250           0           0             0          0            0
...                                        ...    ...                ...    ...       ...        ...  ...   ...         ...         ...           ...        ...          ...
1723            1033 DL Amsterdam (Terrasdorp)   75.0               1990      3         2          1  ...  1450           0           0             1          0            0
1724            1033 DZ Amsterdam (Terrasdorp)   75.0               1990      3         2          1  ...  1500           1           0             1          0            0
1725          1021 NX Amsterdam (IJplein e.o.)   74.0               1986      2         1          1  ...  1400           0           0             1          0            0
1726       1021 EC Amsterdam (Vogelbuurt Zuid)  118.0               1920      5         4          1  ...  2650           1           1             1          0            1
1727       1042 AL Amsterdam (Westhaven Noord)  110.0               2019      5         4          2  ...  2600           0           0             1          0            1

[1728 rows x 17 columns]
"""


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
#                           columns = ['balcony' , 'storage' , 'parking' , 'furnished', 'garden'],
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
#     binarizer_col = data[['balcony_yes' , 'storage_yes' , 'parking_yes', 'furnished_yes', 'garden_yes']]
#     label_binarizer =  LabelBinarizer()
#     for col in binarizer_col:
#         data[col] = label_binarizer.fit_transform(data[col])

#     return data


# # test the script
# baseline_data = prepare_data()
# print(baseline_data)
