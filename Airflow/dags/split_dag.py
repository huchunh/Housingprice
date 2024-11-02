from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from src.data_splitting import split_data

# Define the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
}

dag = DAG(
    'data_split_dag',
    default_args=default_args,
    description='A simple DAG to split CSV data',
    schedule_interval=None,
)

# Define the task using PythonOperator
data_split_task = PythonOperator(
    task_id='split_data_task',
    python_callable=split_data,
    dag=dag,
)

# Set task dependencies
data_split_task
