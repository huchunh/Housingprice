# Airflow Pipeline Documentation

This guide provides comprehensive instructions for setting up and managing the Apache Airflow pipeline in the House Price Prediction MLOps project. The pipeline orchestrates data processing, model training, and monitoring workflows.

## Table of Contents
1. [Pipeline Overview](#pipeline-overview)
2. [Setup Instructions](#setup-instructions)
3. [Pipeline Components](#pipeline-components)
4. [MLflow Integration](#mlflow-integration)
5. [Troubleshooting](#troubleshooting)

## Pipeline Overview

The Airflow pipeline automates the following processes:
- Data acquisition from GCS
- Data preprocessing and validation
- Feature engineering
- Model training and evaluation
- Performance monitoring

### Pipeline Architecture
```
Data Source → Preprocessing → Feature Engineering → Model Training → Evaluation
     ↓             ↓               ↓                    ↓             ↓
   [GCS]     [Data Validation]  [Feature      [Model Training    [Performance
                                Selection]     with MLflow]       Monitoring]
```

## Setup Instructions

### Prerequisites
- Python 3.8+
- Docker and Docker Compose
- Google Cloud SDK
- MLflow

### Installation Steps

1. **Environment Setup**
   ```bash
   # Create virtual environment
   python -m venv venv
   source venv/bin/activate

   # Install dependencies
   pip install -r requirements.txt
   ```

2. **Configure Environment Variables**
   ```bash
   # Create .env file
   cp config/example.env config/.env

   # Add required variables
   GCP_PROJECT_ID=your-project-id
   GCS_BUCKET_NAME=your-bucket
   MLFLOW_TRACKING_URI=postgresql+psycopg2://airflow:airflow@postgres/mlflow
   ```

3. **Initialize Airflow**
   ```bash
   # Initialize database
   airflow db init

   # Create admin user
   airflow users create \
     --username admin \
     --password admin \
     --firstname Anonymous \
     --lastname Admin \
     --role Admin \
     --email admin@example.com
   ```

4. **Start Services**
   ```bash
   # Using Docker Compose
   docker-compose up -d
   ```

## Pipeline Components

### DAG Structure
```
Airflow/
├── dags/
│   ├── data_prep_dag.py        # Data preprocessing
│   └── feature_and_augm_dag.py # Feature engineering
├── src/
│   ├── data_augment.py
│   ├── data_prep.py
│   ├── feature_select.py
│   └── label_encode.py
```

### DAG Descriptions

1. **data_prep_dag**
   - Data loading from GCS
   - Data validation and cleaning
   - Train/test splitting
   - Schema validation

2. **feature_and_augm_dag**
   - Feature engineering
   - Data augmentation
   - Feature selection

## MLflow Integration

### Setup MLflow UI in Airflow Container

1. **Access Container**
   ```bash
   docker exec -it airflow-airflow-worker-1 bash
   ```

2. **Start MLflow UI**
   ```bash
   mlflow ui --backend-store-uri postgresql+psycopg2://airflow:airflow@postgres/mlflow --host 0.0.0.0
   ```

3. **Access MLflow UI**
   ```bash
   # Default port (5000)
   http://localhost:5000

   # If port 5000 is in use, start MLflow with a different port
   mlflow ui --backend-store-uri file:///opt/airflow/mlruns --host 0.0.0.0 --port 5001

   # Ensure your docker-compose.yaml includes the port mapping:
   # services:
   #   mlflow:
   #     ports:
   #       - "5001:5001"
   ```

   **Note**: If changing ports, remember to:
   1. Update the MLflow UI startup command with the new port
   2. Add the corresponding port mapping in docker-compose.yaml
   3. Access the UI at the new port (e.g., `http://localhost:5001`)

### Stopping MLflow UI

1. **If Running in Foreground**
   ```bash
   # Press Ctrl + C
   ```

2. **If Running in Background**
   ```bash
   # Find MLflow process
   ps aux | grep 'mlflow'
   
   # Terminate the process
   kill <PID>
   ```

### MLflow Integration Notes
- Consider running MLflow UI in a dedicated container for better scalability
- Ensure `mlruns` directory is shared between MLflow UI and Airflow containers
- Monitor experiment tracking and model versioning through the UI

![MLflow Dashboard](https://github.com/user-attachments/assets/e0e1720d-b7f7-4f88-afbb-546535b91c5d)
![MLflow Experiments](https://github.com/user-attachments/assets/d5bee6ac-93bd-4dfa-a1b0-0d92ef9c01b9)
![MLflow Models](https://github.com/user-attachments/assets/750effb5-34bf-4c72-a9d9-7fb311b043d2)

### Experiment Tracking
- Model parameters and metrics logged automatically
- Artifacts stored in GCS
- Performance visualization in MLflow UI

## Troubleshooting

### Common Issues

1. **Database Initialization**
   ```bash
   # Check database status
   docker exec -it airflow-postgres-1 psql -U airflow
   \l
   ```

2. **Permission Issues**
   ```bash
   # Fix script permissions
   chmod +x init-db.sh
   ```

3. **MLflow UI Access**
   ```bash
   # Check port availability
   sudo ss -tuln | grep 5000
   ```

### Database Setup Script
```bash
#!/bin/bash
if [ ! -f "/var/lib/postgresql/data/.db_initialized" ]; then
  echo "Initializing database..."
  psql -U airflow -c "CREATE DATABASE mlflow;"
  psql -U airflow -c "GRANT ALL PRIVILEGES ON DATABASE mlflow TO airflow;"
  touch /var/lib/postgresql/data/.db_initialized
fi
```

## Additional Resources

- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [MLflow Documentation](https://www.mlflow.org/docs/latest/index.html)
- [Google Cloud SDK Documentation](https://cloud.google.com/sdk/docs)
