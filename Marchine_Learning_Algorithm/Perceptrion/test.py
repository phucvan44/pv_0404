import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 


class Perceptron:


	def __init__(self, learning_rate, epoch):
		self.learning_rate = learning_rate 
		self.epoch = epoch 
		self.weights = None
		self.bias = 0


	def print_progress(self, index, total):
		percent = ("{0:.1f}").format(100 * ((index + 1) / total))
		filledLength = 50 * index // total
		bar = '=' * filledLength + '-' * (50 - filledLength - 1)
		print('\rTraining: |%s| %s%%' % (bar, percent), end = '\r')
		if index == total - 1:
			print()


	def signum(self, X):
		return np.where(X >= 0, 1, 0)


	def fit(self, X, y):
		n_points, n_features = X.shape

		# Initial weights
		self.weights = np.zeros(n_features)

		for i in range(self.epoch):
			self.print_progress(i, epoch)

			for point_idx, point in enumerate(X):
				linear_output = (point @ self.weights) + self.bias
				y_predict = self.signum(linear_output)

				delta = self.learning_rate * (y[point_idx] - y_predict)

				self.weights += delta*point
				self.bias += delta


	def predict(self, X):
		linear_output = (X @ self.weights) + self.bias 
		return self.signum(linear_output)


	def accuracy(self, y_true, y_predict):
		n_data = y_true.shape[0]
		return np.sum(y_true == y_predict)/n_data


	def plot(self, X, y):
		# Plot point 
		plt.scatter(X[::, 0], X[::, 1], marker = "o", c = y)

		# Divide line
		X0 = np.amin(X[:: , 0])
		y0 = (- X0 * self.weights[0] - self.bias) / self.weights[1]
		X1 = np.amax(X[:: , 0])
		y1 = (- X1 * self.weights[0] - self.bias) / self.weights[1]
		plt.plot([X0, X1], [y0, y1], "k")

		plt.title("Perceptrion Learning Algorithm")
		plt.xlabel("X")
		plt.ylabel("y")

		plt.show()


if __name__ == "__main__":
	data = pd.read_csv("PLA.csv")
	# Shuffle data values
	np.random.shuffle(data.values)

	X = data.values[::, :2]
	y = data.values[::, 2]

	learning_rate = 0.002
	epoch = 10000

	p = Perceptron(learning_rate, epoch)
	p.fit(X, y)

	predictions = p.predict(X)
	print("Accuracy: ", p.accuracy(y, predictions))

	p.plot(X, y)