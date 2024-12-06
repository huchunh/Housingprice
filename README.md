# House Price Prediction MLOps Project

A comprehensive MLOps pipeline for predicting house prices using advanced machine learning techniques and modern DevOps practices.

## Table of Contents
1. [Project Overview](#project-overview)
2. [System Architecture](#system-architecture)
3. [Installation and Setup](#installation-and-setup)
4. [Project Structure](#project-structure)
5. [Pipeline Components](#pipeline-components)
6. [MLflow Integration](#mlflow-integration)
7. [Data Management](#data-management)
8. [Model Development](#model-development)
9. [Monitoring and Validation](#monitoring-and-validation)
10. [Troubleshooting Guide](#troubleshooting-guide)
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

### Deployed Application
- **Application URL**: [House Price Prediction App](https://house-price-app-752005993878.us-east1.run.app)
- **Platform**: Google Cloud Run
- **Features**: Real-time predictions, interactive interface

## System Architecture

### Pipeline Overview
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
├── .github/workflows/            # GitHub Actions workflows
│   ├── ci-unittest.yml
│   └── lightweight_dag_test.yml
├── Airflow/                      # Airflow configuration and DAGs
│   ├── dags/
│   │   ├── data/
│   │   ├── src/
│   │   │   ├── data_prep_dag.py
│   │   │   ├── feature_and_augm_dag.py
│   │   │   ├── mlflow_model_deploy_dag.py
│   │   │   └── modeling_and_eval_dag.py
│   ├── mlruns/                   # MLflow tracking
│   ├── scripts/
│   └── docker-compose.yaml
├── Methodology/                  # Project methodology docs
├── project_dvc/                  # DVC configuration
└── tests/                        # Project tests
```

## Pipeline Components

### 1. Data Processing
- Data validation and cleaning
- Feature engineering
- Data augmentation
- Train/test splitting

### 2. Model Development
Three primary models implemented:
- Linear Regression (baseline)
- Random Forest
- Elastic Net

### 3. MLflow Integration

#### Setup MLflow UI
1. **Access Container**
   ```bash
   docker exec -it airflow-airflow-worker-1 bash
   ```

2. **Start MLflow UI**
   ```bash
   mlflow ui --backend-store-uri postgresql+psycopg2://airflow:airflow@postgres/mlflow --host 0.0.0.0
   ```

3. **Access UI**
   ```bash
   # Default port (5000)
   http://localhost:5000
   ```

#### MLflow Dashboard Views
![MLflow Dashboard](https://github.com/user-attachments/assets/e0e1720d-b7f7-4f88-afbb-546535b91c5d)
![MLflow Experiments](https://github.com/user-attachments/assets/d5bee6ac-93bd-4dfa-a1b0-0d92ef9c01b9)
![MLflow Models](https://github.com/user-attachments/assets/750effb5-34bf-4c72-a9d9-7fb311b043d2)

## Data Management

### DVC Integration
1. **Initialize DVC**
   ```bash
   dvc init
   ```

2. **Add Data**
   ```bash
   dvc add data/raw/ames_housing.csv
   dvc push
   ```

### Data Validation and Drift Detection

![Data Validation Architecture](https://github.com/user-attachments/assets/a4199b64-e6be-4a0c-876c-fed11986d7ba)

#### Validation Components
1. **TFDV Pipeline**
   ![TFDV Dashboard](https://github.com/user-attachments/assets/02c56254-e950-463e-b864-cb456579453e)
   - Schema generation
   - Anomaly detection
   - Statistical validation

2. **Drift Detection**
   ![Drift Detection](https://github.com/user-attachments/assets/4a57684f-d84a-411a-9841-3fc859796662)
   - Real-time monitoring
   - Statistical testing
   - Automated alerts

#### Notification System
![Validation Alert](https://github.com/user-attachments/assets/8644ff1a-d9a6-4224-abe9-84382b040075)
![Drift Alert](https://github.com/user-attachments/assets/2d6eac52-bbce-40bf-a9fa-98e096fe61c5)

## Troubleshooting Guide

### MLflow Issues

1. **UI Access Problems**
   ```bash
   # Check port availability
   sudo ss -tuln | grep 5000
   ```

2. **Permission Issues**
   ```bash
   chmod -R 755 ./mlruns
   ```

### Database Issues

1. **Check Database Initialization**
   ```bash
   docker exec -it airflow-postgres-1 psql -U airflow
   \l
   ```

2. **Script Permissions**
   ```bash
   chmod +x init-db.sh
   ```

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
