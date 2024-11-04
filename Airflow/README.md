# Airflow Pipeline Setup and Usage

This document provides instructions for setting up, running, and troubleshooting the Airflow-based data pipeline. This pipeline orchestrates various ETL processes and ML workflows, ensuring modular, scalable, and efficient data processing.

## 1. Overview

The Airflow pipeline is used to automate the end-to-end data processing and machine learning workflow for the project. It includes tasks for:
- Data acquisition from Google Cloud Storage
- Data preprocessing, feature engineering, and splitting
- Model training and evaluation
- Version control and artifact storage using DVC

## 2. Project Structure

```
Airflow
├── dags                 # Folder containing Airflow DAGs
│   ├── airflowdag.py    # Main DAG definition
│   └── feature_and_augm_dag.py   # DAG for feature engineering and augmentation
├── __pycache__          # Folder for cached Python files
├── config               # Config files for environment variables, Airflow settings
│   └── .env             # Environment variables
└── logs                 # Log files for tracking DAG runs
```

## 3. Prerequisites

### a. Software Requirements
- **Python 3.8+**
- **Apache Airflow**: Version 2.x
- **Docker** (if using Docker Compose)
- **Google Cloud SDK** (for GCS and DVC integration)

### b. Environment Variables
Place environment variables in the `.env` file under the `config` folder. Required variables include:
- `GCP_PROJECT_ID`
- `GCS_BUCKET_NAME`
- `DVC_REMOTE_PATH`
- Additional credentials for Google Cloud

## 4. Setup

### a. Install Dependencies

1. **Clone the repository** and navigate to the Airflow directory.
   ```bash
   git clone [REPO_URL]
   cd Airflow
   ```

2. **Install Python dependencies**.
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Airflow**: Initialize the Airflow database and start the scheduler and web server.
   ```bash
   airflow db init
   airflow scheduler
   airflow webserver
   ```

4. **Docker Setup** (Optional): If using Docker Compose, follow these steps:
   ```bash
   docker-compose up -d
   ```

### b. Configure DVC for Data Version Control
Follow the steps in the main project `README.md` to set up DVC with Google Cloud.

## 5. Running the Pipeline

1. **Access the Airflow Web UI**: Navigate to `http://localhost:8080` to view your DAGs.
2. **Enable DAGs**: Toggle the DAGs you want to activate, including:
   - `airflowdag`: Main pipeline DAG
   - `feature_and_augm_dag`: Feature engineering and augmentation DAG
3. **Trigger DAG Runs**: You can start a DAG run manually or configure a schedule in the DAG definitions.

## 6. DAG Structure and Task Descriptions

### airflowdag
This DAG orchestrates the main data pipeline tasks:
- **Data Loading**: Loads raw data from GCS.
- **Data Validation**: Ensures data integrity by checking schema and formats.
- **Data Preprocessing**: Handles missing values, encoding, and scaling.
- **Data Splitting**: Splits data into train, validation, and test sets.

### feature_and_augm_dag
This DAG handles feature engineering tasks:
- **Feature Engineering**: Applies transformations and feature extraction.
- **Data Augmentation**: Expands the dataset with augmented samples.

## 7. Testing and Validation

We use GitHub Actions to run unit tests for each task. When functions are merged into the main branch, unit tests trigger automatically, providing feedback on the pipeline's functionality.

To run tests locally:
```bash
pytest tests/
```

## 8. Troubleshooting

- **Airflow DAG Not Showing**: Ensure the `dags` folder is correctly set in your `AIRFLOW_HOME` and the DAG files are syntactically correct.
- **GCS Permission Issues**: Confirm that your GCP service account has access to the specified GCS bucket.
- **Docker Setup Errors**: Check that the Docker daemon is running and the `.env` file is correctly configured.

## 9. Resources and References

- **[Apache Airflow Documentation](https://airflow.apache.org/docs/)**: Official Airflow documentation.
- **[Google Cloud SDK](https://cloud.google.com/sdk/docs)**: Instructions for setting up GCS and managing data.
- **[DVC Documentation](https://dvc.org/doc)**: Guide for setting up DVC for data version control.

