import pickle
import numpy as np
import pandas as pd
import config


with open(config.MODEL_FILE_PATH,"rb") as f:
    model = pickle.load(f)

def predict_species(data):
    sepalL = float(data["sepalL"])
    sepalW = float(data["sepalW"])
    petalL = float(data["petalL"])
    petalW = float(data["petalW"])

    y_pred = model.predict([[sepalL,sepalW,petalL,petalW]])

    species = y_pred[0]

    if species == 0:
        species = "Iris Setosa"
    elif species == 1:
        species = "Iris Versicolour"
    elif species == 2:
        species = "Iris Verginica"

    return species