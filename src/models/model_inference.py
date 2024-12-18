"""
This module provides functionality for making predictions using ML models.

It contain the ModelInferenceService class that offers methods
to load a model, make predictions using the loaded model.
"""

import pickle as pk
from pathlib import Path

from loguru import logger

from config import model_setting


class ModelInferenceService:
    """
    ModelService class for managing ML models.

    This class provide functionality for loading, saving, and making
    predictions on ML models from specific paths in the filesystem.
    also checks if the model exists or not before loading it.
    if model not exists it will build one.

    Attributes
    ----------
        model : object
        the ML model object loaded from a pickle file

    Methods
    -------
        __init__(self) : Constructor that initializes the model object
        load_model(self) : Loads the model from a pickle file if it exists
        else builds one predict(self, input_parameters) : Makes a prediction
        using the loaded model by passing input parameters

    """

    def __init__(self) -> None:
        """Initializes the model object"""
        self.model = None
        self.model_path = model_setting.model_path
        self.model_name = model_setting.model_name

    def load_model(self) -> None:
        """
        Function that loads the model from a pickle file if it exists

        Args:
            None

        Returns:
             None
        """
        logger.info(
            f"checking the existance of the model config file at "
            f"{self.model_path}/{self.model_name}",
        )

        model_path = Path(
            f"{self.model_path}/{self.model_name}",
        )

        if not model_path.exists():
            raise FileNotFoundError('Model file does not exist!')
            # logger.warning(
            #     f"model not found at {self.model_path} "
            #     f"building {self.model_name}",
            # )

        logger.info(
            f"model {self.model_name} exists --> "
            "loading model configuration file",
        )

        with open(model_path, "rb") as model_file:
            self.model = pk.load(model_file)

    def predict(self, input_parameters: list) -> list:
        """
        Function that makes a prediction using the loaded model
        by passing input parameters

        Args:
            input_parameters (list): list of input parameters for the model

        Returns:
            list: list of predicted values
        """
        logger.info(
            f"input parameters : {input_parameters} ",
            f"making prediction with model : {self.model}",
        )
        return self.model.predict([input_parameters])