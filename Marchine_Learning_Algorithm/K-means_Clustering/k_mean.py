import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

np.random.seed(42)


class KMeans:
	colors = ['red', 'blue', 'green', 'yellow']


	def __init__(self, K):
		self.K = K 
		self.clusters = [[] for _ in range(K)]
		self.centroids = np.array([[30, -60], [40, -10], [20, 10], [-20, 40]])


	def euclidean_distance(self, point1, point2):
		return np.sqrt(np.sum((point1 - point2)**2))


	def closest_centroid(self, sample, centroids):
		distances = [
			self.euclidean_distance(sample, point) for point in centroids\
		]
		return np.argmin(distances)

	
	def create_clusters(self, centroids):
		clusters = [[] for _ in range(self.K)]
		for idx, sample in enumerate(self.X):
			centroid_idx = self.closest_centroid(sample, centroids)
			clusters[centroid_idx].append(idx)
		return clusters 
	

	def get_cluster_labels(self, clusters):
		labels = np.empty(self.n_samples)

		for cluster_idx, cluster in enumerate(clusters):
			for sample_index in cluster:
				labels[sample_index] = cluster_idx
		return labels
	

	def get_centroids(self, clusters):
		centroids = np.zeros((self.K, self.n_features))
		for cluster_idx, cluster in enumerate(clusters):
			cluster_mean = np.mean(self.X[cluster], axis = 0)
			centroids[cluster_idx] = cluster_mean 
		return centroids 
	

	def is_converged(self, centroids_old, centroids):
		distances = [
			self.euclidean_distance(centroids_old[i], centroids[i]) for i in range(self.K)
		]
		return sum(distances) == 0

	
	def train(self, X):
		self.X = X 
		self.n_samples, self.n_features = X.shape 

		while True:
			self.clusters = self.create_clusters(self.centroids)
			centroids_old = self.centroids
			self.centroids = self.get_centroids(self.clusters)

			if self.is_converged(centroids_old, self.centroids):
				break
			
		return self.get_cluster_labels(self.clusters)

	
	def plot(self):
		for idx, cluster in enumerate(self.clusters):
			point = self.X[cluster].T
			plt.scatter(*point, marker = 'o', color = self.colors[idx])

		for idx, point in enumerate(self.centroids):
			plt.scatter(*point, marker = 's', color =  self.colors[idx], linewidth=2)
		
		plt.show()


if __name__ == "__main__":
	data = pd.read_csv("position.csv")
	X = data.values

	k = KMeans(K = 4)
	y_pred = k.train(X)
	print(k.centroids)
	k.plot()