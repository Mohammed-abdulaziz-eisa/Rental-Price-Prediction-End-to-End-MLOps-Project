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


import pandas as pd
import re
from sklearn.preprocessing import LabelBinarizer
from data_collection import load_data

def prepare_data():
    # Load data
    data = load_data()
    
    # Encode categorical columns
    data_encoded = encode_cat_cols(data)
    
    # Parse the garden column
    data_parsed = parse_garden_col(data_encoded)
    
    # Binarize certain columns
    baseline_data = binarize_df(data_parsed)
    
    return baseline_data
    
def encode_cat_cols(data):
    return pd.get_dummies(data,
                          columns=['balcony', 'storage', 'parking', 'furnished', 'garden'],
                          drop_first=True,
                          prefix_sep='_')

def parse_garden_col(data):
    data['garden'] = data['garden'].apply(lambda x: 0 if x == 'Not present' else int(re.findall(r'\d+', x)[0]))
    return data

def binarize_df(data):
    binarizer_cols = ['balcony_yes', 'storage_yes', 'parking_yes', 'furnished_yes', 'garden_yes']
    label_binarizer = LabelBinarizer()
    for col in binarizer_cols:
        data[col] = label_binarizer.fit_transform(data[col])
    return data

# Test the script
baseline_data = prepare_data()
print(baseline_data)
