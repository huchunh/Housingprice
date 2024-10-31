import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from kneed import KneeLocator # type: ignore
from google.oauth2 import service_account
from airflow.models import Variable
import json
from google.cloud import storage
import pickle
import os
import logging



# def load_data():
#     """
#     Loads data from a CSV file, serializes it, and returns the serialized data.

#     Returns:
#         bytes: Serialized data.
#     """

#     df = pd.read_csv(os.path.join(os.path.dirname(__file__), "../data/file.csv"))
#     serialized_data = pickle.dumps(df)
    
#     return serialized_data
    
def load_data():
    # Fetch the credentials from Airflow Variables
    gcp_credentials = Variable.get("GOOGLE_APPLICATION_CREDENTIALS", deserialize_json=True)
    # Authenticate using the fetched credentials
    credentials = service_account.Credentials.from_service_account_info(gcp_credentials)
    
    # Create a storage client with specified credentials
    storage_client = storage.Client(credentials=credentials)
    bucket_name = 'bucket_data_mlopsteam2'
    blob_name = 'house-prices-advanced-regression-techniques/train.csv'
    
    # Get the bucket and blob
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    # Download the blob to a temporary file
    blob.download_to_filename('/tmp/train.csv')
    
    # Load the dataset into a DataFrame
    data = pd.read_csv('/tmp/train.csv')
    serialized_data = data.to_json()
    # pickle.dumps(data)
    logging.info(data.head())
    return serialized_data


def data_preprocessing(data):

    """
    Deserializes data, performs data preprocessing, and returns serialized clustered data.

    Args:
        data (bytes): Serialized data to be deserialized and processed.

    Returns:
        bytes: Serialized clustered data.
    """
    df = pd.read_json(data)
    # df = data
    df = df.dropna()
    # serialized_data = pickle.dumps(df)
    serialized_data = df.to_json()
    print(df.head())
    return serialized_data

def data_clean_test(data):
    # df_clean = pickle.loads(data)
    df_clean = pd.read_json(data)
    print(df_clean.isna())


# def build_save_model(data, filename):
#     """
#     Builds a KMeans clustering model, saves it to a file, and returns SSE values.

#     Args:
#         data (bytes): Serialized data for clustering.
#         filename (str): Name of the file to save the clustering model.

#     Returns:
#         list: List of SSE (Sum of Squared Errors) values for different numbers of clusters.
#     """
#     df = pd.read_json(data)
#     kmeans_kwargs = {"init": "random","n_init": 10,"max_iter": 300,"random_state": 42,}
#     sse = []
#     for k in range(1, 50):
#         kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
#         kmeans.fit(df)
#         sse.append(kmeans.inertia_)
    
#     output_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "model", filename)

#     # Save the trained model to a file
#     pickle.dump(kmeans, open(output_path, 'wb'))

#     return sse


# def load_model_elbow(filename,sse):
#     """
#     Loads a saved KMeans clustering model and determines the number of clusters using the elbow method.

#     Args:
#         filename (str): Name of the file containing the saved clustering model.
#         sse (list): List of SSE values for different numbers of clusters.

#     Returns:
#         str: A string indicating the predicted cluster and the number of clusters based on the elbow method.
#     """
    
#     output_path = os.path.join(os.path.dirname(__file__), "../model", filename)
#     # Load the saved model from a file
#     loaded_model = pickle.load(open(output_path, 'rb'))

#     df = pd.read_csv(os.path.join(os.path.dirname(__file__), "../data/test.csv"))
    
#     kl = KneeLocator(
#         range(1, 50), sse, curve="convex", direction="decreasing"
#     )

#     # Optimal clusters
#     print(f"Optimal no. of clusters: {kl.elbow}")

#     # Make predictions on the test data
#     predictions = loaded_model.predict(df)
    
#     return predictions[0]