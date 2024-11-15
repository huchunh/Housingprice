import pandas as pd
#import numpy as np
from sklearn.linear_model import LassoCV
from sklearn.preprocessing import StandardScaler


def select_correlated_features(encoded_data, numerical_features, target, threshold):
    """
    Selects numerical features with a correlation of at least `threshold` with the target variable.

    Parameters:
    - encoded_data (str): JSON string containing all encoded data.
    - numerical_features (list): List of numerical feature names to consider for correlation.
    - target (str): Name of the target variable.
    - threshold (float): Minimum absolute correlation threshold for feature selection.

    Returns:
    - list: Selected features with correlation >= threshold with the target variable.
    """
    df = pd.read_json(encoded_data)

    # Use only numerical features without the target variable
    X_num = df[numerical_features]
    y = df[target]

    # Add the target back temporarily to calculate correlations
    X_num_with_target = X_num.copy()
    X_num_with_target[target] = y

    # Calculate the correlation matrix
    correlation_matrix = X_num_with_target.corr()

    # Select features with a correlation of at least `threshold` with the target
    saleprice_correlation = (
        correlation_matrix[target].abs().sort_values(ascending=False)
    )
    selected_features = saleprice_correlation[
        saleprice_correlation >= threshold
    ].index.tolist()

    # Remove the target variable from the list of selected features
    if target in selected_features:
        selected_features.remove(target)

    return selected_features


def rank_features_by_lasso(encoded_data, selected_features, target, threshold):
    """
    Ranks numerical features by importance using Lasso coefficients and selects
    features with coefficients above a specified threshold.

    Parameters:
    - encoded_data (str): JSON string containing the data.
    - selected_features (list): List of feature names selected from correlation matrix.
    - target (str): The name of the target variable.
    - threshold (float): Minimum absolute coefficient threshold to select features.

    Returns:
    - list: Selected feature names (features based on Lasso importance).
    """
    df = pd.read_json(encoded_data)

    # Extract the feature matrix (X) and target variable (y)
    X = df[selected_features]
    y = df[target]

    # Standardize the selected features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Fit Lasso model with cross-validation
    lasso = LassoCV(cv=5, random_state=27).fit(X_scaled, y)

    # Create a series with feature names and their corresponding absolute coefficients
    feature_importance = pd.Series(lasso.coef_, index=X.columns).abs()

    # Filter features based on the specified threshold and sort by importance
    selected_features = feature_importance[
        feature_importance >= threshold
    ].sort_values(ascending=False)
    selected_features = selected_features.index.tolist()

    return selected_features
