import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("/home/ids/IDS_Project/data/clean.csv")

corr=df.iloc[:,0:15].corr()

plt.figure(figsize=(12,8))

plt.imshow(corr)

plt.colorbar()

plt.title(
"Feature Correlation"
)

plt.tight_layout()

plt.savefig(
"/home/ids/IDS_Project/pictures/heatmap.png"
)


