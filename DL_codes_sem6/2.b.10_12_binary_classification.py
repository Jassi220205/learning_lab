from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Dataset
X, y = make_moons(n_samples=1000, noise=0.2, random_state=42)
scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = Sequential([
    Dense(16, activation='relu', input_shape=(2,)),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=30, verbose=0)

# Predictions
pred = (model.predict(X_test) > 0.5).astype(int)
# Evaluate the model
loss, acc = model.evaluate(X_test, y_test, verbose=0)
print("Test Accuracy:", acc)

# Predict a few points
preds = model.predict(X_test[:10])
print("\nSample Predictions (first 10):")
print((preds > 0.5).astype(int).reshape(-1))

# Plot decision boundary
import matplotlib.pyplot as plt

plt.figure(figsize=(6,5))
plt.scatter(X[:,0], X[:,1], c=y, cmap='coolwarm', s=20)
plt.title("Decision Boundary Plot")
plt.xlabel("X1")
plt.ylabel("X2")
plt.show()
