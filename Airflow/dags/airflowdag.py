import pandas as pd
import logging
import json
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from src.data_prep import load_data, data_overview, data_validation, data_cleaning
from src.label_encode import encode_data

# Define default arguments for your DAG
default_args = {
    'owner': 'House_Price_Prediction Team',
    'start_date': datetime(2024, 10, 29),
    'retries': 1,  # Added one retry for robustness
    'retry_delay': timedelta(minutes=5),
}

# Create a DAG instance
dag = DAG(
    'DAG_Data_Preprocessing',
    default_args=default_args,
    description='DAG for data preprocessing tasks in House Price Prediction Project',
    schedule_interval=None,
    catchup=False,
)

# Task to load data
def load_data_callable(**kwargs):
    try:
        data = load_data()
        kwargs['ti'].xcom_push(key='data', value=data)
        logging.info("Data loaded successfully")
    except Exception as e:
        logging.error(f"Error in load_data_task: {str(e)}")
        raise

load_data_task = PythonOperator(
    task_id='load_data_task',
    python_callable=load_data_callable,
    dag=dag,
)

# Task to perform data overview
def data_overview_callable(**kwargs):
    try:
        ti = kwargs['ti']
        data = ti.xcom_pull(task_ids='load_data_task', key='data')
        if data is None:
            raise ValueError("No data found in XCom for key 'data'")
        
        overview_data = data_overview(data)
        ti.xcom_push(key='overview_data', value=overview_data)
        logging.info("Data overview completed successfully")
    except Exception as e:
        logging.error(f"Error in data_overview_task: {str(e)}")
        raise

data_overview_task = PythonOperator(
    task_id='data_overview_task',
    python_callable=data_overview_callable,
    provide_context=True,
    dag=dag,
)

# Task to perform data validation
def data_validation_callable(**kwargs):
    try:
        ti = kwargs['ti']
        overview_data = ti.xcom_pull(task_ids='data_overview_task', key='overview_data')
        if overview_data is None:
            raise ValueError("No data found in XCom for key 'overview_data'")
        
        validated_data = data_validation(overview_data)
        ti.xcom_push(key='validated_data', value=validated_data)
        logging.info("Data validation completed successfully")
    except Exception as e:
        logging.error(f"Error in data_validation_task: {str(e)}")
        raise

data_validation_task = PythonOperator(
    task_id='data_validation_task',
    python_callable=data_validation_callable,
    provide_context=True,
    dag=dag,
)

# Task to perform data cleaning
def data_cleaning_callable(**kwargs):
    try:
        ti = kwargs['ti']
        validated_data = ti.xcom_pull(task_ids='data_validation_task', key='validated_data')
        if validated_data is None:
            raise ValueError("No data found in XCom for key 'validated_data'")
        
        cleaned_data = data_cleaning(validated_data)
        ti.xcom_push(key='cleaned_data', value=cleaned_data)
        logging.info("Data cleaning completed successfully")
    except Exception as e:
        logging.error(f"Error in data_cleaning_task: {str(e)}")
        raise

data_cleaning_task = PythonOperator(
    task_id='data_cleaning_task',
    python_callable=data_cleaning_callable,
    provide_context=True,
    dag=dag,
)

# Task to perform encoding
def encode_data_callable(**kwargs):
    try:
        ti = kwargs['ti']
        cleaned_data = ti.xcom_pull(task_ids='data_cleaning_task', key='cleaned_data')
        if cleaned_data is None:
            raise ValueError("No data found in XCom for key 'cleaned_data'")
        
        # Encode data using updated encode_data function
        encoded_result = encode_data(cleaned_data)
        
        # Push the entire encoded result as a single JSON string
        ti.xcom_push(key='encoded_result', value=encoded_result)
        logging.info("Data encoding completed successfully")
    except Exception as e:
        logging.error(f"Error in encode_data_task: {str(e)}")
        raise

encode_data_task = PythonOperator(
    task_id='encode_data_task',
    python_callable=encode_data_callable,
    provide_context=True,
    dag=dag,
)

# Set task dependencies
load_data_task >> data_overview_task >> data_validation_task >> data_cleaning_task >> encode_data_task