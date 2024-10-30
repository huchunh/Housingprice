# Import necessary libraries and modules
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from src.data_prep import load_data, data_preprocessing

# Define default arguments for your DAG
default_args = {
    'owner': 'Project Team',
    'start_date': datetime(2024, 10, 20),
    'retries': 0,  # Number of retries in case of task failure
    'retry_delay': timedelta(minutes=5),  # Delay before retries
}

# Create a DAG instance named 'DAG 1' with the defined default arguments
dag = DAG(
    'DAG_Data_Preprocessing',
    default_args=default_args,
    description='Dag data prep example for Project',
    schedule_interval=None,  # Set the schedule interval or use None for manual triggering
    catchup=False,
)

# Define PythonOperators for each function

# Task to load data, calls the 'load_data' Python function
def load_data_callable(**kwargs):
    data = load_data()
    # Push data to XCom
    kwargs['ti'].xcom_push(key='data', value=data)

load_data_task = PythonOperator(
    task_id='load_data_task',
    python_callable=load_data_callable,
    provide_context=True,
    dag=dag,
)

# Task to perform data preprocessing
def data_preprocessing_callable(**kwargs):
    # Pull data from XCom
    ti = kwargs['ti']
    data = ti.xcom_pull(task_ids='load_data_task', key='data')
    processed_data = data_preprocessing(data)
    # Push processed data to XCom
    ti.xcom_push(key='processed_data', value=processed_data)

data_preprocessing_task = PythonOperator(
    task_id='data_preprocessing_task',
    python_callable=data_preprocessing_callable,
    provide_context=True,
    dag=dag,
)


# Set task dependencies
load_data_task >> data_preprocessing_task 
