import tensorflow as tf
from tensorflow.keras.datasets import reuters
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense
# Load dataset
vocab_size = 10000
(X_train, y_train), (X_test, y_test) = reuters.load_data(num_words=vocab_size)
# Preprocess
max_len = 200
X_train = pad_sequences(X_train, maxlen=max_len)
X_test = pad_sequences(X_test, maxlen=max_len)
# Model
model = Sequential([
    Embedding(vocab_size, 128, input_length=max_len),
    SimpleRNN(64),
    Dense(46, activation='softmax')
])
model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
# Train
model.fit(X_train, y_train, epochs=5, batch_size=64, validation_split=0.2)
# Evaluate
model.evaluate(X_test, y_test)
