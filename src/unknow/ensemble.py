import joblib
import numpy as np
from tensorflow.keras.models import load_model
xgb=joblib.load("/home/ids/IDS_Project/models/xgb_flow_model.pkl")
lstm=load_model("/home/ids/IDS_Project/models/lstm_model.keras")

def ensemble_predict(flow_feature, sequence_feature):
    p1=xgb.predict_proba([flow_feature])[0]
    p2=lstm.predict(sequence_feature, verbose=0)[0]
    final=(p1+p2)/2
    label=np.argmax(final)
    conf=np.max(final)
    return label,conf
