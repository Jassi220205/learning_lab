import numpy as np

def sigmoid(x):
    """The activation function."""
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    """Derivative of sigmoid (not used here)."""
    return x * (1 - x)

class SimpleNNRandomSearch:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Weights will be initialized during random search
        self.weights_ih = None
        self.weights_ho = None
        self.best_accuracy = 0

    def forward(self, X):
        """Performs a forward pass."""
        hidden_input = np.dot(X, self.weights_ih)
        hidden_output = sigmoid(hidden_input)
        output_input = np.dot(hidden_output, self.weights_ho)
        output = sigmoid(output_input)
        return output

    def calculate_accuracy(self, X, y):
        """Calculates classification accuracy."""
        predictions = (self.forward(X) > 0.5).astype(int)
        return np.mean(predictions == y)

    def train_random_search(self, X, y, iterations=1000):
        print(f"Starting random search training for {iterations} iterations...")

        best_weights_ih = np.random.randn(self.input_size, self.hidden_size) * 0.1
        best_weights_ho = np.random.randn(self.hidden_size, self.output_size) * 0.1

        for i in range(iterations):
            current_weights_ih = np.random.randn(self.input_size, self.hidden_size)
            current_weights_ho = np.random.randn(self.hidden_size, self.output_size)

            self.weights_ih = current_weights_ih
            self.weights_ho = current_weights_ho

            current_accuracy = self.calculate_accuracy(X, y)

            if current_accuracy > self.best_accuracy:
                self.best_accuracy = current_accuracy
                best_weights_ih = current_weights_ih
                best_weights_ho = current_weights_ho

                print(f"Iteration {i}: New best accuracy = {self.best_accuracy:.4f}")

                if self.best_accuracy == 1.0:
                    print("Perfect accuracy achieved. Stopping early.")
                    break

        self.weights_ih = best_weights_ih
        self.weights_ho = best_weights_ho

        print(f"Training finished. Best accuracy = {self.best_accuracy:.4f}")

# ---------------- Example Usage ---------------- #

# XOR dataset
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([
    [0],
    [0],
    [0],
    [1]
])


INPUT_SIZE = 2
HIDDEN_SIZE = 3
OUTPUT_SIZE = 1

nn = SimpleNNRandomSearch(INPUT_SIZE, HIDDEN_SIZE, OUTPUT_SIZE)
nn.train_random_search(X, y, iterations=5000)

print("\nTesting the trained model:")
predictions = (nn.forward(X) > 0.5).astype(int)

print("Inputs:")
print(X)
print("Predicted outputs:")
print(predictions.flatten())
print("Actual outputs:")
print(y.flatten())
