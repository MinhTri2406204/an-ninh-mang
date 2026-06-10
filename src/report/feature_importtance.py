import joblib
from xgboost import plot_importance
import matplotlib.pyplot as plt

model=joblib.load(
"/home/ids/IDS_Project/models/xgb_flow_model.pkl"
)

plt.figure(figsize=(10,8))

plot_importance(
model,
max_num_features=10
)

plt.tight_layout()

plt.savefig(
"/home/ids/IDS_Project/pictures/importance.png"
)


