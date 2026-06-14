import joblib
import pandas as pd
from sklearn.metrics import *
model=joblib.load("/home/ids/IDS_Project/models/xgb_flow_model.pkl")
X_test=pd.read_csv("/home/ids/IDS_Project/data/X_test.csv")
y_test=pd.read_csv("/home/ids/IDS_Project/data/y_test.csv")
y_test=y_test.squeeze()
pred=model.predict(X_test)
prob=model.predict_proba(X_test)
print()
print(classification_report(y_test, pred))
print()
print("F1:")
print(f1_score(y_test, pred, average='weighted'))
print()
print("AUC:")
print(roc_auc_score(y_test, prob[:, -1]))
