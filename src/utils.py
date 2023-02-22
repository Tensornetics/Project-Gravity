import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_data(data_path):
    """
    Loads data from a CSV file and performs basic preprocessing.

    Args:
        data_path (str): Path to the CSV file.

    Returns:
        Tuple of Numpy arrays: (features, labels)
    """
    df = pd.read_csv(data_path)
    X = df.drop('label', axis=1).values
    y = df['label'].values
    le = LabelEncoder()
    y = le.fit_transform(y)
    return X, y

def save_model(model, model_path):
    """
    Saves a machine learning model to disk.

    Args:
        model (sklearn estimator): The trained machine learning model.
        model_path (str): The path where the model should be saved.

    Returns:
        None
    """
    joblib.dump(model, model_path)

def load_model(model_path):
    """
    Loads a machine learning model from disk.

    Args:
        model_path (str): The path to the saved model.

    Returns:
        sklearn estimator: The loaded machine learning model.
    """
    return joblib.load(model_path)
