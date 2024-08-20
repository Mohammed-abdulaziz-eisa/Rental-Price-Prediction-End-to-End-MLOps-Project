from pathlib import Path
import pickle as pk
from config.config import settings
from models.pipe.model import build_model
from loguru import logger 
class ModelService:
    def __init__(self):
        self.model = None

    def load_model(self):
        logger.info(f"loading the model from directory : {settings.model_path}/{settings.model_name}")
        model_path = Path(f'{settings.model_path}/{settings.model_name}')

        if not model_path.exists():
            logger.warning(f"model not found at {settings.model_path}/{settings.model_name}")
            build_model()
        logger.info(f"model {settings.model_name} exists --> loading model configuration file")
        self.model = pk.load(open(f'{settings.model_path}/{settings.model_name}', 'rb'))

    def predict(self, input_parameters):
        logger.info(f"input parameters : {input_parameters} making prediction !")
        return self.model.predict([input_parameters])
# Test the script
# ml_svc = ModelService()
# ml_svc.load_model()
# pred = ml_svc.predict([85 , 2015 , 2 ,20 , 1 ,1 ,0 ,0 ,1])
# print(pred)