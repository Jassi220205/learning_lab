# Logistic Regression on Binary Classification (Iris 2-class). Classify iris flowers into setosa vs non-setosa using Logistic Regression.

#Logistic Regression predicts binary outcomes:
#𝑃(𝑦=1∣𝑥)=1/1+𝑒−𝑧​
#It outputs a probability between 0 and 1.
#We modify the Iris dataset to keep:
#1 = setosa
#0 = non-setosa

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data
iris = load_iris()
X = iris.data
y = (iris.target == 0).astype(int)   # setosa = 1, others = 0

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train logistic regression
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
