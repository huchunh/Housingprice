# House_Price_Prediction_MLOps

This project implements an advanced Machine Learning Operations (MLOps) pipeline for predicting house prices. It integrates traditional property features (location, size, and number of rooms) with a novel feature: **house condition**. The pipeline uses Google Cloud Platform (GCP) for data management, Apache Airflow for orchestration, and Data Version Control (DVC) for tracking data versions and model iterations.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Folder Structure](#folder-structure)
3. [Installation and Setup](#installation-and-setup)
4. [Quickstart Guide](#quickstart-guide)
5. [Data Source](#data-source)
6. [Pipeline Workflow](#pipeline-workflow)
7. [Unit Testing and Continuous Integration](#unit-testing-and-continuous-integration)
8. [Contributing](#contributing)
9. [License](#license)
10. [Contact Information](#contact-information)

---

## Project Overview

This project aims to develop an accurate, condition-aware model for predicting house prices. The model considers a variety of features and employs advanced data processing, feature engineering, and modeling techniques. Key features of this project include:

- **Data Acquisition**: Data scraping from Zillow and integration with the Ames Housing Dataset.
- **Data Preprocessing**: Cleaning, transforming, and feature engineering to enhance prediction accuracy.
- **Modeling Techniques**: Utilizes regression, tree-based models, and neural networks to compare and optimize performance.
- **CI/CD Practices**: Automated deployment and testing using GitHub Actions.
- **Model Monitoring and Maintenance**: Tracks model performance and ensures fairness in predictions over time.

### Dependencies

Key tools and services used in this project include:
- **Apache Airflow**: For orchestrating the ETL pipeline.
- **Google Cloud Platform (GCP)**: For data storage and version control.
- **DVC (Data Version Control)**: For tracking data and model versions.

## Folder Structure

```
House_Price_Prediction_MLOps/
├── Airflow/               # Contains DAGs and scripts for data pipeline orchestration.
├── Methodology/           # Provides details on model choices, data processing, and feature engineering.
├── project_dvc/           # Stores DVC configuration files for data versioning and management.
├── tests/                 # Contains unit tests and validation scripts.
├── .gitignore             # Specifies files to ignore in Git.
└── README.md              # Main project documentation.
```

## Installation and Setup

To set up the project environment:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your_username/House_Price_Prediction_MLOps.git
    cd House_Price_Prediction_MLOps
    ```

2. **Install dependencies**:
   - Use the `requirements.txt` file to install Python dependencies.
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   - Add GCP credentials and other environment variables in a `.env` file (refer to the `config/` folder).
   - Initialize a GCP service account and download an SSH key if accessing data remotely.

4. **Set Up Airflow**:
   - Initialize the Airflow database and start the Airflow scheduler and web server:
   ```bash
   airflow db init
   airflow scheduler
   airflow webserver
   ```

## Quickstart Guide

1. **Load Data from Google Cloud Storage (GCS)**:
   - Our datasets are managed in GCS, with version control provided by DVC.

2. **Trigger the Airflow Pipeline**:
   - Access the Airflow web UI at `http://localhost:8080`.
   - Enable and trigger the DAGs (data acquisition, preprocessing, and model training pipelines) as needed.

3. **Monitor Data and Model Versions**:
   - Use DVC commands to track changes in data and models:
   ```bash
   dvc add data/raw/ames_housing.csv
   dvc push
   ```

## Data Source

The main dataset used is the [Ames Housing Dataset](https://www.kaggle.com/datasets/shashanknecrothapa/ames-housing-dataset), which includes details on property features. For additional feature details, refer to our [Features Explanation](https://docs.google.com/spreadsheets/d/1XL6LJVgLLU27yV7a_oh2zuqhGOI3Syg-jWpmr0Ekk14/edit?gid=0#gid=0).

## Pipeline Workflow

We use **Apache Airflow** to manage our pipeline, which includes tasks for data scraping, preprocessing, model training, and evaluation. The pipeline structure is modular, with tasks organized into distinct DAGs for each stage.

**Pipeline Overview**:

- **Data Loading and Preprocessing**: Loads raw data from GCS, validates and cleans the data.
- **Feature Engineering**: Transforms and augments data for better model performance.
- **Model Training**: Trains models using various algorithms and stores results for evaluation. [Next Stage]
- **Model Evaluation**: Assesses model performance and pushes metrics to monitoring systems. [Next Stage]

![Pipeline Diagram](https://github.com/user-attachments/assets/55121bb8-6b69-4101-ba7b-37ae5d89cab9)


## Unit Testing and Continuous Integration

We use **GitHub Actions** to perform automated unit tests on each pipeline component. When changes are pushed to the main branch, GitHub Actions runs the unit tests and provides feedback on their status.

![Unit Test](https://github.com/user-attachments/assets/74c31c68-e3ad-4c8e-ac46-17482e6718f7)

## Contributing

We welcome contributions to improve this project. Please fork the repository, make changes, and submit a pull request. Ensure that your code follows the existing style guidelines and includes tests for any new features.

## License

This project is licensed under the [].

## Contact Information

For questions or collaboration inquiries, please contact one of the team members:
- Aliya at [26aly000@gmail.com]
- Changping Chen at [champing1409@gmail.com]
- Krishna Priya Gitalaxmi at [gitakrishnapriya@gmail.com]
- Qi An at [blessanq@gmail.com]
- Ziqi Li at [zql04150415@gmail.com]
