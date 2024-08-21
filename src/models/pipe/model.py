import pandas as pd 
import pickle as pkl

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

from config.config import settings
from models.pipe.data_preparation import prepare_data   


from loguru import logger 
def build_model():
    # we need to train and save the model 
    logger.info("starting up model building Pipleline")
    # 1 - loading the data from prepare script
    data = prepare_data()
    # 2- identify the X and y variables
    #print("Building model...")
    X , y = get_X_y(data)
    X_train , X_test ,y_train , y_test  = split_data(X , y)
    Grid_rf = train_model(X_train, y_train)
    evalute_model(Grid_rf , X_test , y_test)
    #print(r'Model Evalute Score : ' , evalute_score)
    # Saving Model as pickle file we can load it any time we wanna to use it 
    save_model(Grid_rf)
    #return r'Model Evalute Score : ' , evalute_score

    
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
    logger.info(f"X shape : {X.shape} , y shape : {y.shape}")
    return X ,y 


def split_data(X , y):
    logger.info("splitting data into train and test sets ")
    X_train , X_test , y_train , y_test = train_test_split(X , y , test_size= 0.2 , random_state = 42)
    return X_train , X_test , y_train , y_test

# def train_model(X_train, X_test , y_train , y_test):
#     rf = RandomForestRegressor()
#     rf.fit(X_train , y_train)
#     model_score = rf.score(X_test , y_test)
#     return model_score
def train_model(X_train , y_train ):
    logger.info("training a model with hyperparameters")
    grid_param = {
    "n_estimators" : range(50 ,100 , 20),
    "criterion": ['squared_error', 'poisson', 'absolute_error', 'friedman_mse'],
    "max_depth" : range(6 , 12 , 2)
    }
    logger.debug(f"grid param : {grid_param}")
    grid = GridSearchCV(
        RandomForestRegressor() , 
        param_grid= grid_param , 
        cv = 5 , 
        n_jobs = -1
    )
    model_grid = grid.fit(X_train , y_train)
    #best_model_param = model_grid.best_params_
    #best_model_score = model_grid.best_score_
    #print("Train score: " , model_grid.best_score_)
    return model_grid.best_estimator_
def evalute_model(model , X_test , y_test):
    
    logger.info(f"evaluting the model performance with score : {model.score(X_test , y_test)}")
    return model.score(X_test , y_test)    


def save_model(model):
    logger.info(f"saving the model to directory : {settings.model_path}/{settings.model_name}")
    with open (f'{settings.model_path}/{settings.model_name}', 'wb') as f:
        pkl.dump(model ,f )
# test 
df_get = build_model()
#print(df_get)


'''
Train score:  0.7143105454150367
('Model Evalute Score : ', 0.7127687339259972)

'''