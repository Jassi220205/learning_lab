import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# ------------------ DATASET ------------------
x = np.linspace(-10, 10, 500)
y = np.sin(x) + 0.1 * (x**2)   # nonlinear function

X = x.reshape(-1, 1)
Y = y.reshape(-1, 1)

# ------------------ MODEL ------------------
model = Sequential()
model.add(Dense(64, activation='relu', input_dim=1))
model.add(Dense(64, activation='relu'))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mse')

print("Training the model…")
model.fit(X, Y, epochs=50, verbose=0)

# ------------------ USER INPUT ------------------
user_x = float(input("Enter a number to predict the nonlinear output for: "))
prediction = model.predict(np.array([[user_x]]))[0][0]

print(f"\nInput: {user_x}")
print(f"Predicted Output: {prediction:.4f}")

# ------------------ PLOTTING ------------------
predicted_curve = model.predict(X)

plt.figure(figsize=(10,6))

# Original function
plt.scatter(x, y, color='lightblue', s=10, label="Original Function")

# Model prediction
plt.plot(x, predicted_curve, color='red', linewidth=2, label="Model Prediction")

# User point
plt.scatter(user_x, prediction, color='black', s=60, label="Your Input Prediction")

plt.title("Deep Feedforward Regression Network Learning a Nonlinear Function")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
