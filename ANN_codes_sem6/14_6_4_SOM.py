import numpy as np

# Input
data = np.array(eval(input("Enter data points: ")))
neurons = int(input("Number of neurons: "))
lr = float(input("Learning rate: "))
epochs = int(input("Epochs: "))

# Initialize weights
weights = np.random.rand(neurons, data.shape[1])

for _ in range(epochs):
    for x in data:
        distances = np.linalg.norm(weights - x, axis=1)
        winner = np.argmin(distances)

        weights[winner] += lr * (x - weights[winner])

print("Final Weights:\n", weights)