"""
Model builder Service is provide functionality for building a ML model

Steps :
    1. train the model
    2. save the model
It contain the ModelBuilderServices class that offers methods
to train a model, and save it to a specified path
"""
# third party packages
from loguru import logger

# local packages
from config import model_setting
from models.pipe.model import build_model


class ModelBuilderService:
    """
    ModelBuilderService class for Building and saving ML models.

    This class provide functionality for train, saving
    ML models from specific paths in the filesystem.
    also checks if the model exists or not before loading it.
    if model not exists it will build one.

    Attributes
    ----------
        model_path (str) : Path to the model directory.
        model_name (str) : Name of the model file.

    Methods
    -------
        __init__(self) : Constructor that initializes the ModelBuilderService
        train_model(self) : Train the model and saves it to a specified path
    """

    def __init__(self) -> None:
        """Initializes the model object"""
        self.model = None
        self.model_path = model_setting.model_path
        self.model_name = model_setting.model_name

    def train_model(self) -> None:
        """
        Function that trains and saves it to a specified path

        Args:
            None

        Returns:
             None
        """
        logger.info(
            f"Building the model config file at "
            f"{self.model_path}/{self.model_name}",
        )

        build_model()
