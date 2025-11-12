from pyswarms.single.global_best import GlobalBestPSO
from sklearn.datasets import make_blobs
import numpy as np

# Data
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=0)
k = 4

# Define cost function for clustering
def cost_function(positions):
    n_particles = positions.shape[0]
    cost = np.zeros(n_particles)
    for i in range(n_particles):
        centroids = positions[i].reshape(k, X.shape[1])
        d = np.linalg.norm(X[:, None] - centroids[None, :], axis=2)
        cost[i] = np.sum(np.min(d, axis=1)**2)
    return cost

# Initialize PSO
options = {'c1': 1.5, 'c2': 1.5, 'w': 0.5}
optimizer = GlobalBestPSO(n_particles=20, dimensions=k*X.shape[1], options=options)

# Optimize
best_cost, best_pos = optimizer.optimize(cost_function, iters=50)
best_centroids = best_pos.reshape(k, X.shape[1])

# Visualize
labels = np.argmin(np.linalg.norm(X[:, None]-best_centroids[None,:], axis=2), axis=1)
plt.scatter(X[:,0], X[:,1], c=labels, cmap='viridis')
plt.scatter(best_centroids[:,0], best_centroids[:,1], c='red', marker='x')
plt.title("PSO Clustering (using pyswarms)")
plt.show()