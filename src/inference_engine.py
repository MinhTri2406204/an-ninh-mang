import pandas as pd
import numpy as np
import joblib

model=joblib.load(
"/home/ids/IDS_Project/models/xgb_flow_model.pkl"
)

encoder=joblib.load(
"/home/ids/IDS_Project/models/label_encoder.pkl"
)

FEATURES=(
model.get_booster()
.feature_names
)


def predict(flow):

    row={}

    for col in FEATURES:

        row[col]=0


    for key,value in flow.items():

        if key in row:

            row[key]=value


    df=pd.DataFrame(
         [row]
    )

#    pred=model.predict(
#        df
#    )

    prob=model.predict_proba(df)
    prob_benign = prob[0][0]
    prob_attack = prob[0][1]

#    label=encoder.inverse_transform(
#        pred
#    )[0]

#    output_class = pred[0]
    THRESHOLD = 0.85
#    if output_class == 1:
#        label = "PortScan"
#    else:
#        label = "BENIGN"
#
#    confidence=max(
#        prob[0]
#    )
    if prob_attack >= THRESHOLD:
        label = "PortScan"
        confidence = prob_attack
    else:
        label = "BENIGN"
        confidence = prob_benign
    return (
       label,
        confidence
    )

