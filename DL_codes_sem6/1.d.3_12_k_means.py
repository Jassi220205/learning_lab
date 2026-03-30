# K-Means Clustering (Unsupervised Learning). Cluster unlabeled data (e.g., Iris features) using K-Means.

#K-Means groups similar items into K clusters without knowing labels:
#1. Choose K cluster centers
#2. Assign points to nearest center
#3. Recompute centers
#4. Repeat until stable
#For Iris, we commonly choose K = 3 (three species).

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load data
iris = load_iris()
X = iris.data

# Train K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X)

print("Cluster Labels:", clusters)

# Plot (first 2 features)
plt.scatter(X[:,0], X[:,1], c=clusters, cmap='viridis')
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("K-Means Clustering on Iris")
plt.show()
