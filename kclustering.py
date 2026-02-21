from sklearn.cluster import KMeans
import numpy as np

X = np.array([[1,2],
              [1,4],
              [1,0],
              [10,2],
              [10,4],
              [10,0]])

kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

print("Centroids:", kmeans.cluster_centers_)
print("Labels:", kmeans.labels_)

import numpy as np

p = np.array([2,3])
q = np.array([6,7])

distance = np.linalg.norm(p - q)
print(distance)

