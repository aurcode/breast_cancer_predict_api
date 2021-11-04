#!/usr/bin/env python
# coding: utf-8

import pickle

import pandas as pd
import numpy as np

from sklearn import datasets
from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score


# parameters

V = 1.0  # Version
depth = 2
min_samples_leaf = 10
output_file = f"model.{V}.bin"

# data preparation

dataset: dict = datasets.load_breast_cancer()
X: pd.DataFrame = pd.DataFrame(dataset["data"], columns=dataset["feature_names"])
y: np.ndarray = dataset["target"]

X_full_train, X_test, Y_full_train, Y_test = train_test_split(X, y, test_size=.20, random_state=0)
X_full_train, X_validation, Y_full_train, Y_validation = train_test_split(X_full_train, Y_full_train, test_size=.25, random_state=0)

# training


def train(X_train, y_train, depth, min_samples_leaf):
    model = DecisionTreeClassifier(
        random_state=0, max_depth=depth, min_samples_leaf=min_samples_leaf
    )
    model.fit(X_train, y_train)

    return model


def predict(df_X, model):
    y_pred = model.predict_proba(df_X)[:, 1]

    return y_pred

# validation

#print(f'doing validation with C={C}')

# training the final model
print("training the final model")

model = train(X_full_train, Y_full_train, depth, min_samples_leaf)

auc = roc_auc_score(Y_validation, predict(X_validation, model))
print("Validation", auc)

y_pred = predict(X_test, model)
auc = roc_auc_score(Y_test, y_pred)

print(f"auc={auc}")

with open(output_file, "wb") as f_out:
    pickle.dump(model, f_out)

print(f"the model is saved to {output_file}")
