import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

# Load dataset
data = pd.read_csv("spam.csv", encoding="latin-1")[["v1","v2"]]
data.columns = ["label","text"]

# Convert labels
data["label"] = data["label"].map({"ham":0,"spam":1})

# Tokenization
tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(data["text"])

seq = tokenizer.texts_to_sequences(data["text"])

# Padding
padded = pad_sequences(seq, maxlen=200)

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    padded,
    data["label"],
    test_size=0.2
)

# Build LSTM model
model_lstm = Sequential()

model_lstm.add(Embedding(input_dim=10000, output_dim=128))
model_lstm.add(LSTM(64))
model_lstm.add(Dense(1, activation="sigmoid"))

# Compile
model_lstm.compile(
    loss="binary_crossentropy",
    optimizer="adam",
    metrics=["accuracy"]
)

# Train
model_lstm.fit(
    X_train,
    y_train,
    epochs=3,
    batch_size=64,
    validation_split=0.2
)

# Evaluate
loss, acc = model_lstm.evaluate(X_test, y_test)

print("LSTM Test Accuracy:", acc)