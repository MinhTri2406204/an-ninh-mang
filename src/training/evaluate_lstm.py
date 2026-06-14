import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score)
from tensorflow.keras.models import load_model

X=np.load("/home/ids/IDS_Project/data/X_seq.npy")
y=np.load("/home/ids/IDS_Project/data/y_seq.npy")

X=X[:100000]
y=y[:100000]

X_train,X_test,y_train,y_test=train_test_split(X, y, test_size=0.2, random_state=42)
model=load_model("/home/ids/IDS_Project/models/lstm_model.keras")
pred_prob=model.predict(X_test)
#pred=pred.argmax(axis=1)
pred=(pred_prob > 0.5).astype(np.int32).flatten()
print("Accuracy:")
print(accuracy_score(y_test, pred))
print("\nPrecision:")
print(precision_score(y_test, pred, average="weighted"))
print("\nRecall:")
print(recall_score(y_test, pred, average="weighted"))
print("\nF1:")
print(f1_score(y_test, pred, average="weighted"))
