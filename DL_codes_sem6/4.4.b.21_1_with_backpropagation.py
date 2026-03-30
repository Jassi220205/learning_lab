import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# ------------------ Input and Output ------------------ #

# XOR input
# OR input
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# OR output
y = np.array([
    [0],
    [1],
    [1],
    [1]
])


# ------------------ Network Parameters ------------------ #

np.random.seed(1)

input_layer_neurons = 2
hidden_layer_neurons = 2
output_neurons = 1
learning_rate = 0.1
epochs = 10000

# Initialize weights and biases
weights_input_hidden = np.random.uniform(
    size=(input_layer_neurons, hidden_layer_neurons)
)
weights_hidden_output = np.random.uniform(
    size=(hidden_layer_neurons, output_neurons)
)

bias_hidden = np.random.uniform(size=(1, hidden_layer_neurons))
bias_output = np.random.uniform(size=(1, output_neurons))

# ------------------ Training (Backpropagation) ------------------ #

for epoch in range(epochs):

    # Forward pass
    hidden_layer_input = np.dot(X, weights_input_hidden) + bias_hidden
    hidden_layer_output = sigmoid(hidden_layer_input)

    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    predicted_output = sigmoid(output_layer_input)

    # Error
    error = y - predicted_output

    # Backpropagation
    d_predicted_output = error * sigmoid_derivative(predicted_output)

    error_hidden_layer = d_predicted_output.dot(weights_hidden_output.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

    # Update weights and biases
    weights_hidden_output += hidden_layer_output.T.dot(d_predicted_output) * learning_rate
    weights_input_hidden += X.T.dot(d_hidden_layer) * learning_rate

    bias_output += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate
    bias_hidden += np.sum(d_hidden_layer, axis=0, keepdims=True) * learning_rate

# ------------------ Testing ------------------ #

print("Final Predictions After Training:\n")

for i in range(len(X)):
    hidden = sigmoid(np.dot(X[i], weights_input_hidden) + bias_hidden)
    output = sigmoid(np.dot(hidden, weights_hidden_output) + bias_output)
    print(f"Input: {X[i]} → Predicted Output: {output.round(3)}")
