import pandas as pd
import numpy as np
import joblib

model=joblib.load("/home/ids/IDS_Project/models/xgb_flow_model.pkl")
encoder=joblib.load("/home/ids/IDS_Project/models/label_encoder.pkl")

FEATURES=(model.get_booster().feature_names)

def predict(flow):
    row={}
    for col in FEATURES:
        row[col]=0
    for key,value in flow.items():
        if key in row:
            row[key]=value
    df=pd.DataFrame([row])
    prob=model.predict_proba(df)
    prob_benign = prob[0][0]
    prob_attack = prob[0][1]
    THRESHOLD = 0.85
    if prob_attack >= THRESHOLD:
        label = "PortScan"
        confidence = prob_attack
    else:
        label = "BENIGN"
        confidence = prob_benign
    return (label, confidence)
