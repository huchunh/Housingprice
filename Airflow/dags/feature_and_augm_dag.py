from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from src.feature_select import rank_features_by_lasso, select_correlated_features
from src.data_augment import augment_data_with_perturbations
from datetime import datetime, timedelta
import json

# Define the DAG
default_args = {
    'owner': 'House_Price_Prediction Team',
    'start_date': datetime(2024, 10, 29),
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'DAG_feature_selcet_data_augmentation',
    default_args=default_args,
    description='DAG for tasks in House Price Prediction Project',
    schedule_interval=None,
    catchup=False,
)
# Define the Python function for the feature selection task
def feature_selection_callable(**kwargs):
    # Pull the encoded data from XCom
    ti = kwargs['ti']
    encoded_data_json = ti.xcom_pull(task_ids='encode_data_task', key='encoded_data')
    
    if encoded_data_json is None:
        raise ValueError("No encoded data found in XCom for 'encoded_data'")
    
    # Load the JSON data into a DataFrame
    df_encoded = pd.read_json(encoded_data_json)

    # Define parameters
    numerical_features = [
       "Order", "PID", "MS SubClass", "Lot Frontage", "Lot Area", "Overall Qual", 
       "Overall Cond", "Year Built", "Year Remod/Add", "Mas Vnr Area", "BsmtFin SF 1", 
       "BsmtFin SF 2", "Bsmt Unf SF", "Total Bsmt SF", "1st Flr SF", "2nd Flr SF", 
       "Low Qual Fin SF", "Gr Liv Area", "Bsmt Full Bath", "Bsmt Half Bath", "Full Bath", 
       "Half Bath", "Bedroom AbvGr", "Kitchen AbvGr", "TotRms AbvGrd", "Fireplaces", 
       "Garage Cars", "Garage Area", "Wood Deck SF", "Open Porch SF", "Enclosed Porch", 
       "3Ssn Porch", "Screen Porch", "Pool Area", "Misc Val", "Mo Sold", "Yr Sold"
    ]
    target = 'SalePrice'
    
    # Step 1: Select features based on correlation
    selected_features = select_correlated_features(df_encoded, numerical_features, target, threshold=0.3)

    # Step 2: Rank features using Lasso and further refine the selection
    final_features = rank_features_by_lasso(df_encoded, selected_features, target, threshold=0.1)

    # Push final selected features to XCom for use in subsequent tasks
    ti.xcom_push(key='final_features', value=final_features)

feature_selection_task = PythonOperator(
    task_id='feature_selection_task',
    python_callable=feature_selection_callable,
    provide_context=True,
    dag=dag,
)

# Data augmentation task
def data_augmentation_callable(**kwargs):
    ti = kwargs['ti']
    # Pull the training data and selected features from XCom
    train_data_json = ti.xcom_pull(task_ids='data_split_task', key='train_data')
    final_features = ti.xcom_pull(task_ids='feature_selection_task', key='final_features')
    
    if train_data_json is None or final_features is None:
        raise ValueError("Required data not found in XCom")

    # Load the JSON-encoded training data into a DataFrame
    train_data = pd.read_json(train_data_json, orient='split')

    # Run the augmentation function
    augmented_data = augment_data_with_perturbations(train_data, final_features, perturbation_percentage=0.02)

    # Convert augmented data to JSON format and push to XCom for later use
    ti.xcom_push(key='augmented_data', value=augmented_data.to_json(orient='split'))

data_augmentation_task = PythonOperator(
    task_id='data_augmentation_task',
    python_callable=data_augmentation_callable,
    provide_context=True,
    dag=dag,
)

# Set dependencies
feature_selection_task >> data_augmentation_task
