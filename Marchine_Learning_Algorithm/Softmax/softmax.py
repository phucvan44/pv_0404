import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 

np.random.seed(43)


class SoftmaxRegression:


	def __init__(self):
		self.theta = None
		self.loss_his = []
		self.learning_rate = None
		self.epoch = None


	def train_test_split(self, X, y, test_size):
		size_data = len(X)
		limit = int(size_data*(1 - test_size))

		# Concatenate X with ones_matrix
		X = np.concatenate((X, np.ones((size_data, 1))), axis = 1)

		X_train = X[:limit, ::]
		X_test = X[limit:, ::]
		y_train = y[:limit]
		y_test = y[limit:]

		return (X_train, X_test, y_train, y_test)


	def	plot_data(self, X, y):
		plt.scatter(*X, marker = 'o', c = y)
		plt.title("Initial Data")
		plt.xlabel("X")
		plt.ylabel("y")
		plt.show()


	def plot_loss(self):
		plt.plot(self.loss_his)
		plt.title("Loss History")
		plt.xlabel("X")
		plt.ylabel("y")
		plt.show()


	def print_progress(self, index, total):
		percent = ("{0:.1f}").format(100 * ((index + 1) / total))
		filledLength = 50 * index // total
		bar = '=' * filledLength + '-' * (50 - filledLength - 1)
		print('\rTraining: |%s| %s%%' % (bar, percent), end = '\r')
		if index == total - 1:
			print()


	def fit(self, X_train, y_train):
		# Initial variable
		self.n_points, self.n_features = X_train.shape
		self.X = X_train
		self.labels = np.unique(y_train)
		self.labels.sort()
		self.theta = np.zeros((len(self.labels), self.n_features))
		self.y = np.zeros((self.n_points, len(self.labels)))
		for label in self.labels:	
			self.y[np.where(y_train[::] == label), label] = 1


	def softmax(self, fx):
		"""
			f(x) = X @ theta.T : Linear
			h(x) = softmax(fx) = exp(fx)/sum(exp(fx))
		"""
		hx = np.exp(fx) / np.sum(np.exp(fx), axis = 1).reshape(fx.shape[0], 1)
		return hx


	def gradient_descent(self, hx, X):
		delta_f_theta = (1 / self.n_points) * (hx.T @ X)
		return delta_f_theta


	def train(self, learning_rate, epoch):
		for i in range(epoch):
			self.print_progress(i, epoch)

			fx = self.X @ self.theta.T
			hx = self.softmax(fx)

			loss_value = - (1 / self.n_points) * np.sum(self.y * np.log(hx))
			self.loss_his.append(loss_value)

			delta_f_theta = self.gradient_descent(hx - self.y, self.X)
			self.theta -= learning_rate*delta_f_theta


	def predict(self, X):
		fx = X @ self.theta.T
		hx = self.softmax(fx)
		y_predict = np.argmax(hx, axis = 1)
		return y_predict


	def accuracy(self, y, y_predict):
		size_data = len(y)
		return np.sum(y == y_predict) / size_data


	def compare_value(self, y_test, y_predict):
		print("{:<30} {:<30}".format("Giá trị thực tế", "Giá trị dự đoán"))
		print('-' * 60)
		for i in range(len(y_test)):
			print("{:<30} {:<30}".format(y_test[i], y_predict[i]))
			print('-' * 60)


if __name__ == "__main__":
	data = pd.read_csv("commodity.csv")
	# Shuffle data values
	np.random.shuffle(data.values)

	smr = SoftmaxRegression()
	
	X_train, X_test, y_train, y_test = smr.train_test_split(data.values[::, :2], data.values[::, 2], 0.2) 

	smr.fit(X_train, y_train)

	learning_rate = 0.00006
	epoch = 100000
	smr.train(learning_rate, epoch)

	y_predict = smr.predict(X_test)
	
	# Compare model
	#smr.compare_value(y_test, y_predict)

	print("Accuracy:", smr.accuracy(y_test, y_predict))
	