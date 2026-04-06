import joblib
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
model = joblib.load('rfrmodel.pkl')

FEATURE_NAMES = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    df = pd.DataFrame([data])
    output = np.exp(model.predict(df)[0])
    return jsonify(output)

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    df = pd.DataFrame([data], columns=FEATURE_NAMES)
    output = np.exp(model.predict(df)[0])
    return render_template('home.html', prediction_text=f'Predicted House Price: ${output * 100000:,.2f}')

if __name__ == '__main__':
    app.run(debug=True)
