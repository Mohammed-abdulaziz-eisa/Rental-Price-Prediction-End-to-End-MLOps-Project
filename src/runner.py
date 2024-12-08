"""
This script serves as the entry point for running the machine learning model to make predication.

The `main` function:
1. Initializes the model service.
2. Loads the pre-trained model from the specified directory.
3. Uses the loaded model to make predictions.
4. Logs the prediction results and model name used for predication.

Logging is integrated with Loguru, capturing all events, including errors and exceptions
to facilitate debugging and monitoring of script execution.
"""

from loguru import logger

from models.model_services import ModelService
from config import model_setting


@logger.catch
def main():
    """
    Executes the main workflow for running the model predication.

    The function performs the following steps:
    1. Logs the start of the script execution.
    2. creates an instance of the ModelService class.
    3. Loads the pre-trained model using the `load_model` method.
    4. Predicts rental prices using the loaded model with sample input parameters.
    5. Logs the prediction results along with the model name used for predication.

    This function decrated with the Loguru's `@logger.catch` to automatically log any exceptions
    that accur during the script execution.
    """
    logger.info("running the runner script ...")
    ml_svc = ModelService()
    ml_svc.load_model()
    
    feature_values = {
        'area': 85,
        'constraction_year': 2015,
        'bedrooms': 2,
        'garden_area': 20,
        'balcony_present': 1,
        'parking_present': 1,
        'furnished': 0,
        'garage_present': 0,
        'storage_present': 1,
    }
    pred = ml_svc.predict(list(feature_values.values()))
    logger.info(f"the predication is : {pred} From the model : {model_setting.model_name}")


if __name__ == "__main__":
    main()
