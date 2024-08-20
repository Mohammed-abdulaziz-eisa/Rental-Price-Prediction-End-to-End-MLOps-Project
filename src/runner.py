from models.model_services import ModelService
from config.config import settings
from loguru import logger

@logger.catch
def main():
    logger.info("running the runner script ...")
    ml_svc = ModelService()
    ml_svc.load_model()
    pred = ml_svc.predict([85 , 2015 , 2 ,20 , 1 ,1 ,0 ,0 ,1])
    logger.info(f"the predication is : {pred} From the model : {settings.model_name}")
    
if __name__ == '__main__':
    main()