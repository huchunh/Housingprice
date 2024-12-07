# House Price Prediction MLOps Project

A comprehensive MLOps pipeline for predicting house prices using advanced machine learning techniques and modern DevOps practices. [House Price Prediction App](https://house-price-app-752005993878.us-east1.run.app)

## Table of Contents
1. [Project Overview](#project-overview)
2. [System Architecture](#system-architecture)
3. [Installation and Setup](#installation-and-setup)
4. [Project Structure](#project-structure)
5. [Pipeline Components](#pipeline-components)
6. [Model Development and Methodology](#model-development-and-methodology)
7. [MLflow Integration](#mlflow-integration)
8. [Data Management](#data-management)
9. [Production Deployment](#production-deployment)
10. [References and Resources](#references-and-resources)
11. [Contributing](#contributing)
12. [Contact Information](#contact-information)

## Project Overview

This project implements a production-grade machine learning pipeline for house price prediction, integrating:
- Automated data processing and validation
- Model training and evaluation
- Continuous deployment
- Real-time monitoring
- Data version control

### Key Features
- Data processing pipeline using Apache Airflow
- Experiment tracking with MLflow
- Data version control using DVC
- Automated testing with GitHub Actions
- Real-time data validation using TensorFlow Data Validation (TFDV)
- Model deployment via Google Cloud Run

### System Architecture

```
Data Source → Preprocessing → Feature Engineering → Model Training → Evaluation
     ↓             ↓               ↓                    ↓             ↓
   [GCS]     [Data Validation]  [Feature      [Model Training    [Performance
                                Selection]     with MLflow]       Monitoring]
```

## Installation and Setup

### Prerequisites
- Python 3.8+
- Docker and Docker Compose
- Google Cloud SDK
- Apache Airflow
- MLflow

### Setup Steps

1. **Clone Repository**
   ```bash
   git clone https://github.com/your_username/House_Price_Prediction_MLOps.git
   cd House_Price_Prediction_MLOps
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment**
   ```bash
   # Create .env file
   cp config/example.env config/.env

   # Add required variables
   GCP_PROJECT_ID=your-project-id
   GCS_BUCKET_NAME=your-bucket
   MLFLOW_TRACKING_URI=postgresql+psycopg2://airflow:airflow@postgres/mlflow
   ```

4. **Initialize Services**
   ```bash
   # Initialize Airflow database
   airflow db init
   
   # Start Airflow services
   docker-compose up -d
   ```

## Project Structure

```
House_Price_Prediction_MLOps/
├── .github/workflows/           # GitHub Actions workflows
│   ├── ci-unittest.yml
│   └── lightweight_dag_test.yml
├── Airflow/                     # Airflow configuration and DAGs
│   ├── dags/
│   │   ├── data/
│   │   ├── src/
│   │   │   ├── __pycache__/                    # Compiled Python files
│   │   │   ├── __init__.py                     # Package initializer
│   │   │   ├── bias_detection.py               # Bias detection script
│   │   │   ├── data_augment.py                 # Data augmentation methods
│   │   │   ├── data_prep.py                    # Data preparation utilities
│   │   │   ├── data_splitting.py               # Dataset splitting logic
│   │   │   ├── feature_select.py               # Feature selection logic
│   │   │   ├── label_encode.py                 # Label encoding methods
│   │   │   ├── mlflow_model_deploy.py          # MLflow model deployment script
│   │   │   ├── model_elastic_net.py            # Elastic Net regression model
│   │   │   ├── model_linear_regression.py      # Linear regression model
│   │   │   ├── model_rf.py                     # Random Forest model
│   │   │   ├── one_hot_encoder.py              # One-hot encoding methods
│   │   ├── __init__.py                      # Package initializer
│   │   ├── data_prep_dag.py
│   │   ├── feature_and_augm_dag.py
│   │   ├── mlflow_model_deploy_dag.py  
│   │   └── modeling_and_eval_dag.py   
│   ├── mlruns/                  # MLflow tracking
│   │   └──model
│   │   │   ├── conda.yaml                   # Conda environment configuration
│   │   │   ├── MLmodel                      # MLflow model file
│   │   │   ├── model.pkl                    # Serialized model file
│   │   │   ├── python_env.yaml              # Python environment dependencies
│   │   │   ├── requirements.txt             # Python package requirements
│   |   └── feature_importance.csv           # CSV file containing feature importance scores
│   ├── scripts/
│   └── docker-compose.yaml
├── Methodology/                 # Project methodology docs
├── project_dvc/                 # DVC configuration
└── tests/                       # Project tests
```



## Model Development and Methodology

### Dataset Overview
- **Dimensions**: 82 columns, 2930 rows
- **Data Types**:
  - `float64`: 11 columns
  - `int64`: 28 columns
  - `object`: 43 columns
- **Feature Mix**: Balanced combination of quantitative (e.g., year built, fireplaces) and qualitative variables (e.g., heating quality, exterior quality)

### Data Processing Pipeline

1. **Data Validation and Cleaning**
   - Outlier removal: Houses > 4000 square feet excluded
   - Data corrections: Fixed anomalies (e.g., garage year 2207 → 2007)
   - Duplicate check: No duplicates found

2. **Missing Value Treatment**
   - **Numerical Variables**:
     - Zero imputation for structural features (e.g., basement bathrooms)
     - Median imputation for continuous features (e.g., lot frontage)
   - **Categorical Variables**:
     - Standardized all NA/empty/None values to "Missing"

3. **Feature Engineering and Selection**
   - **Correlation Analysis**:
     - Pearson correlation threshold: 0.3
     - Selected features with significant relationship to SalePrice
   
   - **Lasso-based Selection**:
     - LassoCV for optimal regularization
     - Importance threshold: 0.1
     - Validated correlation-based selection

4. **Data Augmentation**
   - Custom `augment_data_with_perturbations` function
   - Perturbation range: 2% of original values
   - Generated 2000 synthetic records
   - Applied only to training data

### Model Selection and Development

1. **Model Experimentation**
   - Tested multiple architectures:
     - Regression models (Linear, Lasso)
     - Tree-based models (Random Forest)
     - Neural networks
   
2. **Final Model Selection**
   - Primary models chosen:
     - **Lasso Regression**: For interpretability and feature selection
     - **Tree-based Models**: For handling non-linear relationships
   - Selection criteria:
     - Model interpretability
     - Prediction performance
     - Training efficiency

3. **Model Optimization**
   - Hyperparameter tuning for each model
   - Cross-validation for stability
   - Regularization to prevent overfitting

4. **Evaluation Framework**
   - Key Metrics:
     - **RMSE (Root Mean Squared Error)**:
       - Measures prediction accuracy
       - Penalizes larger errors
     - **MAE (Mean Absolute Error)**:
       - Provides average error magnitude
       - More robust to outliers
   - Performance monitoring through MLflow
   - Regular model retraining based on metrics

## Production Deployment

1. **Web Application**
   - **URL**: [House Price Prediction App](https://house-price-app-752005993878.us-east1.run.app)
   - **Platform**: Google Cloud Run
   - **Features**: 
     - Real-time predictions
     - Interactive interface
     - Automated monitoring

2. **Performance Tracking**
   - Continuous metric monitoring
   - Automated retraining triggers
   - Drift detection alerts

3. **Results**
   - Optimal accuracy-complexity balance
   - Enhanced model robustness
   - Reproducible evaluation framework

## References and Resources

1. **Data Documentation**
   - [Ames Housing Dataset Definition Document](https://docs.google.com/spreadsheets/d/1XL6LJVgLLU27yV7a_oh2zuqhGOI3Syg-jWpmr0Ekk14/edit?usp=sharing)
   - [Original Data Documentation and Methodology](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt)

2. **Technical Resources**
   - Feature Selection Techniques
   - Data Augmentation Methods
   - Model Validation Approaches

3. **Project Documentation**
   - Detailed methodology in `/Methodology`
   - Pipeline documentation in `/Airflow`
   - Model specifications in MLflow

## Contributing

We welcome contributions! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## Contact Information

- Aliya: 26aly000@gmail.com
- Changping Chen: champing1409@gmail.com
- Krishna Priya Gitalaxmi: gitakrishnapriya@gmail.com
- Qi An: an.qi2@northeastern.edu
- Ziqi Li: zql04150415@gmail.com
