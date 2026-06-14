import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

SEQ=10

df=pd.read_csv("/home/ids/IDS_Project/data/clean.csv")
le=LabelEncoder()
df["Label"]=le.fit_transform(df["Label"])
features=[
'Flow Duration',
'Packet Length Mean',
'Flow Bytes/s',
'SYN Flag Count'
]
X=[]
y=[]
for i in range(len(df)-SEQ):
    X.append(
        df[
        features
        ].iloc[
        i:i+SEQ
        ].values
    )
    y.append(
        df["Label"].iloc[
        i+SEQ
        ]
    )
X=np.array(X, dtype=np.float32)
y=np.array(y, dtype=np.int32)
np.save("/home/ids/IDS_Project/data/X_seq.npy", X)
np.save("/home/ids/IDS_Project/data/y_seq.npy", y)

print(
"X shape:",
X.shape
)

print(
"y shape:",
y.shape
)

print(
"y dtype:",
y.dtype
)

print(
"Unique labels:",
len(set(y))
)
