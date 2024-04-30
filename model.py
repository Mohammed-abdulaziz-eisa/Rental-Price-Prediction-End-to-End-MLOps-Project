import pandas as pd 
from data_preparation import prepare_data   
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
def build_model():
    # we need to train and save the model 
    
    # 1 - loading the data from prepare script
    data = prepare_data()
    # 2- identify the X and y variables
    X , y = get_X_y(data)
    X_train , X_test ,y_train , y_test  = split_data(X , y)
    Grid_rf = train_model(X_train, y_train)
    evalute_score = evalute_model(Grid_rf , X_test , y_test)
    #print(r'Model Evalute Score : ' , evalute_score)
    return r'Model Evalute Score : ' , evalute_score
    
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

# def train_model(X_train, X_test , y_train , y_test):
#     rf = RandomForestRegressor()
#     rf.fit(X_train , y_train)
#     model_score = rf.score(X_test , y_test)
#     return model_score
def train_model(X_train , y_train ):
    grid_param = {
    "n_estimators" : range(50 ,100 , 20),
    "criterion" : ['mae'], 
    "max_depth" : range(6 , 12 , 2)
    }
    grid = GridSearchCV(
        RandomForestRegressor() , 
        param_grid= grid_param , 
        cv = 5 , 
        n_jobs = -1
    )
    model_grid = grid.fit(X_train , y_train)
    #best_model_param = model_grid.best_params_
    #best_model_score = model_grid.best_score_
    print("Train score: " , model_grid.best_score_)
    return model_grid.best_estimator_
def evalute_model(model , X_test , y_test):
    return model.score(X_test , y_test)    
# test 
df_get = build_model()
print(df_get)


'''
Train score:  0.7143105454150367
('Model Evalute Score : ', 0.7127687339259972)

'''