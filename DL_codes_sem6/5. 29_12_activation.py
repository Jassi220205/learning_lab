import numpy as np

x = np.array([1.0, 2.0, 3.0])
w = np.array([0.2, 0.4, 0.6])
b = 0.5

z = 0
for i in range(len(x)):
    z += w[i] * x[i]
z = z + b

def binary_step(z):
    return 1 if z >= 0 else 0

def linear(z):
    return z

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def tanh(z):
    return np.tanh(z)

def relu(z):
    return max(0, z)

def leaky_relu(z, alpha=0.01):
    return z if z > 0 else alpha * z

def softmax(z_vector):
    exp_z = np.exp(z_vector - np.max(z_vector))
    return exp_z / np.sum(exp_z)

z_vector = np.array([z, z, z])

print("Input x:", x)
print("Weights w:", w)
print("Bias b:", b)
print("z = Σ(wi*xi) + b:", z)
print()

print("Binary Step:", binary_step(z))
print("Linear:", linear(z))
print("Sigmoid:", sigmoid(z))
print("Tanh:", tanh(z))
print("ReLU:", relu(z))
print("Leaky ReLU:", leaky_relu(z))
print("Softmax:", softmax(z_vector))
