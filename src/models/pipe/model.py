"""
    This module is responsible for building and saving a machine learning model to predict rental prices.

    The `build_model` function orchestrates the entire model building process, which includes:
    1. Loading and preparing the dataset.
    2. Splitting the data into training and testing sets.
    3. Training a Random Forest Regressor model with hyperparameter tuning using GridSearchCV.
    4. Evaluating the model's performance on the test set.
    5. Saving the trained model as a pickle file for later use.

    Logging is integrated with Loguru to track the model building process, providing insights into each step's status and potential issues.
"""

import pandas as pd 
import pickle as pkl

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

from config.config import settings
from models.pipe.data_preparation import prepare_data   


from loguru import logger 

def build_model():
    
    """
        Coordinates the end-to-end process of building, training, and saving the machine learning model.
        The `build_model` function orchestrates the entire model building process
         
        Returns:
            None
    """
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
    """
       Extracts feature variable (X) and target variable (y) from the prepared data.
       
       The function include various characteristics of the rental properties
       which the target is the rent price. 
       
       Args:
           data (DataFrame): The DataFrame containing the prepared data.

       Returns:
           Tuple: A tuple containing :
               - X (DataFrame): The feature Variable.
               - y (Series): The target variable.
    """
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
    """
       Splits the data into training and testing sets.
       
       This function ensures that 80% of the data is used for training
       and 20% for testing, with a fixed random state for reproducibility.
       
        Args:
            X (DataFrame): The feature variable.
            y (Series): The target variable.

    Returns:
        Tuple: A Tuple containing: 
            - X_train (DataFrame): The training feature variable.
            - X_test (DataFrame): The testing feature variable. 
            - y_train (Series): The training target variable. 
            - y_test (Series): The testing target variable.
    """
    logger.info("splitting data into train and test sets ")
    X_train , X_test , y_train , y_test = train_test_split(X , y , test_size= 0.2 , random_state = 42)
    return X_train , X_test , y_train , y_test

# def train_model(X_train, X_test , y_train , y_test):
#     rf = RandomForestRegressor()
#     rf.fit(X_train , y_train)
#     model_score = rf.score(X_test , y_test)
#     return model_score
def train_model(X_train , y_train ):
    """ 
        Trains a Random Forest Regressor model with hyperparameter using GridSearchCV.
        
        The function searches for the best hyperparameters for the Random Forest Regressor model
        from specified trains the model in the training data.
        
        Args:
            X_train (DataFrame): The Training set features. 
            y_train (Series): The Training set target variable.
            
        Returns:
            RandomForestRegressor:  The best-performed Random Forest Regressor model with hyperparameters.
    """
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
    """ 
        Evaluates the performance of the trained Random Forest Regerssor on the data.
        
        This Function calculates and logs the model R^2 score, which indicates how well 
        the model predicts the target variable on the test set.
        
        Args:
            model (RandomForestRegressor): The trained Random Forest Regressor model.
            X_test (DataFrame): The Test set features.
            y_test (Series): The Test set target variable.
            
        Returns:
            float: The R^2 score of the model on the test set. 
    """
    logger.info(f"evaluting the model performance with score : {model.score(X_test , y_test)}")
    return model.score(X_test , y_test)    


def save_model(model):
    """
    Saves the trained model to a specified directory as a pickle file.

    The function uses the path and file name defined in the settings to save the model.

    Args:
        model (RandomForestRegressor): The trained Random Forest Regressor model to be saved.

    Returns:
        None
    """
    logger.info(f"saving the model to directory : {settings.model_path}/{settings.model_name}")
    with open (f'{settings.model_path}/{settings.model_name}', 'wb') as f:
        pkl.dump(model ,f )
# test 
df_get = build_model()
#print(df_get)