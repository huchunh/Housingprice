from airflow import DAG

from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta

import pandas as pd
 
# read data

def read_data():

    global df

    df = pd.read_csv('/Users/liziqi/NEU/IE7374/AmesHousing 2.csv')

    print("Data loaded successfully")
 
# data overview

def data_overview():

    global df

    print("Data shape:", df.shape)

    print("Data info:")

    df.info()  # print out data info

    print("Data description:")

    print(df.describe(include="all"))
 
# check for missing value

def check_missing_values():

    global df

    missing_values = df.isna().sum()

    print("Missing values in each column:")

    print(missing_values)
 
# data categorical overview

def categorical_overview():

    global df

    for column in df.columns:

        if df[column].dtype == 'object' or df[column].nunique() < 20:

            print(f"Column: {column}")

            print("Number of classes:", df[column].nunique())

            print("Number of data samples per class:")

            print(df[column].value_counts())
 
# data preprocess

def preprocess_data():

    global df

    df = df.dropna()
 
    # print the head of dataframe

    print("Data after preprocessing:")

    print(df.head())
 
# define default parameter of DAG 

default_args = {

    'owner': 'Kiki',

    'depends_on_past': False,

    'email_on_failure': False,

    'email_on_retry': False,

    'retries': 1,

    'retry_delay': timedelta(minutes=5),

}
 
# define DAG

with DAG(

    'weekly_data_cleaning_dag',

    default_args=default_args,

    description='Weekly data cleaning DAG',

    schedule_interval='@weekly',  # run weekly

    start_date=datetime(2024, 10, 29),  # set begining date

    catchup=False,

) as dag:
 
    # task 1: read data

    read_data_task = PythonOperator(

        task_id='read_data',

        python_callable=read_data

    )
 
    # task 2: data overview

    data_overview_task = PythonOperator(

        task_id='data_overview',

        python_callable=data_overview

    )
 
    # task 3: check missing value

    check_missing_values_task = PythonOperator(

        task_id='check_missing_values',

        python_callable=check_missing_values

    )
 
    # task 4: data categorical overview

    categorical_overview_task = PythonOperator(

        task_id='categorical_overview',

        python_callable=categorical_overview

    )
 
    # task 5: data preprecessing

    preprocess_data_task = PythonOperator(

        task_id='preprocess_data',

        python_callable=preprocess_data

    )
 
    # define relationship

    read_data_task >> data_overview_task >> check_missing_values_task >> categorical_overview_task >> preprocess_data_task