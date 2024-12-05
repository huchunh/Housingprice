from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from src.mlflow_model_deploy import fetch_best_model_across_experiments, download_best_model, upload_model_to_gcs

# Define default arguments for the DAG
default_args = {
    'owner': 'House_Price_Prediction Team',
    'start_date': datetime(2024, 11, 2),
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag4 = DAG(
    'DAG_Compare_and_Push_Best_Model',
    default_args=default_args,
    description='Compare MLflow experiments, pick the best model, and upload to GCS',
    schedule_interval=timedelta(hours=1, minutes=30),  # Runs every hour
    start_date=datetime(2024, 12, 5, 0, 0),  # Today's date, midnight,
    catchup=False,
)

# Tasks
fetch_model_task = PythonOperator(
    task_id='fetch_best_model',
    python_callable=fetch_best_model_across_experiments,
    provide_context=True,
    dag=dag4,  # Associate with dag4
)

download_model_task = PythonOperator(
    task_id='download_best_model',
    python_callable=download_best_model,
    provide_context=True,
    op_kwargs={
        'local_path': '/tmp/best_model',  # Temporary local path
    },
    dag=dag4,  # Associate with dag4
)

upload_to_gcs_task = PythonOperator(
    task_id='upload_best_model_to_gcs',
    python_callable=upload_model_to_gcs,
    provide_context=True,
    op_kwargs={
        'local_model_path': '/tmp/best_model/model',
        'destination_path': 'models/best_model',  # Replace with your GCS path
    },
    dag=dag4,  # Associate with dag4
)

# Define task dependencies
fetch_model_task >> download_model_task >> upload_to_gcs_task
