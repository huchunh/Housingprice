import pandas as pd
import numpy as np
from sklearn.linear_model import LassoCV
from sklearn.preprocessing import StandardScaler

def select_correlated_features(encoded_data):
    """
    Selects numerical features with a correlation of at least `threshold` with the target variable.
    
    Parameters:
    - df (pd.DataFrame): DataFrame containing all encoded data.
    - numerical_features (list): List of numerical feature names to consider for correlation.
    - target (str): Name of the target variable.
    - threshold (float): Minimum absolute correlation threshold for feature selection.
    
    Returns:
    - list: Selected features with correlation >= threshold with the target variable.
    """
    ### path
    df = pd.read_json(encoded_data)

    # List of all numerical features except the target to consider for correlation
    numerical_features = [
       "Order", "PID", "MS SubClass", "Lot Frontage", "Lot Area", "Overall Qual", 
       "Overall Cond", "Year Built", "Year Remod/Add", "Mas Vnr Area", "BsmtFin SF 1", 
       "BsmtFin SF 2", "Bsmt Unf SF", "Total Bsmt SF", "1st Flr SF", "2nd Flr SF", 
       "Low Qual Fin SF", "Gr Liv Area", "Bsmt Full Bath", "Bsmt Half Bath", "Full Bath", 
       "Half Bath", "Bedroom AbvGr", "Kitchen AbvGr", "TotRms AbvGrd", "Fireplaces", 
       "Garage Cars", "Garage Area", "Wood Deck SF", "Open Porch SF", "Enclosed Porch", 
       "3Ssn Porch", "Screen Porch", "Pool Area", "Misc Val", "Mo Sold", "Yr Sold"
    ]
    target='SalePrice'

    threshold=0.3

    # Use only numerical features without the target variable
    X_num = df[numerical_features]
    y = df[target]

    # Add the target back temporarily to calculate correlations
    X_num_with_target = X_num.copy()
    X_num_with_target[target] = y

    # Calculate the correlation matrix
    correlation_matrix = X_num_with_target.corr()

    # Select features with a correlation of at least `threshold` with the target
    saleprice_correlation = correlation_matrix[target].abs().sort_values(ascending=False)
    selected_features = saleprice_correlation[saleprice_correlation >= threshold].index.tolist()

    # Remove the target variable from the list of selected features
    if target in selected_features:
        selected_features.remove(target)

    return selected_features


def rank_features_by_lasso(encoded_data):
    """
    Ranks numerical features by importance using Lasso coefficients and selects
    features with coefficients above a specified threshold.
    
    Parameters:
    - df (pd.DataFrame): The entire DataFrame containing the data.
    - selected_features (list): List of feature names selected from correlation matrix.
    - target_column (str): The name of the target variable.
    - threshold (float): Minimum absolute coefficient threshold to select features.
    
    Returns:
    - list: Selected feature names (features based on Lasso importance).
    """

    target='SalePrice'
    selected_features = select_correlated_features()
    threshold=0.1
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
    selected_features = feature_importance[feature_importance >= threshold].sort_values(ascending=False)
    selected_features = selected_features.index.tolist()

    return selected_features

