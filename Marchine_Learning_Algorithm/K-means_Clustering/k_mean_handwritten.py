import matplotlib.pyplot as plt 
import pandas as pd 


class MathSupport:


	def euclidean_distance(self, point1, point2):
		vector = [point1[idx] - point2[idx] for idx in range(len(point1))]
		distance = sum(vector)**(1/2)
		return distance


	def average_by_id_column(self, points, id_column):
		column_value = [points[idx][id_column] for idx in range(len(points))]
		sum_column = sum(column_value)
		return sum_column/len(points)


class KMeans(MathSupport):
	colors = ["red", "green", "blue", "yellow"]


	def __init__(self, K):
		MathSupport.__init__(self)

		self.K = K
		self.clusters = [[] for _ in range(self.K)]
		self.centroids = [[30, -60], [40, -10], [20, 10], [-20, 40]]


	def closest_centroids(self, point, centroids):
		distances = [
			self.euclidean_distance(point, centroid) for centroid in centroids
		]
		return distances.index(min(distances))


	def create_clusters(self, centroids):
		clusters = [[] for _ in range(self.K)]
		for idx, point in enumerate(self.X):
			centroid_idx = self.closest_centroids(point, self.centroids)
			clusters[centroid_idx].append(idx)
		return clusters


	def get_centroids(self, clusters):
		centroids = [[0 for i in range(self.n_features)] for j in range(self.K)]
		for cluster_idx, cluster in enumerate(clusters):
			points = [self.X[idx] for idx in cluster]
			print("====\n",points,"\n====\n")
			centroids[cluster_idx] = [
				self.average_by_id_column(points, i) for i in range(len(points[0]))
			]
		return centroids


	def get_clusters_labels(self, clusters):
		labels = [0 for _ in range(self.n_points)]
		for cluster_idx, cluster in enumerate(clusters):
			for point_idx in cluster:
				labels[point_idx] = cluster_idx
		return labels


	def is_converged(self, centroids_old, centroids):
		distances = [
			self.euclidean_distance(centroids_old[idx], centroids[idx]) for idx in range(self.K)
		]	
		return sum(distances) == 0


	def predict(self, X):
		self.X = X
		self.n_points = len(X)
		self.n_features = len(X[0])

		while True:
			self.clusters = self.create_clusters(self.centroids)
			centroids_old = self.centroids 
			self.centroids = self.get_centroids(self.clusters)

			if self.is_converged(centroids_old, self.centroids):
				break
		return self.get_clusters_labels(self.clusters)


if __name__ == "__main__":
	data = pd.read_csv("position.csv")
	X = [[data.values[i][0], data.values[i][1]] for i in range(len(data.values))]

	k = KMeans(K = 4)

	y_pred = k.predict(X)

	print(k.centroids)

	#k.plot()	