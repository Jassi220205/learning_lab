import numpy as np

# Sample function: f(x) = x^2
def grad(x):
    return 2*x

x = float(input("Initial x: "))
lr = float(input("Learning rate: "))
epochs = int(input("Epochs: "))

print("Choose Strategy: 1-Batch 2-Stochastic")
choice = int(input())

for i in range(epochs):
    if choice == 1:
        g = grad(x)
    else:
        g = grad(x + np.random.randn()*0.1)

    x = x - lr * g

print("Optimized x:", x)