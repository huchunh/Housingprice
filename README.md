# House_Price_Prediction_MLOPs
This project implements an advanced Machine Learning Operations (MLOps) pipeline for predicting house prices. It incorporates traditional factors such as location, size, and number of rooms, along with a novel feature: house condition.

## Features

- Data scraping from Zillow for up-to-date market information
- Comprehensive data preprocessing and feature engineering
- Advanced modeling techniques including regression, tree-based models, and neural networks
- Continuous integration and deployment (CI/CD) practices
- Monitoring and maintenance systems for model performance and fairness

## Installation

1. Clone the repository:


## Data
https://www.kaggle.com/datasets/shashanknecrothapa/ames-housing-dataset 

## Key features
![image](https://github.com/user-attachments/assets/82150931-caac-4779-8d48-8e7c4ee0f828)


For all features please check the reference : [Features Explanation](https://docs.google.com/spreadsheets/d/1XL6LJVgLLU27yV7a_oh2zuqhGOI3Syg-jWpmr0Ekk14/edit?gid=0#gid=0).





## Load dataset from Google Cloud Storage
Our data version control is managed and hosted on Google Cloud Platform (GCP). GCP offers seamless support for hosting large datasets and tracking their versions, facilitating the development of robust ETL pipelines. It enables multiple users to access and update data simultaneously, with built-in versioning that makes retrieving previous versions straightforward. GCP has been instrumental in efficiently implementing our ETL processes while maintaining intermediate files for all modular tasks.

- To get started with GCP services, simply initialize a service account.
- As with other remote services, downloading an SSH key is necessary for remote access.

![image](https://github.com/user-attachments/assets/9b1e2f1e-82fc-4628-be23-db7f63b685f4)

Picture: Our data files at GCP

Current MLPipline

（insert pipline pic here maybe ）

Airflow Dags
We utilize Apache Airflow for our pipeline. We create a DAG with our modules.

![image](https://github.com/user-attachments/assets/a8ecfda0-bf73-4ce4-9c8c-46b162cf10a2)

![image](https://github.com/user-attachments/assets/1282bf7d-c42b-4383-a2b3-73847527460f)

Picture: our current dag


## Unittest

We use GitHub Actions and unit tests to validate functions of our Airflow DAGs. Once functions are merged into the main branch, unit tests are triggered automatically, providing us with feedback on the test results.

![image](https://github.com/user-attachments/assets/dd5985b6-f473-4a29-b036-991de9a1e4b4)
![image](https://github.com/user-attachments/assets/28978057-f8c0-4e58-bbec-e66ecf3a1ae6)
![image](https://github.com/user-attachments/assets/74c31c68-e3ad-4c8e-ac46-17482e6718f7)

Picture: Our unit tests




