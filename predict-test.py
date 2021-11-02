#!/usr/bin/env python
# coding: utf-8

import requests


url = "http://localhost:9696/predict"

customer_name = "Lisi"

patient = {
    "mean radius": 17.99,
    "mean texture": 10.38,
    "mean perimeter": 122.80,
    "mean area": 1001.0,
    "mean smoothness": 0.11840,
    "mean compactness": 0.27760,
    "mean concavity": 0.30010,
    "mean concave points": 0.14710,
    "mean symmetry": 0.2419,
    "mean fractal dimension": 0.07871,
    "radius error": 1.0950,
    "texture error": 0.9053,
    "perimeter error": 8.589,
    "area error": 153.40,
    "smoothness error": 0.006399,
    "compactness error": 0.04904,
    "concavity error": 0.05373,
    "concave points error": 0.01587,
    "symmetry error": 0.03003,
    "fractal dimension error": 0.006193,
    "worst radius": 25.380,
    "worst texture": 17.33,
    "worst perimeter": 184.60,
    "worst area": 2019.0,
    "worst smoothness": 0.16220,
    "worst compactness": 0.66560,
    "worst concavity": 0.7119,
    "worst concave points": 0.2654,
    "worst symmetry": 0.4601,
    "worst fractal dimension": 0.11890,
}

# print(patient)

response = requests.post(url, json=patient)  # .json()
print(response)
