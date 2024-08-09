import pandas as pd
import re
from data_collection import load_data
from sklearn.preprocessing import LabelBinarizer
from loguru import logger
def prepare_data():
    # make logger object to use it in the script
    logger.info("Starting up preprocessing Pipeline")
    # 1. load preprocessed dataset
    data = load_data()
    # 2. encode categorical data
    data_encoded = encode_cat_cols(data)
    # 3. parse the garden data
    df = parse_garden_col(data_encoded)
    # 4. binarize the data
    df = binarize_df(df)

    return df

def encode_cat_cols(data):
    cols = ['balcony','parking','furnished','garage','storage']
    logger.info(f"Dummy encoding the data {cols}")
    #print("Step 2 : Dummy encoding the data...")
    return pd.get_dummies(data, 
                          columns = cols, 
                          drop_first=True)

# def parse_garden_col(data):
#     print("Parsing the garden data...")
#     for i in range(len(data)):
#         if data.garden[i]=='Not present':
#             data.garden[i]=0
#         else: 
#             data.garden[i] = int(re.findall(r'\d+', data.garden[i])[0])
#     return data 
def parse_garden_col(data):
    logger.info("Parsing the garden data...")
    data['garden'] = data['garden'].apply(lambda x : 0 if  x == "Not present" else int(re.findall(r'\d+', x)[0]))
    return data

def binarize_df(data):
    #print("Step 3 : Binarizing the data...")
    binarizer_col = data[['balcony_yes' , 'storage_yes' , 'parking_yes' , 'furnished_yes' , 'garage_yes']]
    logger.info(f"Binarizing the data {binarizer_col}")
    label_binarizer = LabelBinarizer()
    for col in binarizer_col:
        data[col] = label_binarizer.fit_transform(data[col])
    return data

# # test the script
# baseline_data = prepare_data()
# print(baseline_data)


# output 

'''
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
'''


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