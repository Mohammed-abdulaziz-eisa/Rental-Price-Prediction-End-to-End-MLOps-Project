"""
Main appplication script for running the ML model to inference service.

This script intializes the model inference services 'ModelInferenceService',
Load the ML model, makes a predication based on predefined input user parameters,
and logs the output along with the model name used for predication.

It demostrates the typical workflow of using the ModelInferenceService in Practical
application context.
"""

from loguru import logger

from models.model_inference import ModelInferenceService


@logger.catch
def main():
    """
    Executes the main workflow for running the model predication.

    The function performs the following steps:
    Logs the start of the script execution,
    creates an instance of the ModelInferenceService class,
    Loads the pre-trained model using the `load_model` method,
    Predicts rental prices using the loaded model with sample parameters,
    and logs the results along with the model name used for predication.

    This function decrated with the Loguru's @logger.catch to automatically
    log any exceptions that accur during the script execution.
    """
    logger.info("running the runner script ...")
    ml_svc = ModelInferenceService()
    ml_svc.load_model()

    feature_values = {
        "area": 85,
        "constraction_year": 2015,
        "bedrooms": 2,
        "garden_area": 20,
        "balcony_present": 1,
        "parking_present": 1,
        "furnished": 0,
        "garage_present": 0,
        "storage_present": 1,
    }
    pred = ml_svc.predict(list(feature_values.values()))
    logger.info(f"Prediction: {pred}")


if __name__ == "__main__":
    main()
