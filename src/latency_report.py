import pandas as pd
import numpy as np

df=pd.read_csv(
"/home/ids/IDS_Project/logs/stage_latency.csv"
)

ai=df[
df["stage"]=="inference"
]["latency"]

print()

print(
"MEAN:"
)

print(
np.mean(ai)
)

print()

print(
"P95:"
)

print(
np.percentile(
ai,
95
)
)

print()

print(
"P99:"
)

print(
np.percentile(
ai,
99
)
)
