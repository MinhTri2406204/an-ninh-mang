import matplotlib.pyplot as plt

from sklearn.metrics import roc_curve
from sklearn.metrics import auc

fpr=[0,0.05,0.1,1]
tpr=[0,0.92,0.98,1]

roc_auc=auc(
    fpr,
    tpr
)

plt.figure()

plt.plot(
    fpr,
    tpr
)

plt.xlabel(
    "False Positive Rate"
)

plt.ylabel(
    "True Positive Rate"
)

plt.title(
    f"ROC Curve AUC={roc_auc:.2f}"
)

plt.savefig(
    "/home/ids/IDS_Project/pictures/roc_curve.png"
)
