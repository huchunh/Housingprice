# House Price Prediction MLOps Project

A comprehensive MLOps pipeline for predicting house prices using advanced machine learning techniques and modern DevOps practices. [House Price Prediction App](https://house-price-app-752005993878.us-east1.run.app)

# Table of Contents
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

# Project Overview

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

# Project Structure

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

# Project Installation and Setup

### Prerequisites
- Python 3.8+
- Docker and Docker Compose
- Google Cloud SDK
- Apache Airflow
- MLflow

### Environment Variables

To facilitate connections to GCS and manage Airflow configuration, add environment variables in a `.env` file within the `config/` folder. Key variables include:
- `GCP_PROJECT_ID`
- `GCS_BUCKET_NAME`
- `DVC_REMOTE_PATH`
- Additional Google Cloud credentials as needed

# Airflow DAG Setup Steps

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
   - Refer to the main project `README.md` for DVC setup instructions with Google Cloud.## 4. Running the Pipeline

6. **Access the Airflow Web UI**:
   - Open `http://localhost:8080` in your browser to view your DAGs.

7. **Enable DAGs**:
   - In the Airflow UI, toggle the DAGs to enable them:
     - `data_prep_dag`: Manages data loading, cleaning, and splitting
     - `feature_and_augm_dag`: Conducts feature engineering and augmentation

8. **Trigger DAG Runs**:
   - Manually start a DAG run or configure a schedule in the DAG definitions as needed.
   - In this project, DAG is scheduled automatically trigger in one hour interval and push model to GCP in one and half hour interval

<img width="1426" alt="image" src="https://github.com/user-attachments/assets/4f8b5f1b-1a68-48f5-ab41-d392874a01a0">

<img width="1423" alt="feature selection" src="https://github.com/user-attachments/assets/5c7cd917-d90f-4a23-9dee-b3ab3430c481">

<img width="1422" alt="Screenshot 2024-12-07 at 11 20 13 AM" src="https://github.com/user-attachments/assets/051fa95c-dcb0-44f3-80fb-97213d5380d3">


9. **Troubleshooting and Common Issues**:

- **Airflow DAG Not Showing**: Ensure the `dags` folder is correctly set in `AIRFLOW_HOME`. Check for syntax errors in the DAG files.
- **GCS Permission Issues**: Verify that the GCP service account has access permissions to the specified GCS bucket.
- **Docker Errors**: If using Docker, confirm that the Docker daemon is running and `.env` variables are correctly configured.

# Unit tests set up
10. **Testing and Validation**:

We use **GitHub Actions** to automate unit tests and validate each task within the DAGs functions. When changes are committed to the main branch, GitHub Actions triggers the tests and provides feedback on their results.

- Create folder named tests under repo,create test tasks in tests folder name it <test> .py
- Based on data validation functions preset a simple dataset including all the anomalies and edge cases, using for testing DAG tasks functionalities.
- Create git action workflow .yml file under .github/workflows folder

To run tests locally:
```bash
pytest tests/
```
<img width="578" alt="image" src="https://github.com/user-attachments/assets/1f45ce59-b451-4a53-bbf6-3d2652c38c6b">

# **MLflow Set up**
In this project, we used MLflow within an Airflow container to track our machine learning experiments. We trained three models for predicting house prices using both categorical and numerical features:

Linear Regression
Random Forest
Elastic Net
After evaluating their performance, we found that the Random Forest model provided the best results for our dataset. All training runs, metrics, and artifacts were logged and visualized through the MLflow UI, which made it easy to compare the models and select the optimal one.

This guide explains how to run the **MLflow UI** from an Airflow container in a Dockerized environment. It assumes you already have an Airflow setup running using `docker-compose` and MLflow installed in the containers via `_PIP_ADDITIONAL_REQUIREMENTS`.
![image](https://github.com/user-attachments/assets/e0e1720d-b7f7-4f88-afbb-546535b91c5d)
![image](https://github.com/user-attachments/assets/d5bee6ac-93bd-4dfa-a1b0-0d92ef9c01b9)
![image](https://github.com/user-attachments/assets/750effb5-34bf-4c72-a9d9-7fb311b043d2)

---

#### **Prerequisites**

**Airflow Setup**: Ensure your Airflow containers are running and properly configured in the `docker-compose.yaml` file.
**MLflow Installed**: MLflow should be included in the `_PIP_ADDITIONAL_REQUIREMENTS` of your Airflow setup:
   ```yaml
   _PIP_ADDITIONAL_REQUIREMENTS: "mlflow pandas scikit-learn kneed google-cloud-storage"
   ```
**Shared Volume**: The `mlruns` directory should be mounted to `/opt/airflow/mlruns` for consistent tracking:
   ```yaml
   volumes:
     - ./mlruns:/opt/airflow/mlruns
   ```

---

#### **Steps to Run MLflow UI**

1. **Start Airflow Containers**
Start your Airflow setup:
```bash
docker-compose up -d
```

Ensure all containers are running:
```bash
docker ps
```

2.**Access the Desired Container**
Decide which Airflow container will host the MLflow UI. Typically, this will be the **worker** or **webserver** container. Enter the container:
```bash
docker exec -it airflow-airflow-worker-1 bash
```
*(Replace `airflow-airflow-worker-1` with the name of the desired container.)*

3. **Start the MLflow UI**
Inside the container, start the MLflow UI:
```bash
mlflow ui --backend-store-uri postgresql+psycopg2://airflow:airflow@postgres/mlflow --host 0.0.0.0
```

- **`--backend-store-uri`**: Specifies the location of the MLflow tracking directory.
- **`--host`**: Ensures the UI is accessible from outside the container.

4. **Access the MLflow UI**
The UI will be available at:
```
http://localhost:5000
```

If port **5000** is already in use, you can specify a different port:
```bash
mlflow ui --backend-store-uri file:///opt/airflow/mlruns --host 0.0.0.0 --port 5001
```
Ensure the port is mapped in your `docker-compose.yaml`:
```yaml
ports:
  - "5001:5001"
```

---

5. **Stopping the MLflow UI**

**If Running in the Foreground**
Stop the process by pressing:
```
Ctrl + C
```

**If Running in the Background**
Find the MLflow process ID (PID) and terminate it:
```bash
ps aux | grep 'mlflow'
kill <PID>
```

**Notes**

- For modular setups, consider running the MLflow UI in a dedicated container for better scalability and separation of concerns.
- Make sure the `mlruns` directory is shared between the container running the MLflow UI and the container where Airflow logs experiments.

---

#### **Troubleshooting**

**Cannot Access MLflow UI**:
   - Verify that port **5000** is mapped correctly in the `docker-compose.yaml`.
   - Check if another process is using port **5000**:
     ```bash
     sudo ss -tuln | grep 5000
     ```
**Permission Issues**:
   Ensure the `mlruns` directory has the correct permissions:
   ```bash
   chmod -R 755 ./mlruns
   ```

---

#### Troubleshooting `init-db.sh` Script in Docker Compose

This guide helps you troubleshoot issues related to the execution of the `init-db.sh` script in a Docker Compose setup, specifically for initializing a PostgreSQL database.

#### Common Issues and Resolutions

1.**File Permissions**
Ensure the `init-db.sh` file has executable permissions.

2.**Command to check permissions:**  
```bash
ls -l init-db.sh
```

Expected output:  
```bash
-rwxr-xr-x 1 user group size date init-db.sh
```

If permissions are incorrect, run:  
```bash
chmod +x init-db.sh
```

# Data Validation and Data Shift Detection

To ensure high-quality data processing and robust model training, the project incorporates automated **Data Validation** and **Data Shift Detection** mechanisms. These processes leverage **TensorFlow Data Validation (TFDV)** and custom Cloud Functions integrated with **Google Pub/Sub** for real-time tracking of changes to the data folder in the GCS bucket. Notifications are sent via email for critical events.

![image](https://github.com/user-attachments/assets/a4199b64-e6be-4a0c-876c-fed11986d7ba)


---

### Data Validation using TFDV

We use **TensorFlow Data Validation (TFDV)** to validate the dataset during the preprocessing pipeline. TFDV automatically analyzes the dataset to detect anomalies, inconsistencies, and schema violations.

![image](https://github.com/user-attachments/assets/02c56254-e950-463e-b864-cb456579453e)


#### Key Features:
- **Schema Generation**: Defines expected feature types, value ranges, and distributions.
- **Anomaly Detection**: Identifies:
  - Missing or unexpected values.
  - Type mismatches (e.g., numerical features containing non-numeric values).
  - Distributional anomalies (e.g., significant deviations in feature distributions).
- **Statistics Comparison**: Ensures consistency with historical data by comparing feature statistics (mean, median, standard deviation).

#### Workflow:
1. During the **data preprocessing pipeline**, TFDV analyzes the dataset and validates it against the schema.
2. Anomalies detected by TFDV are logged, and an email notification is sent for critical issues.
3. If no anomalies are found, the pipeline proceeds to the next stage.

---

### Data Shift Detection using Cloud Functions

To maintain model reliability, we monitor the **data folder** in the GCS bucket for changes (additions or deletions). A custom **Google Cloud Function** tracks these events in real-time and evaluates potential data drift.

![image](https://github.com/user-attachments/assets/4a57684f-d84a-411a-9841-3fc859796662)


#### Pub/Sub Integration:
- A **Pub/Sub topic** is configured to monitor the `data/` folder in the GCS bucket.
- Whenever a new file is added or an existing file is deleted, a message is published to the Pub/Sub topic, triggering the **Data Shift Detection Cloud Function**.

#### Data Drift Detection:
- The Cloud Function compares the statistics of the newly added file with a reference dataset using statistical tests:
  - **Kolmogorov-Smirnov Test**: For numerical features.
  - **Chi-Squared Test**: For categorical features.
- Drift detection logic identifies significant deviations in feature distributions, indicating potential issues with the data pipeline.

#### Workflow:
1. **File Added to GCS**: When a new file is added to the `data/` folder, the Cloud Function:
   - Downloads the new file and the reference dataset.
   - Generates feature statistics for both datasets.
   - Detects drift using statistical tests.
2. **File Deleted from GCS**: If a file is removed, the function logs the event and sends an email notification.

---

# Email Notifications

The Cloud Functions and TFDV processes are configured to send email alerts for critical events:
- **Data Validation Anomalies**:
  - Schema violations (e.g., unexpected feature types).
  - Missing or out-of-range values.
    ![image](https://github.com/user-attachments/assets/8644ff1a-d9a6-4224-abe9-84382b040075)

- **Data Drift Detection**:
  - Significant drift in feature distributions.
  - Notifications include a summary of drifted features and the corresponding p-values.
    ![image](https://github.com/user-attachments/assets/2d6eac52-bbce-40bf-a9fa-98e096fe61c5)

- **File Addition/Deletion**:
  - Alerts are sent whenever files are added to or removed from the `data/` folder.
 
 # DVC Set Up

This project uses Data Version Control (DVC) to manage datasets and track changes efficiently. Below is the directory structure and description of each component in this project.

#### Directory Structure

```plaintext
project_dvc/                  # Root folder for the DVC project
├── .dvc/                      # DVC configuration folder
│   ├── config.txt             # DVC configuration file
│   └── gitignore.txt          # Git ignore settings for DVC files
├── data/                      # Data folder containing datasets and version files
│   ├── AmesHousing.csv.dvc    # DVC-tracked file for the Ames Housing dataset
│   ├── cleaned_data.csv.dvc   # DVC-tracked file for the cleaned dataset
│   ├── encoding_data.csv.dvc  # DVC-tracked file for the encoded dataset
│   ├── gitignore.txt          # Git ignore file specific to the data folder
│   └── dvcignore.txt          # DVC ignore file for excluding certain files from DVC tracking
```

#### Description of Files and Folders

- **project_dvc/**: The main directory of the project where all DVC-related files are stored.
  
- **.dvc/**: Contains DVC configuration and settings files.
  - **config.txt**: Configuration file that includes the settings for DVC in this project.
  - **gitignore.txt**: Specifies files and directories that Git should ignore in the `.dvc` folder.
  
- **data/**: This folder contains the datasets used in the project, all tracked by DVC.
  - **AmesHousing.csv.dvc**: DVC-tracked file for the original Ames Housing dataset.
  - **cleaned_data.csv.dvc**: DVC-tracked file for the cleaned version of the dataset after preprocessing.
  - **encoding_data.csv.dvc**: DVC-tracked file for the dataset after encoding categorical variables.
  - **gitignore.txt**: File to specify files in the `data` folder that Git should ignore.
  - **dvcignore.txt**: File to specify files in the `data` folder that DVC should ignore.

#### Set Up

1. **Setting Up DVC**:
   - Ensure DVC is installed by running `pip install dvc`.
   - Initialize DVC in the project (if not already done) using `dvc init`.

2. **Adding Data Files**:
   - Place raw and processed datasets in the `data/` folder.
   - Track each dataset with DVC by running `dvc add data/<filename>`.
   - This creates `.dvc` files (e.g., `AmesHousing.csv.dvc`) that reference the version-controlled data.

3. **Using gitignore.txt and dvcignore.txt**:
   - `gitignore.txt` is used to prevent specific files in `data/` from being tracked by Git.
   - `dvcignore.txt` helps DVC to ignore files or directories in `data/` that you do not want to track.

4. **Pushing Data to Remote Storage**:
   - Configure a remote storage for DVC using `dvc remote add -d <remote-name> <remote-url>`.
   - Push the data to the remote storage with `dvc push` to back up your datasets.

5. **Pulling Data**:
   - To retrieve data from the remote storage, use `dvc pull`.

## Notes

- Ensure that both `gitignore.txt` and `dvcignore.txt` are properly configured to exclude unnecessary files from version control.
- For collaborative projects, share `.dvc` files and configuration, allowing others to reproduce your work by using `dvc pull` to fetch the data.


# Methodology for House Price Prediction

### Dataset Overview
- **Dimensions**: 82 columns, 2930 rows
- **Data Types**:
  - `float64`: 11 columns
  - `int64`: 28 columns
  - `object`: 43 columns
- **Feature Mix**: Balanced combination of quantitative (e.g., year built, fireplaces) and qualitative variables (e.g., heating quality, exterior quality) For detailed data definitions, refer to this [Data Definition Document](https://docs.google.com/spreadsheets/d/1XL6LJVgLLU27yV7a_oh2zuqhGOI3Syg-jWpmr0Ekk14/edit?usp=sharing).

### Data Processing Pipeline

![Pipeline Diagram](https://github.com/user-attachments/assets/55121bb8-6b69-4101-ba7b-37ae5d89cab9)

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
<img width="1386" alt="Screenshot 2024-12-07 at 11 19 43 AM" src="https://github.com/user-attachments/assets/be5c830f-c024-47c7-8be1-890778d6faf4">

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
