import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model

X=np.load("/home/ids/IDS_Project/data/X_seq.npy")
y=np.load("/home/ids/IDS_Project/data/y_seq.npy")

X=X[:100000]
y=y[:100000]

_,X_test,_,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model=load_model("/home/ids/IDS_Project/models/lstm_model.keras")

pred=model.predict(X_test)
pred=pred.argmax(axis=1)
cm=confusion_matrix(y_test, pred)
plt.figure(figsize=(10,8))
plt.imshow(cm)
plt.colorbar()
plt.title("Confusion Matrix LSTM")
plt.savefig("/home/ids/IDS_Project/pictures/confusion_matrix_lstm.png")

