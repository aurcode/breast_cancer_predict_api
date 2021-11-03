import pickle
import json
import pandas as pd
from flask import Flask
from flask import request
from flask import jsonify


model_file = "model.1.0.bin"

with open(model_file, "rb") as f_in:
    model = pickle.load(f_in)

app = Flask("breastcancer")


@app.route("/predict", methods=["POST"])
def predict():
    patient = request.get_json()
    y_pred = model.predict_proba([[i for i in patient.values()]])[0, 1]
    malignant = y_pred >= 0.5

    result = {"malignant_probability": float(y_pred), "malignant": bool(malignant)}
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)
