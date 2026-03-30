from google.colab import files
files.upload()

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("menstrual_cycle_dataset_with_factors.csv")
print(df.head())



# Create binary target based on cycle length
df['Irregular_Cycle'] = np.where((df['Cycle Length'] < 25) | (df['Cycle Length'] > 31), 1, 0)

# Drop irrelevant columns
X = df.drop(['User ID', 'Cycle Start Date', 'Next Cycle Start Date', 'Irregular_Cycle'], axis=1)
y = df['Irregular_Cycle'].values

# Handle categorical variables
X = pd.get_dummies(X, drop_first=True)

# Handle missing values
X.fillna(X.mean(), inplace=True)

# Convert to NumPy
X = X.values

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Logistic Regression from scratch
class LogisticRegressionScratch:
    def __init__(self, lr=0.1, n_iters=3000):
        self.lr = lr
        self.n_iters = n_iters

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def fit(self, X, y):
        self.w = np.zeros(X.shape[1])
        self.b = 0

        for _ in range(self.n_iters):
            linear_output = np.dot(X, self.w) + self.b
            y_pred = self.sigmoid(linear_output)

            dw = np.dot(X.T, (y_pred - y)) / len(y)
            db = np.sum(y_pred - y) / len(y)

            self.w -= self.lr * dw
            self.b -= self.lr * db

    def predict(self, X):
        linear_output = np.dot(X, self.w) + self.b
        y_pred = self.sigmoid(linear_output)
        return np.where(y_pred >= 0.5, 1, 0)

# Train model
model = LogisticRegressionScratch()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = np.mean(predictions == y_test)
print("Logistic Regression Accuracy:", accuracy)
