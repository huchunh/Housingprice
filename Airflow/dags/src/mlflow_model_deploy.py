import mlflow
from google.cloud import storage
import os
import numpy as np
from airflow.models import Variable
from google.oauth2 import service_account

def fetch_best_model_across_experiments(**kwargs):
        """
        Fetch the best model across all MLflow experiments.
        """
        # Initialize MLflow client
        client = mlflow.tracking.MlflowClient()

        # Get all experiments
        experiments = client.list_experiments()
        if not experiments:
            raise ValueError("No experiments found in MLflow.")

        best_model_uri = None
        best_metric_value = np.inf  # Assuming we're minimizing a metric (e.g., RMSE)
        best_experiment = None
        best_run = None

        # Iterate through experiments to find the best model
        for experiment in experiments:
            runs = client.search_runs(
                experiment_ids=[experiment.experiment_id],
                order_by=["metrics.rmse ASC"],  # Adjust metric key as needed
                max_results=1,
            )
            if runs:
                run = runs[0]
                rmse = run.data.metrics.get("rmse")
                if rmse is not None and rmse < best_metric_value:
                    best_metric_value = rmse
                    best_model_uri = f"runs:/{run.info.run_id}/model"
                    best_experiment = experiment
                    best_run = run

        if not best_model_uri:
            raise ValueError("No valid models found across all experiments.")

        print(f"Best model URI: {best_model_uri}")
        print(f"Best Experiment: {best_experiment.name}, Run ID: {best_run.info.run_id}, RMSE: {best_metric_value}")

        # Push the best model URI to XCom
        kwargs['ti'].xcom_push(key='best_model_uri', value=best_model_uri)

def download_best_model(local_path, **kwargs):
        """
        Download the best model artifacts locally from MLflow.
        """
        # Retrieve the best model URI from XCom
        ti = kwargs['ti']
        best_model_uri = ti.xcom_pull(task_ids='fetch_best_model', key='best_model_uri')

        if not best_model_uri:
            raise ValueError("Best model URI not found in XCom.")

        # Download the model artifacts
        mlflow.artifacts.download_artifacts(best_model_uri, dst_path=local_path)
        print(f"Best model downloaded to: {local_path}")

def upload_model_to_gcs(local_model_path, destination_path, **kwargs):
        """
        Upload the model to Google Cloud Storage (GCS).
        """
        # Fetch the credentials from Airflow Variables
        gcp_credentials = Variable.get("GOOGLE_APPLICATION_CREDENTIALS", deserialize_json=True)

        # Authenticate using the fetched credentials
        credentials = service_account.Credentials.from_service_account_info(gcp_credentials)

        # Create a storage client with specified credentials
        client = storage.Client(credentials=credentials)
        bucket_name = 'bucket_data_mlopsteam2'
        # Get the bucket
        bucket = client.get_bucket(bucket_name)

        # Define the local path to the model.pkl file
        model_pkl_path = os.path.join(local_model_path, "model.pkl")

        # Check if model.pkl exists
        if not os.path.exists(model_pkl_path):
            raise FileNotFoundError(f"model.pkl not found in {local_model_path}.")

        # Define the GCS destination path
        gcs_file_path = os.path.join(destination_path, "model.pkl")

        # Upload model.pkl to GCS
        blob = bucket.blob(gcs_file_path)
        blob.upload_from_filename(model_pkl_path)
        print(f"Uploaded {model_pkl_path} to gs://{bucket_name}/{gcs_file_path}")
        