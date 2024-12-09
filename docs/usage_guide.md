# Usage Guide for Rental Price Prediction Project

This guide provides a walkthrough for setting up, configuring, and running the **Rental Price Prediction** project. The project is designed with modularity and scalability in mind, ensuring ease of use for both development and production environments.

---

## Project Structure

```plaintext
.github/
  └── actions/
  └── workflows/       # CI/CD workflows for automated testing and deployment
src/
  ├── config/          # Configuration management (e.g., database, logging, environment variables)
  ├── db/              # Database access and management
  ├── logs/            # Centralized logging files
  ├── model/           # Machine Learning model modules (training, inference, etc.)
  └── runner.py        # Main entry point for running the project
Makefile               # Commands for setup, testing, and deployment automation
poetry.lock            # Poetry lock file for dependency management
pyproject.toml         # Poetry project configuration
setup.cfg              # Additional setup configuration
```


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

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <[repository_url](https://github.com/Mohammed-abdulaziz-eisa/Rental-Price-Prediction-End-to-End-MLOps-Project.git)>
cd rental-price-prediction
```

### 2. Install Dependencies

- Use Poetry to install the required Python packages:

```bash
poetry install
```

### 3. Set Up Environment Variables

- Create a .env file in the `src/config` directory with the required configurations:

```bash
touch src/config/.env
```

- Fill in the variables with your database credentials and other relevant environment variables.

```bash
DATABASE_URL=<your_database_url>
LOGGING_LEVEL=INFO
MODEL_PATH=src/model/<trained_model_file>.pkl
```

## Usage

### 1. Running the Application

- Run the `src/runner.py` script to start the application:
```bash
poetry run python3 src/runner.py
```
or using makefile:
```bash
make runner
```

This will:

 - Load configurations.
 - Initialize the database.
 - Start the model for predictions or training (based on the mode).