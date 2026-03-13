import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Dataset
data = {
    'Marks': [20, 25, 30, 45, 50, 60],
    'Result': [0, 0, 0, 1, 1, 1]   # 0 = Fail, 1 = Pass
}

df = pd.DataFrame(data)

# Features and target
X = df[['Marks']]
y = df['Result']

# Create Decision Tree
model = DecisionTreeClassifier()

# Train model
model.fit(X, y)

# Predict result for a student with 35 marks
prediction = model.predict([[35]])

print("Marks = 35")
print("Prediction:", prediction)