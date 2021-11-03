#!/usr/bin/env python
# coding: utf-8

import requests


url = "http://localhost:9696/predict"

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

response = requests.post(url, json=patient).json()
print(response)


patient = {
    "mean radius": 20.57,
    "mean texture": 17.77,
    "mean perimeter": 132.90,
    "mean area": 1326.0,
    "mean smoothness": 0.08474,
    "mean compactness": 0.07864,
    "mean concavity": 0.08690,
    "mean concave points": 0.07017,
    "mean symmetry": 0.1812,
    "mean fractal dimension": 0.05667,
    "radius error": 0.5435,
    "texture error": 0.7339,
    "perimeter error": 3.398,
    "area error": 74.08,
    "smoothness error": 0.005225,
    "compactness error": 0.01308,
    "concavity error": 0.01860,
    "concave points error": 0.01340,
    "symmetry error": 0.01389,
    "fractal dimension error": 0.003532,
    "worst radius": 24.990,
    "worst texture": 23.41,
    "worst perimeter": 158.80,
    "worst area": 1956.0,
    "worst smoothness": 0.12380,
    "worst compactness": 0.18660,
    "worst concavity": 0.2416,
    "worst concave points": 0.1860,
    "worst symmetry": 0.2750,
    "worst fractal dimension": 0.08902,
}

response = requests.post(url, json=patient).json()
print(response)
