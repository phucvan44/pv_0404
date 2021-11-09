import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

np.random.seed(42)


class KMeans:

	colors = ["red", "blue", "green", "yellow"] # Colors for marker 


	def __init__(self, K):
		self.K = K
		self.clusters = [[] for _ in range(self.K)]
		self.centroids = np.array([[30, -60], [40, -10], [20, 10], [-20, 40]])


	def euclidean_distance(self, point1, point2):
		return np.sqrt(np.sum((point1 - point2)**2))


	def closest_centroids(self, point, centroids):
		distances = [
			self.euclidean_distance(point, centroid) for centroid in centroids
		]
		return np.argmin(distances)


	def create_clusters(self, centroids):
		clusters = [[] for _ in range(self.K)]
		for idx, point in enumerate(self.X):
			centroid_idx = self.closest_centroids(point, centroids)
			clusters[centroid_idx].append(idx)
		return clusters


	def get_centroids(self, clusters):
		centroids = np.zeros((self.K, self.n_features))
		for cluster_idx, cluster in enumerate(clusters):
			cluster_mean = np.mean(self.X[cluster], axis = 0)
			centroids[cluster_idx] = cluster_mean
		return centroids


	def is_converged(self, centroids_old, centroids):
		distances = [
			self.euclidean_distance(centroids_old[idx], centroids[idx]) for idx in range(self.K)
		]
		return sum(distances) == 0


	def get_clusters_labels(self, clusters):
		labels = np.zeros((self.n_points))
		for cluster_idx, cluster in enumerate(self.clusters):
			for point_idx in cluster:
				labels[point_idx] = cluster_idx
		return labels


	def predict(self, X):
		self.X = X 
		self.n_points, self.n_features = X.shape

		while True:
			self.clusters = self.create_clusters(self.centroids)
			centroids_old = self.centroids 
			self.centroids = self.get_centroids(self.clusters)

			if self.is_converged(centroids_old, self.centroids):
				break

		return self.get_clusters_labels(self.clusters)


	def plot(self):
		for idx, cluster in enumerate(self.clusters):
			point = self.X[cluster].T
			plt.scatter(*point, marker = 'o', color = self.colors[idx])
			
		for idx, centroid in enumerate(self.centroids):
			plt.scatter(*centroid, marker = 's', color = self.colors[idx])
		
		plt.title("K-Means Clustering")
		plt.xlabel("X")
		plt.ylabel("y")
		plt.show()


if __name__ == "__main__":
	# Read data
	data = pd.read_csv("position.csv")
	X = data.values

	k = KMeans(K = 4)

	labels_clusters = k.predict(X)

	print(k.centroids)

	k.plot()	