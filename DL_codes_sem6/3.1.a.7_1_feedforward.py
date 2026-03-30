# Build a Feed Forward Neural Network and compare optimizers

import numpy as np
import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import accuracy_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD, Adam, RMSprop

# Reproducibility
tf.keras.utils.set_random_seed(42)

# 1. Load Dataset
iris = load_iris()
X, y = iris.data, iris.target

# One-hot encode target labels
encoder = OneHotEncoder(sparse=False)
y = encoder.fit_transform(y.reshape(-1, 1))

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Standardize features (NO data leakage)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 2. Function to build and train the model
def build_and_train_model(optimizer_name, optimizer):
    print(f"\n--- Training with {optimizer_name} ---")

    model = Sequential([
        Dense(10, activation='relu', input_shape=(X_train.shape[1],)),
        Dense(10, activation='relu'),
        Dense(3, activation='softmax')
    ])

    model.compile(
        optimizer=optimizer,
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    model.fit(
        X_train,
        y_train,
        epochs=50,
        batch_size=16,
        validation_split=0.2,
        verbose=0
    )

    y_pred = model.predict(X_test, verbose=0)
    y_pred_classes = np.argmax(y_pred, axis=1)
    y_test_classes = np.argmax(y_test, axis=1)

    accuracy = accuracy_score(y_test_classes, y_pred_classes)
    print(f"Test Accuracy with {optimizer_name}: {accuracy:.4f}")

    return accuracy

# 3. Optimizers to compare
optimizers = {
    "SGD": SGD(learning_rate=0.01),
    "Adam": Adam(learning_rate=0.001),
    "RMSprop": RMSprop(learning_rate=0.001)
}

# 4. Train and evaluate
performance_results = {}

for name, optimizer in optimizers.items():
    performance_results[name] = build_and_train_model(name, optimizer)

# 5. Summary
print("\n--- Summary of Performance ---")
for name, acc in performance_results.items():
    print(f"{name}: {acc:.4f}")
