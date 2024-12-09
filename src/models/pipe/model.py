"""
This module creates the pipeline for building, training and saving ML model.

It includes the process of data preparation, model training using
RandomForestRegressor, hyperparameter tuning with GridSearchCV,
model evaluation, and serialization of the trained model.
"""

import pandas as pd
import pickle as pkl

from loguru import logger
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

from config import model_setting
from models.pipe.data_preparation import prepare_data


def build_model() -> None:
    """
    Coordinates the end-to-end process of building, training, and saving
    the machine learning model.
    The `build_model` function orchestrates the entire model building process

    Returns:
        None
    """
    # we need to train and save the model
    logger.info("starting up model building pipleline")
    # 1 - loading the data from prepare script
    data = prepare_data()
    feature_names = [
        "area",
        "constraction_year",
        "bedrooms",
        "garden",
        "balcony_yes",
        "parking_yes",
        "furnished_yes",
        "garage_yes",
        "storage_yes",
    ]
    # 2- identify the X and y variables
    # print("Building model...")
    X, y = _get_X_y(
        data,
        col_x=feature_names,
    )
    X_train, X_test, y_train, y_test = _split_train_test(
        X,
        y,
    )
    Grid_rf = _train_model(
        X_train,
        y_train,
    )
    _evalute_model(
        Grid_rf,
        X_test,
        y_test,
    )
    # print(r'Model Evalute Score : ' , evalute_score)
    # Saving Model as pickle file we can load it any time we wanna to use it
    _save_model(Grid_rf)
    # return r'Model Evalute Score : ' , evalute_score


def _get_X_y(
    data: pd.DataFrame,
    col_x: list[str],
    col_y: str = "rent",
) -> tuple[pd.DataFrame, pd.Series]:
    """
    Split the dataset into feature and target variables.

    Args:
        data (pd.DataFrame): The dataset to split.
        col_x (list[str]): List of feature variable names.
        col_y (str): Name of target variables.

    Returns:
        Tuple: A tuple containing :
            - X (DataFrame): The feature Variable.
            - y (Series): The target variable.
    """
    logger.info(f" definign X and X variables.{col_x} ; {col_y}")
    return data[col_x], data[col_y]


def _split_train_test(
    features: pd.DataFrame,
    target: pd.Series,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
       Splits the data into training and testing sets.

       This function ensures that 80% of the data is used for training
       and 20% for testing, with a fixed random state for reproducibility.

        Args:
            features (pd.DataFrame): The feature dataset.
            target (pd.Series): The target variable.

    Returns:
        Tuple: A Tuple containing:
            - X_train (pd.DataFrame): The training feature variable.
            - X_test (pd.DataFrame): The testing feature variable.
            - y_train (pd.Series): The training target variable.
            - y_test (pd.Series): The testing target variable.
    """
    logger.info("splitting data into train and test sets ")
    return train_test_split(features, target, test_size=0.2, random_state=42)


#  def train_model(X_train, X_test , y_train , y_test):
#     rf = RandomForestRegressor()
#     rf.fit(X_train , y_train)
#     model_score = rf.score(X_test , y_test)
#     return model_score


def _train_model(
    X_train: pd.DataFrame,
    y_train: pd.Series,
) -> RandomForestRegressor:
    """
    Trains a Random Forest Regressor with hyperparameter using GridSearchCV.

    The function searches for the best hyperparameters for the Random Forest
    Regressor model from specified trains the model in the training data.

    Args:
        X_train (pd.DataFrame): The Training set features.
        y_train (pd.Series): The Training set target variable.

    Returns:
        RandomForestRegressor:  The best-performed model hyperparameter.
    """
    logger.info("training a model with hyperparameters")
    grid_param = {
        "n_estimators": range(50, 100, 20),
        "criterion": [
                      "squared_error",
                      "poisson",
                      "absolute_error",
                      "friedman_mse"
                      ],
        "max_depth": range(6, 12, 2),
    }
    logger.debug(f"grid param : {grid_param}")
    grid = GridSearchCV(
                        RandomForestRegressor(),
                        param_grid=grid_param,
                        cv=5,
                        n_jobs=-1
                        )
    model_grid = grid.fit(X_train, y_train)
    # best_model_param = model_grid.best_params_
    # best_model_score = model_grid.best_score_
    # print("Train score: " , model_grid.best_score_)
    return model_grid.best_estimator_


def _evalute_model(
    model: RandomForestRegressor,
    X_test: pd.DataFrame,
    y_test: pd.Series,
) -> float:
    """
    Evaluates the performance of the trained model on the data.

    This Function calculates and logs the model R^2 score, which indicates
    how well the model predicts the target variable on the test set.

    Args:
        model (RandomForestRegressor): The trained Random Forest Regressor.
        X_test (pd.DataFrame): The Test set features.
        y_test (pd.Series): The Test set target variable.

    Returns:
        float: The R^2 score of the model on the test set.
    """
    model_score = model.score(
        X_test,
        y_test,
    )
    logger.info(f"evaluting the model performance with score : {model_score}")
    return model_score


def _save_model(model: RandomForestRegressor) -> None:
    """
    Saves the trained model to a specified directory as a pickle file.

    The function uses the path and file name defined in the settings
    configuration to save the model.

    Args:
        model (RandomForestRegressor): The trained model to be saved.

    Returns:
        None
    """
    model_path = f"{model_setting.model_path}/{model_setting.model_name}"
    logger.info(f"saving the model to directory : {model_path}")
    with open(model_path, "wb") as model_file:
        pkl.dump(model, model_file)


# test
df_get = build_model()
# print(df_get)
