
# House Price Prediction MLOps Project

This project focuses on building a robust **Machine Learning Operations (MLOps)** pipeline to predict house prices. The pipeline integrates **Apache Airflow** for orchestration, **Google Cloud Platform (GCP)** for data management, and **Data Version Control (DVC)** for data and model tracking. The main dataset used is the **Ames Housing Dataset**, enhanced with additional features for better prediction accuracy.

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Folder Structure](#folder-structure)  
3. [Installation and Setup](#installation-and-setup)  
4. [Pipeline Workflow](#pipeline-workflow)  
5. [Methodology](#methodology)  
6. [Unit Testing and Continuous Integration](#unit-testing-and-continuous-integration)  
7. [Contributing](#contributing)  
8. [Contact Information](#contact-information)  

---

## Project Overview

The project automates the end-to-end process of house price prediction with the following stages:

- **Data Acquisition**: Retrieval of property data from GCS.  
- **Data Preprocessing**: Cleaning, validation, and transformation of raw data.  
- **Feature Engineering and Augmentation**: Enhancing data quality for better modeling.  
- **Model Training and Evaluation**: Leveraging regression and tree-based models.  
- **Version Control**: Ensuring reproducibility with DVC for tracking changes.  

**Key Features**:  
- Modular pipeline designed with **Apache Airflow**.  
- Scalable data storage and management with **GCP**.  
- Continuous integration and deployment with **GitHub Actions**.

---

## Folder Structure

```plaintext
House_Price_Prediction_MLOps/
├── Airflow/               # Airflow DAGs and orchestration scripts
│   ├── dags/              # Airflow DAG definitions
│   ├── src/               # Task-specific processing scripts
├── project_dvc/           # DVC configuration and data versioning
├── Methodology/           # Documentation for modeling and data processing
├── tests/                 # Unit tests for pipeline components
└── README.md              # Main project documentation
```

---

## Installation and Setup

### Prerequisites

- **Python 3.8+**  
- **Apache Airflow 2.x**  
- **DVC**  
- **Google Cloud SDK**  
- **Docker (optional)**  

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

3. **Configure Environment Variables**:  
   - Add the following to a `.env` file:  
     ```
     GCP_PROJECT_ID=your_project_id
     GCS_BUCKET_NAME=your_bucket_name
     DVC_REMOTE_PATH=your_remote_path
     ```

4. **Set Up Airflow**:  
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

### Overview

The pipeline uses **Apache Airflow** to manage the workflow with modular DAGs:

1. **Data Loading and Preprocessing**:
   - Load raw data from GCS.  
   - Validate, clean, and split into training, validation, and test sets.  

2. **Feature Engineering and Augmentation**:
   - Enhance features and apply augmentation techniques.  

3. **Model Training and Evaluation**:
   - Train models and evaluate performance using RMSE and MAE metrics.  

4. **Version Control with DVC**:
   - Track changes in data and models, and synchronize with remote storage.  

### Pipeline Visualization

![Pipeline Diagram](https://github.com/user-attachments/assets/55121bb8-6b69-4101-ba7b-37ae5d89cab9)

---

## Methodology

### Data Processing

1. **Outlier Removal**:
   - Exclude houses with extreme feature values (e.g., over 4000 sq. ft.).  

2. **Missing Values**:
   - Fill numerical features with `0` or median values.  
   - Encode categorical features with "Missing" as a valid category.  

### Feature Engineering

- Encode quality-related features (e.g., 1-5 scales).  
- Augment training data with 2000 synthetic records (varying features by 2%).  

### Model Selection and Evaluation

- Use **Lasso Regression** and **tree-based models** for interpretability and accuracy.  
- Evaluate models with:
  - **Root Mean Squared Error (RMSE)**  
  - **Mean Absolute Error (MAE)**  

---

## Unit Testing and Continuous Integration

We use **GitHub Actions** for automated testing and deployment. Upon each commit, the pipeline triggers:  

- **Unit Tests**: Validates individual pipeline components.  
- **Integration Tests**: Ensures compatibility between stages.  

**Run Tests Locally**:  
```bash
pytest tests/
```

![Unit Test Results](https://github.com/user-attachments/assets/74c31c68-e3ad-4c8e-ac46-17482e6718f7)

---

## Contributing

1. **Fork the Repository**.  
2. **Create a Feature Branch**.  
3. **Submit a Pull Request** detailing the changes.  

---

## Contact Information

For questions or collaborations, contact:  

- **Aliya**: [26aly000@gmail.com](mailto:26aly000@gmail.com)  
- **Changping Chen**: [champing1409@gmail.com](mailto:champing1409@gmail.com)  
- **Krishna Priya Gitalaxmi**: [gitakrishnapriya@gmail.com](mailto:gitakrishnapriya@gmail.com)  
- **Qi An**: [blessanq@gmail.com](mailto:blessanq@gmail.com)  
- **Ziqi Li**: [zql04150415@gmail.com](mailto:zql04150415@gmail.com)  

--- 
