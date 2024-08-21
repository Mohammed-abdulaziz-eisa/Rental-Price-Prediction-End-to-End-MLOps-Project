"""
    Model Service is responsble for loading the machine learning model, making predictions,
    and managing the model lifecycle, including saving and loading it from a pickle file.
    
    Steps :
        1. load the model from a specified directory 
        2. make prediction using the loaded model 
        
    ModelService class is intended to be used by a runner script that performs predictions.
    If the model is not found in the specifed directory, the service will trigger the model
    creation, save it as a pickle file and then load it for use. the process is logged 
    throughout, providing debugging information aout the model's staus such as wether it's 
    being created, saved or loaded. 
    
    In the predict function, the input parameters are logged and the predication is returned 
    based on the provided input parameters.
    
"""
# standard library packages
import pickle as pk
from pathlib import Path
# third party packages
from loguru import logger 
# local packages
from config.config import settings
from models.pipe.model import build_model

class ModelService:
    """
    ModelService class for managing ML models.
    
    This class provide functionality for loading, saving, and making predictions
    on ML models from specific paths in the filesystem. also checks if the model
    exists or not before loading it. if model not exists it will build one.
    
    Attributes
    ----------
    model : object
        the ML model object loaded from a pickle file
    
    Methods
    -------
    __init__(self) : Constructor that initializes the model object 
    load_model(self) : Loads the model from a pickle file if it exists else builds one
    predict(self, input_parameters) : Makes a prediction using the loaded model by passing input parameters
    
    """
    def __init__(self):
        """ Initializes the model object """
        self.model = None

    def load_model(self):
        """
        Function that loads the model from a pickle file if it exists else builds one
        
        load_model function is responsible for loading the model from a pickle file if it exists
        else it will build a new model. the loading process is logged throughout the function to 
        provide debugging information about the model's status such as wether it's being built, 
        saved or loaded. 
        
        Args:
            None
        
        Returns: 
             None
        """
        logger.info(f"loading the model from directory : {settings.model_path}/{settings.model_name}")
        model_path = Path(f'{settings.model_path}/{settings.model_name}')

        if not model_path.exists():
            logger.warning(f"model not found at {settings.model_path}/{settings.model_name}")
            build_model()
        logger.info(f"model {settings.model_name} exists --> loading model configuration file")
        self.model = pk.load(open(f'{settings.model_path}/{settings.model_name}', 'rb'))

    def predict(self, input_parameters):
        """
        Function that makes a prediction using the loaded model by passing input parameters

        Args:
            input_parameters (list): list of input parameters for the model

        Returns:
            list: list of predicted values
        """
        logger.info(f"input parameters : {input_parameters} making prediction !")
        return self.model.predict([input_parameters])
# Test the script
# ml_svc = ModelService()
# ml_svc.load_model()
# pred = ml_svc.predict([85 , 2015 , 2 ,20 , 1 ,1 ,0 ,0 ,1])
# print(pred)