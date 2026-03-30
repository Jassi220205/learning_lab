import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.1):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate

        # Initialize weights and biases
        self.weights_ih = np.random.randn(self.input_size, self.hidden_size) * 0.01
        self.bias_h = np.random.randn(1, self.hidden_size) * 0.01
        self.weights_ho = np.random.randn(self.hidden_size, self.output_size) * 0.01
        self.bias_o = np.random.randn(1, self.output_size) * 0.01

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def forward_pass(self, X):
        # Input → Hidden
        self.hidden_input = np.dot(X, self.weights_ih) + self.bias_h
        self.hidden_output = self.sigmoid(self.hidden_input)

        # Hidden → Output
        self.output_input = np.dot(self.hidden_output, self.weights_ho) + self.bias_o
        self.predicted_output = self.sigmoid(self.output_input)

        return self.predicted_output

    def backward_pass(self, X, y, output):
        # Output layer error
        output_error = y - output
        output_delta = output_error * self.sigmoid_derivative(output)

        # Hidden layer error
        hidden_error = output_delta.dot(self.weights_ho.T)
        hidden_delta = hidden_error * self.sigmoid_derivative(self.hidden_output)

        # Update weights and biases
        self.weights_ho += self.hidden_output.T.dot(output_delta) * self.learning_rate
        self.bias_o += np.sum(output_delta, axis=0, keepdims=True) * self.learning_rate
        self.weights_ih += X.T.dot(hidden_delta) * self.learning_rate
        self.bias_h += np.sum(hidden_delta, axis=0, keepdims=True) * self.learning_rate

    def train(self, X, y, epochs):
        for epoch in range(epochs):
            output = self.forward_pass(X)
            self.backward_pass(X, y, output)

            if epoch % 1000 == 0:
                loss = np.mean((y - output) ** 2)
                print(f"Epoch {epoch}, Loss: {loss:.4f}")

        final_loss = np.mean((y - output) ** 2)
        print(f"Final Loss after {epochs} epochs: {final_loss:.4f}")

# -------- XOR Example -------- #

X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([
    [0],
    [1],
    [1],
    [1]
])


nn = NeuralNetwork(input_size=2, hidden_size=4, output_size=1, learning_rate=0.1)

print("Starting training...")
nn.train(X, y, epochs=10000)
print("Training finished.")

print("\nTesting results:")
predictions = nn.forward_pass(X)
print(predictions)

print("\nThresholded predictions:")
print((predictions > 0.5).astype(int))
