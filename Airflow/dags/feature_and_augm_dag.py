from airflow import DAG
import logging
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
from src.data_splitting import split_data
from src.feature_select import rank_features_by_lasso, select_correlated_features
from src.data_augment import augment_data_with_perturbations

# Define default arguments for your DAG
default_args = {
    'owner': 'House_Price_Prediction Team',
    'start_date': datetime(2024, 11, 2),
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}

# Create a DAG instance
dag2 = DAG(
    'DAG_feature_select_and_data_augmentation',
    default_args=default_args,
    description=(
        'DAG for splitting data, feature selection, and '
        'data augmentation tasks'
    ),
    schedule_interval=None,
    catchup=False,
    max_active_runs=1,
)


def split_data_callable(**kwargs):
    """Task to split data."""
    ti = kwargs['ti']
    conf = kwargs.get("dag_run").conf

    # Retrieve encoded_result from the conf dictionary
    data = conf.get('encoded_result')

    if data is None:
        logging.error("No encoded data found in XCom for key 'encoded_result'")
    else:
        split_result = split_data(data, test_size=0.15)
        ti.xcom_push(key='train_data', value=split_result['train_data'])
        ti.xcom_push(key='test_data', value=split_result['test_data'])


data_split_task = PythonOperator(
    task_id='data_split_task',
    python_callable=split_data_callable,
    provide_context=True,
    dag=dag2,
)


def feature_selection_callable(**kwargs):
    """Task to select features."""
    ti = kwargs['ti']
    conf = kwargs.get("dag_run").conf

    encoded_data_json = conf.get('encoded_result')
    if encoded_data_json is None:
        raise ValueError("No encoded data found in XCom for 'encoded_data'")

    # Parameters
    numerical_features = [
        "Order", "PID", "MS SubClass", "Lot Frontage", "Lot Area",
        "Overall Qual", "Overall Cond", "Year Built", "Year Remod/Add",
        "Mas Vnr Area", "BsmtFin SF 1", "BsmtFin SF 2", "Bsmt Unf SF",
        "Total Bsmt SF", "1st Flr SF", "2nd Flr SF", "Low Qual Fin SF",
        "Gr Liv Area", "Bsmt Full Bath", "Bsmt Half Bath", "Full Bath",
        "Half Bath", "Bedroom AbvGr", "Kitchen AbvGr", "TotRms AbvGrd",
        "Fireplaces", "Garage Cars", "Garage Area", "Wood Deck SF",
        "Open Porch SF", "Enclosed Porch", "3Ssn Porch", "Screen Porch",
        "Pool Area", "Misc Val", "Mo Sold", "Yr Sold"
    ]
    target = 'SalePrice'

    selected_features = select_correlated_features(
        encoded_data_json, numerical_features, target, threshold=0.3
    )
    final_features = rank_features_by_lasso(
        encoded_data_json, selected_features, target, threshold=0.1
    )
    ti.xcom_push(key='final_features', value=final_features)


feature_selection_task = PythonOperator(
    task_id='feature_selection_task',
    python_callable=feature_selection_callable,
    provide_context=True,
    dag=dag2,
)


def data_augmentation_callable(**kwargs):
    """Task to augment data."""
    ti = kwargs['ti']
    train_data_json = ti.xcom_pull(task_ids='data_split_task', key='train_data')
    final_features = ti.xcom_pull(task_ids='feature_selection_task', key='final_features')

    if train_data_json is None or final_features is None:
        raise ValueError("Required data not found in XCom")

    train_data = pd.read_json(train_data_json, orient='split')
    augmented_data = augment_data_with_perturbations(
        train_data, final_features, perturbation_percentage=0.02
    )
    ti.xcom_push(key='augmented_data', value=augmented_data.to_json(orient='split'))


data_augmentation_task = PythonOperator(
    task_id='data_augmentation_task',
    python_callable=data_augmentation_callable,
    provide_context=True,
    dag=dag2,
)

# Set dependencies
data_split_task >> feature_selection_task
#data_split_task >> feature_selection_task >> data_augmentation_task
