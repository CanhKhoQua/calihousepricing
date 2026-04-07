import joblib
import numpy as np
import pandas as pd
import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app import app

FEATURE_NAMES = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']
SAMPLE_INPUT = [3.5, 25.0, 5.2, 1.1, 1200.0, 3.0, 34.05, -118.25]


def test_model_loads():
    model = joblib.load('rfrmodel.pkl')
    assert model is not None

def test_model_predicts():
    model = joblib.load('rfrmodel.pkl')
    df = pd.DataFrame([SAMPLE_INPUT], columns=FEATURE_NAMES)
    prediction = model.predict(df)
    assert len(prediction) == 1
    assert isinstance(prediction[0], (float, np.floating))


def test_home_route():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200


def test_predict_route():
    client = app.test_client()
    data = {name: value for name, value in zip(FEATURE_NAMES, SAMPLE_INPUT)}
    response = client.post('/predict', data=data)
    assert response.status_code == 200
    assert b'Predicted House Price' in response.data
