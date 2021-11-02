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
    # return "PONG"
    patient = request.get_json()

    # print(type(patient))
    X = pd.DataFrame(patient, index=patient.keys())
    print(X)
    print(type(X))
    print(X)
    print(model.predict([patient]))  # [0, 1])
    # y_pred = model.predict_proba(patient)[0, 1]
    # malignant = y_pred >= 0.5

    # result = {"malignant_probability": float(y_pred), "malignant": bool(malignant)}
    return "pong"
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)
