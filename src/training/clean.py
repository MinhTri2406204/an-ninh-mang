import pandas as pd
import numpy as np

df=pd.read_csv("/home/ids/IDS_Project/data/all.csv")
df.columns=df.columns.str.strip()
df=df.replace([np.inf,-np.inf],np.nan)
df=df.dropna()
print(df.shape)

df.to_csv("/home/ids/IDS_Project/data/clean.csv",index=False)
