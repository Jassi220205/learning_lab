import numpy as np

def activation(x):
    return np.clip(x, -1, 1)

# Input
x = np.array(list(map(float, input("Enter initial state: ").split())))
W = np.array(eval(input("Enter weight matrix: ")))

steps = int(input("Iterations: "))

for _ in range(steps):
    x = activation(x + np.dot(W, x))

print("Final State:", x)