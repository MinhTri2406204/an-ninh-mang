import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM,Dense

X=np.load("/home/ids/IDS_Project/data/X_seq.npy")
y=np.load("/home/ids/IDS_Project/data/y_seq.npy")

X=X[:100000]
y=y[:100000]

print(X.shape)
print(y.shape)

num_classes=len(set(y))
model=Sequential([
    LSTM(
        64,
        input_shape=(
            X.shape[1],
            X.shape[2]
        )
    ),
    Dense(
        32,
        activation="relu"
    ),
    Dense(
        num_classes,
        activation="softmax"
    )

])
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)
model.fit(
    X,
    y,
    epochs=5,
    batch_size=64
)

model.save("/home/ids/IDS_Project/models/lstm_model.keras")
print("Training completed")
