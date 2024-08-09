import pandas as pd 
from config import settings
def load_data(path = settings.data_file_name):
    print("Loading CSV file...")
    return pd.read_csv(path)
# # test 
# df = load_data()
# print(df)