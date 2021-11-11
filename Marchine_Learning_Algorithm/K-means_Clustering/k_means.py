import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

np.random.seed(42)


class KMeans:

	colors = ["red", "green", "blue", "black"]


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


	def get_clusters(self, centroids):
		clusters = [[] for _ in range(self.K)]
		for point_idx, point in enumerate(self.X):
			centroid_idx = self.closest_centroids(point, centroids)
			clusters[centroid_idx].append(point_idx)
		return clusters


	def get_centroids(self, clusters):
		centroids = np.zeros((self.K, self.n_features))
		for cluster_idx, cluster in enumerate(clusters):
			cluster_mean = np.mean(self.X[cluster], axis = 0)
			centroids[cluster_idx] = cluster_mean
		return centroids


	def is_converged(self, centroids, old_centroids):
		distances = [
			self.euclidean_distance(centroids[idx], old_centroids[idx]) for idx in range(self.K)
		]
		return sum(distances) == 0


	def get_clusters_labels(self, clusters):
		labels = np.zeros((self.n_points))
		for cluster_idx, cluster in enumerate(clusters):
			for point_idx in cluster:
				labels[point_idx] = cluster_idx
		return labels


	def predict(self, X):
		self.X = X 
		self.n_points, self.n_features = X.shape

		while True:
			self.clusters = self.get_clusters(self.centroids)
			old_centroids = self.centroids 
			self.centroids = self.get_centroids(self.clusters)

			if self.is_converged(self.centroids, old_centroids):
				break

		return self.get_clusters_labels(self.clusters)


	def plot(self):
		for cluster_idx, cluster in enumerate(self.clusters):
			points = self.X[cluster].T
			plt.scatter(*points, marker = 'o', color = self.colors[cluster_idx])

		for centroid_idx, centroid in enumerate(self.centroids):
			plt.scatter(*centroid, marker = 's', color = self.colors[centroid_idx])

		plt.title("K-Means Clustering")
		plt.xlabel("X")
		plt.ylabel("y")
		plt.show()


if __name__ == "__main__":
	data = pd.read_csv("position.csv")

	X = data.values

	k = KMeans(K = 4)
	labels_predict = k.predict(X)

	print(k.centroids)

	k.plot()