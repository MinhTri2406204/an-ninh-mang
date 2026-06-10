import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from xgboost import XGBClassifier
import joblib

df=pd.read_csv("/home/ids/IDS_Project/data/clean.csv")

X=df.drop("Label",axis=1)

y=df["Label"]

le=LabelEncoder()

y=le.fit_transform(y)

X_train,X_test,y_train,y_test=train_test_split(
X,
y,
test_size=.2,
random_state=42,
stratify=y
)

X_test.to_csv(

    "/home/ids/IDS_Project/data/X_test.csv",

    index=False

)

pd.DataFrame(y_test).to_csv(

    "/home/ids/IDS_Project/data/y_test.csv",

    index=False

)

model=XGBClassifier(

n_estimators=100,

max_depth=8,

random_state=42

)

model.fit(
X_train,
y_train
)

joblib.dump(
model,
"/home/ids/IDS_Project/models/xgb_flow_model.pkl"
)

joblib.dump(
le,
"/home/ids/IDS_Project/models/label_encoder.pkl"
)
