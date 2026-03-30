import numpy as np 
# Define Perceptron Class (No Backpropagation) 
class Perceptron: 
    def __init__(self, input_size, learning_rate=0.1): 
        self.learning_rate = learning_rate 
        self.weights = np.zeros(input_size) 
        self.bias = 0 
 
    def activation(self, x): 
        return 1 if x >= 0 else 0 
 
    def predict(self, inputs): 
        weighted_sum = np.dot(inputs, self.weights) + self.bias 
        return self.activation(weighted_sum) 
 
    def train(self, X, y, epochs): 
        for epoch in range(epochs): 
            print(f"Epoch {epoch + 1}") 
            for i in range(len(X)): 
                prediction = self.predict(X[i]) 
                error = y[i] - prediction 
 
                # Weight update (Perceptron learning rule) 
                self.weights += self.learning_rate * error * X[i] 
                self.bias += self.learning_rate * error 
 
                print(f"Input:{X[i]}, Target:{y[i]}, Prediction:{prediction}") 
            print("-" * 40) 
 
#Define Training Data (AND Gate) 
# Define Training Data (OR Gate)
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([0, 1, 1, 1])

 
#Create and Train the ANN 
perceptron = Perceptron(input_size=2, learning_rate=0.1) 
perceptron.train(X, y, epochs=10) 
 
#Test the Trained Model 
print("\nTesting Perceptron") 
for i in range(len(X)): 
    output = perceptron.predict(X[i]) 
print(f"Input: {X[i]} → Output: {output}")