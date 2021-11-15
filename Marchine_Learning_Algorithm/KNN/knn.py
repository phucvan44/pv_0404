import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

np.random.seed(8)


class KNN:


	def __init__(self, K):
		self.K = K;


	def euclidean_distance(self, point1, point2):
		return np.sqrt(np.sum((point1 - point2)**2))


	def fit(self, X, y):
		self.X = X
		self.y = y


	def get_labels_train(self, index_list):
		labels = [
			self.y[idx] for idx in index_list
		]
		return labels


	def get_label_max_occur(self, knn_labels):
		ans = None
		labels = set(knn_labels.copy())
		max_occur = 0

		for label in labels:
			count = knn_labels.count(label)
			if count > max_occur:
				max_occur = count 
				ans = label
		return ans 


	def predict(self, X_test):
		labels_predict = []

		for point in X_test:
			distances = [
				self.euclidean_distance(point, point_train) for point_train in self.X
			]
			k_first_idx = np.argsort(distances)[:self.K]
			knn_labels = self.get_labels_train(k_first_idx)
			labels_predict.append(self.get_label_max_occur(knn_labels))
		return np.array(labels_predict)


	def accuracy(self, y, y_predict):
		size_data = len(y)
		return np.sum(y == y_predict)/size_data


	def compare_model(self, y_test, y_predict):
		print("{:<30} {:<30}".format("Giá trị thực tế", "Giá trị dự đoán"))
		print('-' * 60)
		for i in range(len(y_test)):
			print("{:<30} {:<30}".format(y_test[i], y_predict[i]))
			print('-' * 60)


def train_test_split(data, test_size):
	size_data = len(data.values)
	limit = int(size_data*(1-test_size)) 

	data = np.array(data[["fruit_label", "mass", "width", "height"]])
	# Shuffle data values
	np.random.shuffle(data)

	X_train = data[:limit, 1:]
	X_test = data[limit:, 1:]
	y_train = data[:limit, 0]
	y_test = data[limit:, 0]

	return (X_train, X_test, y_train, y_test)


if __name__ == "__main__":
    data = pd.read_csv("fruits.txt", sep = "\t")

    X_train, X_test, y_train, y_test = train_test_split(data, 0.2)

    knn = KNN(3)
    knn.fit(X_train, y_train)

    y_predict = knn.predict(X_test)

    print("accuracy:", knn.accuracy(y_test, y_predict))

    knn.compare_model(y_test, y_predict)