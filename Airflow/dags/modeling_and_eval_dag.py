from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import logging
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Define default arguments for your DAG
default_args = {
    'owner': 'House_Price_Prediction Team',
    'start_date': datetime(2024, 11, 6),
    'retries': 0,  # Number of retries in case of task failure
    'retry_delay': timedelta(minutes=5),
}

# Create a new DAG instance named 'DAG_Model_Training_and_Evaluation'
dag3 = DAG(
    'DAG_Model_Training_and_Evaluation',
    default_args=default_args,
    description='DAG for training, evaluating, and comparing model performance',
    schedule_interval=None,
    catchup=False,
    max_active_runs=1,
)

# Task to train the model and make predictions
def train_and_predict_callable(**kwargs):
    ti = kwargs['ti']

    # Access the configuration passed from dag1
    conf = kwargs.get("dag_run").conf
    # Retrieve encoded_result from the conf dictionary
    augmented_data = conf.get('augmented_data')
    test_data = conf.get('test_data')

    augmented_data = pd.read_json(augmented_data, orient='split')
    test_data = pd.read_json(test_data, orient='split')

    # Train and predict
    X_train = augmented_data.drop('SalePrice', axis=1)
    y_train = augmented_data['SalePrice']
    X_test = test_data.drop('SalePrice', axis=1)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Push predictions to XCom
    ti.xcom_push(key='y_pred', value=y_pred.tolist())

train_and_predict_task = PythonOperator(
    task_id='train_and_predict_task',
    python_callable=train_and_predict_callable,
    provide_context=True,
    dag=dag3,
)

# Task to evaluate the model's performance
def evaluate_and_compare_models_callable(**kwargs):
    ti = kwargs['ti']
    y_pred = np.array(ti.xcom_pull(task_ids='train_and_predict_task', key='y_pred'))

    # Access the configuration
    conf = kwargs.get("dag_run").conf
    # Retrieve encoded_result from the conf dictionary
    test_data = conf.get('test_data')

    if y_pred is None or test_data is None:
        raise ValueError("Required data for model evaluation not found in XCom")

    test_data = pd.read_json(test_data, orient='split')

    # Evaluate model
    y_test = test_data['SalePrice']
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    # Create comparison DataFrame
    comparison_df = pd.DataFrame({
        "Metric": ["MAE", "MSE", "RMSE", "R2"],
        "Value": [mae, mse, rmse, r2]
    })

    # Log and push results
    logging.info(f"Evaluation metrics:\n{comparison_df}")
    ti.xcom_push(key='comparison_metrics', value=comparison_df.to_json(orient='split'))

evaluate_and_compare_task = PythonOperator(
    task_id='evaluate_and_compare_task',
    python_callable=evaluate_and_compare_models_callable,
    provide_context=True,
    dag=dag3,
)

# Set dependencies for tasks within dag3
train_and_predict_task >> evaluate_and_compare_task

