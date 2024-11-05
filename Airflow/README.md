# Airflow Pipeline Setup and Usage

This document provides instructions for setting up, running, and troubleshooting the Airflow-based data pipeline for the **House Price Prediction MLOps** project. Apache Airflow orchestrates various ETL processes and machine learning workflows, ensuring modular, scalable, and efficient data processing.

---

## 1. Introduction

The Airflow pipeline automates the end-to-end data processing and machine learning workflow for the House Price Prediction project. Key stages in the pipeline include:
- **Data acquisition** from Google Cloud Storage (GCS)
- **Data preprocessing** (cleaning, validation, splitting)
- **Feature engineering** and **data augmentation**
- **Model training** and **evaluation**
- **Artifact storage** and version control using DVC

---

## 2. Pipeline Overview

The pipeline consists of modular DAGs (Directed Acyclic Graphs) that run specific tasks in a sequence to process data, train models, and track outputs. Each DAG is designed to operate independently, allowing for flexibility in updating and testing individual components.

### DAGs Included:
- **data_prep_dag**: Handles data loading, validation, cleaning, and splitting.
- **feature_and_augm_dag**: Performs feature engineering and data augmentation.

### Pipeline Flow Diagram:
![Pipeline Diagram](https://github.com/user-attachments/assets/a8ecfda0-bf73-4ce4-9c8c-46b162cf10a2)
![Pipeline Diagram](https://github.com/user-attachments/assets/cf91bad9-c892-41cb-9640-31a8ef25fee9)

---

## 3. Setup

### a. Prerequisites

- **Python 3.8+**
- **Apache Airflow** (version 2.x)
- **Docker** (if using Docker Compose for containerized Airflow)
- **Google Cloud SDK** (for integration with GCS and DVC)

### b. Environment Variables

To facilitate connections to GCS and manage Airflow configuration, add environment variables in a `.env` file within the `config/` folder. Key variables include:
- `GCP_PROJECT_ID`
- `GCS_BUCKET_NAME`
- `DVC_REMOTE_PATH`
- Additional Google Cloud credentials as needed

### c. Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone [REPO_URL]
   cd Airflow
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize Airflow**:
   - Set up the Airflow database, then start the scheduler and web server:
   ```bash
   airflow db init
   airflow scheduler &
   airflow webserver
   ```

4. **Docker Setup** (Optional):
   - If using Docker Compose, start Airflow services as follows:
   ```bash
   docker-compose up -d
   ```

5. **Configure DVC**:
   - Refer to the main project `README.md` for DVC setup instructions with Google Cloud.

---

## 4. Running the Pipeline

1. **Access the Airflow Web UI**:
   - Open `http://localhost:8080` in your browser to view your DAGs.

2. **Enable DAGs**:
   - In the Airflow UI, toggle the DAGs to enable them:
     - `data_prep_dag`: Manages data loading, cleaning, and splitting
     - `feature_and_augm_dag`: Conducts feature engineering and augmentation

3. **Trigger DAG Runs**:
   - Manually start a DAG run or configure a schedule in the DAG definitions as needed.

---

## 5. DAG Structure and Task Descriptions

### **data_prep_dag**
This DAG performs core data processing tasks:
- **Data Loading**: Loads raw data from GCS.
- **Data Validation**: Validates data schema and format.
- **Data Preprocessing**: Cleans missing values, encodes categorical data, and normalizes features.
- **Data Splitting**: Divides data into training, validation, and test sets.

### **feature_and_augm_dag**
This DAG is responsible for feature engineering and data augmentation:
- **Feature Engineering**: Applies transformations and extracts meaningful features.
- **Data Augmentation**: Expands the dataset using augmentation techniques to improve model robustness.

---

## 6. Troubleshooting and Common Issues

- **Airflow DAG Not Showing**: Ensure the `dags` folder is correctly set in `AIRFLOW_HOME`. Check for syntax errors in the DAG files.
- **GCS Permission Issues**: Verify that the GCP service account has access permissions to the specified GCS bucket.
- **Docker Errors**: If using Docker, confirm that the Docker daemon is running and `.env` variables are correctly configured.

---

## 7. Folder Structure (Airflow-Specific)

Here is an outline of the `Airflow` folder structure for easy reference:

```
Airflow
├── dags                   # Contains all DAG scripts
│   ├── __pycache__        # Python cache files
│   ├── data               # Data files required by DAGs
│   ├── src                # Source scripts for custom processing
│   │   ├── __init__.py
│   │   ├── data_augment.py
│   │   ├── data_prep.py
│   │   ├── data_splitting.py
│   │   ├── feature_select.py
│   │   └── label_encode.py
│   ├── __init__.py        # Initialization file for Airflow
│   ├── data_prep_dag.py   # DAG for data loading and preprocessing
│   └── feature_and_augm_dag.py  # DAG for feature engineering and augmentation
```

---

## 8. Testing and Validation

We use **GitHub Actions** to automate unit tests and validate each task within the DAGs. When changes are committed to the main branch, GitHub Actions triggers the tests and provides feedback on their results.

To run tests locally:
```bash
pytest tests/
```

![Unit Test Status](https://github.com/user-attachments/assets/74c31c68-e3ad-4c8e-ac46-17482e6718f7)

---

## 9. Resources and References

- **[Apache Airflow Documentation](https://airflow.apache.org/docs/)**: Official documentation for setting up and using Apache Airflow.
- **[Google Cloud SDK](https://cloud.google.com/sdk/docs)**: Guide for configuring GCS and managing data storage.
- **[DVC Documentation](https://dvc.org/doc)**: Guide for setting up DVC for data versioning.
