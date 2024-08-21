# Rental Price Prediction: End-to-End MLOps Project

## Project Overview

This project is an end-to-end MLOps pipeline for predicting rental prices. The system leverages a Random Forest model trained on real estate data to provide rental price predictions. The project is structured to handle data ingestion, preprocessing, model training, evaluation, and prediction, with a robust logging mechanism and scalable deployment features.

## Project Structure

```bash
src/
│
├── config/                    # Configuration files
│   └── config.py              # Project settings and database connection
│   └── .env                   # Environment variables
├── db/                        # Database-related scripts
│   ├── db_model.py            # SQLAlchemy model for database table
│   └── db_sqlite              # SQLite database
├── models/                    # Model-related scripts and artifacts
│   ├── model/                 # Training pipeline scripts
│   │   ├── model.py           # Model training, evaluation, and saving
│   │   └── model_services.py  # Model loading and prediction service
│   └── pipe/                  # Data pipeline scripts
│   │    ├── data_collection.py # Data collection from CSV and database
│   │    └── data_preparation.py # Data preprocessing and feature engineering
│   │    └── model.py           # Model training, evaluation, and saving
│   └── model_services.py       # Model loading and prediction service
│   └── model_baseline.ipynb    # Baseline notebook for model evaluation
├── logs/                      # Logs directory (automatically populated)
│   └── app.log                # Log file for the project
│
└── runner.py                  # Main script to execute the prediction pipeline

```

## Project Structure

The project is organized as follows:
## Tools and Packages Used

- **Python**: Core programming language for building the pipeline.
- **pandas**: Data manipulation and analysis.
- **numpy**: Numerical computing.
- **SQLAlchemy**: ORM for database interactions.
- **pydantic**: Data validation and management.
- **Poetry**: Package manager for Python.
- **scikit-learn**: Machine learning library for model training and evaluation.
- **Loguru**: Logging library for tracking pipeline processes.
- **Flask**: Web framework for API deployment.
- **Celery**: Asynchronous task queue.
- **Docker**: Containerization for deploying the entire pipeline.
- **DBeaver**: Database management tool. 
- **Pickle**: Model serialization and deserialization.

## Key Features

1. **Data Ingestion**:
   - Load data from a CSV file or directly from a database.
   - Utilizes SQLAlchemy ORM to manage database connections and queries.

2. **Data Preprocessing**:
   - Categorical feature encoding, data binarization, and garden data parsing.
   - Scalable and modular preprocessing pipeline using `data_collection.py` and `data_preparation.py`.

3. **Model Training**:
   - Train a Random Forest model with hyperparameter tuning using GridSearchCV.
   - Automatically saves the best model as a `.pkl` file for later use.

4. **Prediction Service**:
   - Provides a service for loading the model and making predictions.
   - The `runner.py` script allows end-to-end execution of the prediction pipeline.

5. **Logging**:
   - Comprehensive logging with Loguru to monitor each step of the pipeline.

6. **Deployment**:
   - Ready to be containerized with Docker for consistent and scalable deployment.
