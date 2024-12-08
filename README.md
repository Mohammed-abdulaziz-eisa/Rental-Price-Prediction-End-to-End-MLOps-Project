# Rental Price Prediction: End-to-End MLOps Project

## Project Overview

This project is an end-to-end MLOps pipeline for predicting rental prices. The system leverages a Random Forest model trained on real estate data to provide rental price predictions. The project is structured to handle data ingestion, preprocessing, model training, evaluation, and prediction, with a robust logging mechanism and scalable deployment features.

## Project Structure

```bash
rental-price-prediction/
│
├── notebook/                  # Exploratory Data Analysis
│   └── model_baseline.ipynb   # Baseline notebook for model evaluation
│
│── app/
│   ├── templates/             # HTML templates  
│   │   └── index.html          # Index page
│   └── app.py                 # API for prediction service
│
├── src/
│   ├── config/                # Configuration Management
│   │   ├── __init__.py        # Project-wide settings and imports
│   │   ├── .env               # Environment-specific configurations
│   │   ├── db.py              # Database connection and settings
│   │   ├── logger.py          # Logging configuration
│   │   └── model.py           # Model configuration settings
│
│   ├── db/                    # Database Interaction Layer
│   │   ├── db_model.py        # SQLAlchemy ORM models
│   │   └── db_sqlite          # SQLite database storage
│
│   ├── models/                # Machine Learning Components
│   │   ├── pipe/              # Data Processing Pipeline
│   │   │   ├── data_collection.py   # Data acquisition
│   │   │   ├── data_preparation.py  # Data preprocessing
│   │   │   └── model.py             # Model training utilities
│   │   │
│   │   ├── model/             # Model Training and Management
│   │   │   ├── model.py       # Core model training logic
│   │   │   └── model_services.py  # Model loading and prediction services
│   │   │
│   │   └── model_services.py  # Additional model service layer
│
│   ├── logs/                  # Application Logging
│   │   └── app.log            # Centralized log file
│
│   └── runner.py              # Main application entry point
│
├── tests/                     # Unit Test Suite
│   ├── test_data_collection.py
│   ├── test_model_training.py
│   └── test_prediction.py
│
├── docs/                      #  ML Project Documentation
│   ├── architecture.md
│   └── usage_guide.md
│
├── .gitignore
├── README.md
├── Makefile
├── poetry.lock
└── pyproject.toml
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

## ML Project Development Workflow:
![workflow](./imgs/mlflow_diagram.png)

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
