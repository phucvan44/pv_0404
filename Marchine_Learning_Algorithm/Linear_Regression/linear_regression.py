import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt


class Linear_Regression:

	
	def __init__(self):
		"""
			@theta: theta of gradient descent
			@loss_his: list loss of model
		"""
		self.theta = []
		self.loss_his = []


	def plot_data(self, X, y, title):
		plt.plot(X, y, 'ro')
		plt.title(title)
		plt.xlabel("X")
		plt.ylabel("y")
		plt.show()


	def plot_model(self, X_test, y_test, y_predict):
		X_test = X_test[::, :-1]
		plt.plot(X_test, y_test, 'ro', X_test, y_predict, 'b')
		plt.title("Train Model")
		plt.xlabel("X")
		plt.ylabel("y")
		plt.show()


	def train_test_split(self, X, y, test_size):
		size_data = X.shape[0]

		# Reshape X, y = (size_data, 1)
		X = X.reshape(size_data, 1)
		y = y.reshape(size_data, 1)

		#Concatenate X with one_matrix
		X = np.concatenate((X, np.ones_like(X)), axis = 1)

		# Calculate limit of data
		limit = int(size_data*(1 - test_size))

		# Split X_train, y_train
		X_train = X[:limit, ::]
		y_train = y[:limit, ::]

		# Split X_test, y_test
		X_test = X[limit:, ::]
		y_test = y[limit:, ::]

		return (X_train, X_test, y_train, y_test)


	def gradient_descent(self, X, y):
		"""
			delta_f_theta: derivative of f(theta) with respect to theta
		"""

		size_data = X.shape[0]
		delta_f_theta = (1/size_data)*X.T.dot(X.dot(self.theta) - y)
		return delta_f_theta.reshape(self.theta.shape)


	def loss_function(self, X, y):
		size_data = X.shape[0]
		loss_value = 1/(2*size_data)*np.sum((X.dot(self.theta) - y)**2)
		return loss_value


	def predict(self, X_test):
		y_predict = X_test.dot(self.theta)
		return y_predict


	def train(self, X, y, learning_rate, iter):
		# Initial theta of gradient descent
		self.theta = np.random.normal(size = X.shape[1]).reshape(X.shape[1], 1)

		# Training model
		for i in range(iter):
			delta_f_theta = self.gradient_descent(X, y)
			self.theta -= learning_rate*delta_f_theta 
			loss_value = self.loss_function(X, y)
			self.loss_his.append(loss_value)


	def compare_model(self, y_test, y_predict):
		print("{:<30} {:<30}".format("Giá trị thực tế", "Giá trị dự đoán"))
		print('-'*60)
		for i in range(len(y_test)):
			print("{:<30} {:<30}".format(y_test[i][0], y_predict[i][0]))
			print('-'*60)


	def get_loss(self):
		return self.loss_his


if __name__ == "__main__":
	data = pd.read_csv("linear_regression.csv")

	X = data.values[::, 0]
	y = data.values[::, 1]

	lr = Linear_Regression()

	# Show data 
	#lr.plot_data(X, y, "Initial Data")

	# Train test split
	X_train, X_test, y_train, y_test = lr.train_test_split(X, y, 0.2)

	learning_rate = 0.02
	iter = 10000

	# Train model
	lr.train(X_train, y_train, learning_rate, iter)

	# Predict values
	y_predict = lr.predict(X_test)
	#print(y_predict)

	# Compare y_test with y_predict
	#lr.compare_model(y_test, y_predict)

	# Loss history
	loss_his = lr.get_loss()
	print(loss_his[-1])

	# Show loss
	x_axis = np.arange(len(loss_his))
	#lr.plot_data(x_axis, loss_his)

	# Visualize 
	lr.plot_model(X_test, y_test, y_predict)
