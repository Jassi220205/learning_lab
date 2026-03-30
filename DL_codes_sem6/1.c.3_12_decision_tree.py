# Decision Tree Classifier on Iris Dataset. Train a Decision Tree to classify iris species and visualize the tree.

#A Decision Tree splits data based on feature thresholds
#(e.g., petal length < 2.5 cm → setosa).
#Trees are easy to visualize and interpret.

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Load data
iris = load_iris()
X, y = iris.data, iris.target

# Train model
tree = DecisionTreeClassifier(max_depth=3)
tree.fit(X, y)

# Visualize tree
plt.figure(figsize=(12, 8))
plot_tree(tree, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.show()
