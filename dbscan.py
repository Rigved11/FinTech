from sklearn.cluster import DBSCAN
import numpy as np
import matplotlib.pyplot as plt

# Sample Data
X = np.array([[1,2],
              [2,2],
              [2,3],
              [8,7],
              [8,8],
              [25,80]])  # outlier

# Apply DBSCAN
db = DBSCAN(eps=2, min_samples=2)
labels = db.fit_predict(X)

print("Cluster Labels:", labels)

# Plot
plt.scatter(X[:,0], X[:,1], c=labels)
plt.show()