from tensorflow.keras.models import load_model

model=load_model(
"/home/ids/IDS_Project/models/lstm_model.keras"
)

prob=model.predict(
packet_sequence
)
