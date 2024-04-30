import pandas as pd 
from data_preparation import prepare_data   
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
def build_model():
    # we need to train and save the model 
    
    # 1 - loading the data from prepare script
    data = prepare_data()
    # 2- identify the X and y variables
    X , y = get_X_y(data)
    df_split = split_data(X , y)
    model_score = train_model(df_split[0] , df_split[1] , df_split[2] , df_split[3])
    
    return model_score
    
def get_X_y(data):
    X = data[['area' ,
              'constraction_year' ,
              'bedrooms' ,
              'garden' ,
              'balcony_yes' ,
              'storage_yes' ,
              'parking_yes' ,
              'furnished_yes' , 
              'garage_yes']]
    
    y = data['rent']
    
    return X ,y 


def split_data(X , y):
    X_train , X_test , y_train , y_test = train_test_split(X , y , test_size= 0.2 , random_state = 42)
    return X_train , X_test , y_train , y_test




def train_model(X_train, X_test , y_train , y_test):
    rf = RandomForestRegressor()
    rf.fit(X_train , y_train)
    model_score = rf.score(X_test , y_test)
    return model_score
    
    
# test 
model_score = build_model()
print(model_score)
