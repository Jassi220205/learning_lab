import numpy as np

# Given data
x = np.array([0.6, 0.8, 0.0])
t = 0.9
alpha = 0.3

V = np.array([[2.0, 1.0, 0.0],
              [1.0, 2.0, 2.0],
              [0.0, 3.0, 1.0]])

V0 = np.array([0.0, 0.0, -1.0])

W = np.array([-1.0, 1.0, 2.0])
W0 = -1.0

def sigmoid(a):
    return 1 / (1 + np.exp(-a))

def sigmoid_derivative(f):
    return f * (1 - f)

epochs = 1000
previous_output = 0  # Initialize for the first check

for epoch in range(epochs):
    # -------------------
    # FORWARD PASS
    # -------------------
    zj = np.dot(x, V) + V0
    Z = sigmoid(zj)

    yk = np.dot(Z, W) + W0
    Y = sigmoid(yk)

    # CHECK FOR CONVERGENCE
    # This stops the loop if the change in Y is negligible
    if abs(Y - previous_output) < 0.0001:
        print(f"\n Converged at Epoch {epoch+1}")
        break
    
    previous_output = Y # Update for next epoch check

    # -------------------
    # BACKPROPAGATION
    # -------------------
    delta_k = (Y - t) * sigmoid_derivative(Y)
    delta_j = delta_k * W
    delta_j_final = delta_j * sigmoid_derivative(Z)

    # -------------------
    # WEIGHT UPDATES (Gradient DESCENT)
    # -------------------
    delta_V = alpha * np.outer(x, delta_j_final)
    delta_V0 = alpha * delta_j_final

    # We use MINUS here to move toward the target 0.9
    V = V - delta_V
    V0 = V0 - delta_V0

    delta_W = alpha * delta_k * Z
    delta_W0 = alpha * delta_k

    W = W - delta_W
    W0 = W0 - delta_W0

# Final Results
print(f"Target: {t}")
print(f"Final Output Y: {Y:.6f}")
print(f"Final Error: {Y - t:.6f}")