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



## Data Splitting

We split the encoded dataset into training and test sets with an 85/15 ratio. This allocation provides a larger portion of data for training, which is essential for model learning, especially with our limited dataset size. The larger training set also supports the accuracy and balance required for our subsequent data augmentation. 

Importantly, we only augment the training data to ensure that the test data remains purely representative of real-world cases, helping to provide an unbiased evaluation of model performance.


## Feature Selection

After splitting, we apply feature selection to identify the most relevant features for predicting SalePrice. These selected features will be used for data augmentation.

### *1. Correlation Analysis*

First, we perform a correlation analysis, focusing on features with a correlation coefficient (Pearson’s r) of at least 0.3 with SalePrice. Pearson’s r, which ranges from -1 to +1, measures the strength and direction of a linear relationship between two variables. We set the threshold at 0.3 to capture features with a moderate level of association, aiming to retain features that hold predictive potential without being overly restrictive. This method also enhances interpretability in the context of a linear model, like linear regression, which we plan to use in modeling.


### *2. Lasso Coefficients*

Next, we apply Lasso regression to further refine our feature selection. Before performing Lasso, we standardize the features since Lasso is sensitive to feature scaling. We then use LassoCV to automatically determine the optimal level of regularization. This technique penalizes less important features, potentially reducing their coefficients to zero, thereby simplifying the model and focusing on the most predictive features. We set a high threshold of 0.1 for feature importance to retain only the most impactful features. Notably, only one feature was removed by Lasso, indicating that most of the features identified in the correlation step were indeed significant.


## Data Augmentation

Finally, we use the selected features as input to the augment_data_with_perturbations function for data augmentation. This approach generates synthetic records by perturbing only the most relevant features, thereby adding meaningful diversity to the training set. By introducing controlled variability in the important features, we enable the model to generalize better to slight variations in real-world data, enhancing robustness and stability.

We set the perturbation_percentage to 0.02, limiting perturbations to within 2% of each feature’s original value. This conservative level of variation ensures that the synthetic data remains realistic, avoiding outliers that could reduce model accuracy. Adding 2000 augmented records expands the dataset in a balanced way, enhancing model performance without introducing excessive noise, while keeping computational requirements manageable.



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




