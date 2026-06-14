import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("/home/ids/IDS_Project/data/clean.csv")

counts=df["Label"].value_counts()

plt.figure(figsize=(12,6))

counts.plot(kind="bar")

plt.xticks(rotation=45)

plt.ylabel("Samples")

plt.title(
"Label Distribution CICIDS2017"
)

plt.tight_layout()

plt.savefig(
"/home/ids/IDS_Project/pictures/label_distribution.png"
)


