import os
import joblib
import pandas as pd
from scripts.file_system_paths import *

# define basic database struct
base_struct = {
    'runtime': [],
    'tag2': [],
    'tag3': [],
    'tag4': [],
    'tag7': [],
    'tag9': [],
    'tag11': [],
    'tag12': [],
    'tag14': [],
    'tag15': [],
    'tag17': [],
    'tag20': [],
    'tag21': [],
    'rul_pred': [],
    'prob_pred': []
}

# check if the folder exists and if not, create it
if not os.path.isdir(DASHBOARD_PATH):
    os.makedirs(DASHBOARD_PATH)

# check if the dataset exists and if not, create it
if 'predictions.csv' in os.listdir(DASHBOARD_PATH):
    data = pd.read_csv(os.path.join(DASHBOARD_PATH, 'predictions.csv'))
else:
    data = pd.DataFrame(base_struct)
    data.to_csv(os.path.join(DASHBOARD_PATH, 'predictions.csv'), index=False)

# load the trained models
regression_model = joblib.load(os.path.join(MODELS, 'regression_model.m'))
classification_model = joblib.load(os.path.join(MODELS, 'classification_model.m'))