"""
Main application script for running the ML model to builder service.

This script  intializes the model builder services 'ModelBuilderService',
train the model and save it to model config folder. also save logs the output,
It demostrates the typical workflow of using the ModelBuilderService in Practical
application context.
"""

from loguru import logger

from models.model_builder import ModelBuilderService


@logger.catch
def main():
    """
    Run the application.
    Train the model and save it to model config folder.
    """
    logger.info("running the runner builder script ...")
    ml_svc = ModelBuilderService()
    ml_svc.train_model()


if __name__ == "__main__":
    main()
