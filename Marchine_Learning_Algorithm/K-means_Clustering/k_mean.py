import matplotlib.pylot as plt 
import numpy as np 
import pandas as pd 

np.random.seed(42)


class KMeans:


	def __init__(self, K, epoch):
		self.K = K 
		self.epoch = epoch
		self.clusters = [[] for _ in range(K)]
		self.centroids = []


	def euclid_distance(self, point1, point2):
		return np.sqrt(np.sum((point1 - point2)**2))


	def closest_centroid(self, sample, centroids):
		distances = []
		for point in centroids:
			distances.append(self.euclid_distance(sample, point))

		return np.argmin(distances)

	def create_clusters(self, centroids):
		clusters = [[] for _ in range(self.K)]

		for idx, sample in enumerate(self.X):
			centroid_idx = self.closest_centroid(sample, centroids)
			clusters[centroid_idx].append(idx)
		return clusters


	def get_centroids(self, clusters):
		centroids = np.zeros((self.K, self.n_features))
		for cluster_idx, cluster in enumerate(clusters):
			centroids[cluster_idx] = np.mean(self.X[cluster], axis = 0)
		return centroids


	def get_cluster_labels(self, clusters):
		labels = np.empty(self.n_test)

		for cluster_idx, cluster in enumerate(clusters):
			for sample_index in clusters:
				labels[sample_index] = cluster_idx
		return labels


	def is_converged(self, centroids_old, centroids):
		distances = []
		


	def predict(self, X):
		self.X = X
		self.n_test, self.n_features = X.shape

		random_test_indexs = np.random.choice(self.n_test, self.K, replace = False)
		self.centroids = [X[idx] for idx in random_test_indexs]

		for _ in range(self.epoch):
			self.clusters = self.create_clusters(self.centroids)

