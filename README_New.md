
# House Price Prediction MLOps Project

This project implements a robust **Machine Learning Operations (MLOps)** pipeline for predicting house prices. The pipeline integrates **Apache Airflow** for workflow orchestration, **Google Cloud Platform (GCP)** for data management, and **Data Version Control (DVC)** for dataset and model versioning. The primary dataset is the **Ames Housing Dataset**, enhanced with additional features to improve prediction accuracy and robustness.

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Folder Structure](#folder-structure)  
3. [Installation and Setup](#installation-and-setup)  
4. [Pipeline Workflow](#pipeline-workflow)  
5. [Methodology](#methodology)  
6. [Testing and Validation](#testing-and-validation)  
7. [Troubleshooting and Common Issues](#troubleshooting-and-common-issues)  
8. [Contributing](#contributing)  
9. [Contact Information](#contact-information)  

---

## Project Overview

The goal of this project is to automate the end-to-end process of predicting house prices, including:

- **Data Acquisition**: Retrieving property data from Google Cloud Storage (GCS).  
- **Data Preprocessing**: Cleaning, validating, and transforming raw data.  
- **Feature Engineering and Augmentation**: Extracting meaningful features and generating synthetic data for better generalization.  
- **Model Training and Evaluation**: Training models using regression, tree-based algorithms, and deep learning techniques.  
- **Artifact Management**: Using DVC to version datasets and models.  
- **CI/CD Integration**: Leveraging GitHub Actions for automated testing and deployment.

**Key Features**:  
- Modular and scalable pipeline with **Apache Airflow**.  
- Comprehensive data management using **GCP**.  
- Reproducibility ensured by **DVC**.  
- Continuous integration and monitoring via **GitHub Actions**.

---

## Folder Structure

```plaintext
House_Price_Prediction_MLOps/
├── Airflow/               # Airflow DAGs and orchestration scripts
│   ├── dags/              # Definitions of Airflow DAGs
│   ├── src/               # Task-specific Python scripts
├── project_dvc/           # DVC configuration and data versioning
├── Methodology/           # Detailed documentation on modeling and feature engineering
├── tests/                 # Unit tests for pipeline components
├── images/                # Diagrams and visualizations
└── README.md              # Main project documentation
```

---

## Installation and Setup

### Prerequisites

- **Python 3.8+**  
- **Apache Airflow 2.x**  
- **DVC**  
- **Google Cloud SDK**  
- **Docker** (optional)

### Steps

1. **Clone the Repository**:  
    ```bash
    git clone https://github.com/your_username/House_Price_Prediction_MLOps.git
    cd House_Price_Prediction_MLOps
    ```

2. **Install Dependencies**:  
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Environment Variables**:  
    Create a `.env` file with the following values:
    ```plaintext
    GCP_PROJECT_ID=your_project_id
    GCS_BUCKET_NAME=your_bucket_name
    DVC_REMOTE_PATH=your_remote_path
    ```

4. **Initialize Airflow**:  
    ```bash
    airflow db init
    airflow scheduler &
    airflow webserver
    ```

5. **Initialize DVC**:  
    ```bash
    dvc init
    ```

---

## Pipeline Workflow

The pipeline is orchestrated with **Apache Airflow**, consisting of multiple modular DAGs:

1. **Data Acquisition and Preprocessing**:
   - Retrieve raw data from GCS.
   - Validate schema, clean missing values, and split datasets.

2. **Feature Engineering and Data Augmentation**:
   - Perform feature transformations and create synthetic records to improve model robustness.

3. **Model Training and Evaluation**:
   - Train and evaluate models using various algorithms.
   - Metrics include **RMSE** and **MAE**.

4. **Version Control with DVC**:
   - Track data and model changes.
   - Sync datasets with remote storage.

### Pipeline Diagram

![Pipeline Diagram](https://github.com/user-attachments/assets/55121bb8-6b69-4101-ba7b-37ae5d89cab9)

---

## Methodology

### Data Processing

1. **Outlier Removal**:
   - Remove records with extreme values (e.g., houses >4000 sq. ft.).

2. **Handling Missing Values**:
   - Fill numerical fields with `0` or median values.
   - Standardize categorical fields by encoding "Missing".

3. **Validation**:
   - Use schema checks to ensure data consistency.

### Feature Engineering

- Transform quality-related features into numeric scales (e.g., 1-5).  
- Generate augmented datasets with slight perturbations to key features.

### Model Selection

- Compare **Lasso Regression**, **tree-based models**, and **deep learning models**.  
- Refine feature selection using Lasso regularization.

---

## Testing and Validation

**GitHub Actions** automates testing to ensure pipeline reliability. Key test stages include:

1. **Unit Tests**: Validates the functionality of individual pipeline components.  
2. **Integration Tests**: Checks compatibility between pipeline stages.

**Run Tests Locally**:  
```bash
pytest tests/
```

![Unit Test Results](https://github.com/user-attachments/assets/74c31c68-e3ad-4c8e-ac46-17482e6718f7)

---

## Troubleshooting and Common Issues

- **DAG Not Displaying**: Ensure the `dags/` directory path is set in `AIRFLOW_HOME`.  
- **Permission Errors**: Verify that the GCP service account has correct permissions for accessing GCS.  
- **Docker Errors**: Ensure the Docker daemon is running, and `.env` variables are configured correctly.

---

## Contributing

1. **Fork the Repository**.  
2. **Create a Feature Branch**.  
3. **Submit a Pull Request** with a detailed description of your changes.

---

## Contact Information

For questions or collaborations, contact:  

- **Aliya**: [26aly000@gmail.com](mailto:26aly000@gmail.com)  
- **Changping Chen**: [champing1409@gmail.com](mailto:champing1409@gmail.com)  
- **Krishna Priya Gitalaxmi**: [gitakrishnapriya@gmail.com](mailto:gitakrishnapriya@gmail.com)  
- **Qi An**: [blessanq@gmail.com](mailto:blessanq@gmail.com)  
- **Ziqi Li**: [zql04150415@gmail.com](mailto:zql04150415@gmail.com)

---
