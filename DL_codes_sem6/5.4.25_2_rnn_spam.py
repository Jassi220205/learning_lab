import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense

# Load dataset (Colab: upload spam.csv)
data = pd.read_csv("spam.csv", encoding='latin-1')[['v1','v2']]
data.columns = ['label','text']
data['label'] = data['label'].map({'ham':0,'spam':1})
# Tokenization
tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(data['text'])
seq = tokenizer.texts_to_sequences(data['text'])
padded = pad_sequences(seq, maxlen=100)
X_train, X_test, y_train, y_test = train_test_split(padded, data['label'], test_size=0.2)

# Model
model = Sequential([
    Embedding(5000, 128),
    SimpleRNN(64),
    Dense(1, activation='sigmoid')
])
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=5, batch_size=32)
model.evaluate(X_test, y_test)

