import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 


class LinearRegression:


	def __init__(self):
		"""
			theta: theta of gradient descent
			loss_his: list loss of model
		"""
		self.theta = []
		self.loss_his = []


	def plot_data(self, X, y, title):
		plt.plot(X, y, 'g^')
		plt.title(title)
		plt.xlabel("X")
		plt.ylabel("y")
		plt.show()


	def plot_model(self, X, y, y_predict):
		X = X[::, :-1]
		plt.plot(X, y, 'ro', X, y_predict, 'b')
		plt.title("Train Model")
		plt.xlabel("X")
		plt.ylabel("y")
		plt.show()


	def train_test_split(self, X, y, test_size):
		size_data = X.shape[0]

		# Concatenate X with ones_matrix
		X = np.concatenate((X, np.ones_like(X)), axis = 1)

		# Calculate limit of data 
		limit = int(size_data*(1 - test_size))

		# Split X_train, y_train
		X_train = X[:limit]
		y_train = y[:limit]

		# Split X_test, y_test
		X_test = X[limit:]
		y_test = y[limit:]

		return (X_train, X_test, y_train, y_test)


	def gradient_descent(self, X, y, theta):
		"""
			delta_f_theta: derivative of f(theta) with respect to theta 
		"""
		size_data = X.shape[0]
		delta_f_theta = (1/size_data) * X.T @ (X @ theta - y)
		return delta_f_theta.reshape(theta.shape)


	def loss_function(self, X, y, theta):
		size_data = X.shape[0]
		loss_value = 1/(2*size_data) * np.sum((X @ theta - y)**2)
		return loss_value


	def print_progress(self, index, total):
		percent = ("{0:.1f}").format(100 * ((index + 1) / total))
		filledLength = 50 * index // total
		bar = '=' * filledLength + '-' * (50 - filledLength - 1)
		print('\rTraining: |%s| %s%%' % (bar, percent), end = '\r')
		if index == total - 1:
			print()


	def train(self, X, y, learning_rate, epoch):
		# Initial theta of gradient descent
		self.theta = np.random.normal(size = X.shape[1]).reshape(X.shape[1], 1)

		for i in range(epoch):
			self.print_progress(i, epoch)
			delta_f_theta = self.gradient_descent(X, y, self.theta)
			self.theta -= learning_rate * delta_f_theta
			loss_value = self.loss_function(X, y, self.theta)
			self.loss_his.append(loss_value)


	def predict(self, X):
		return X @ self.theta


	def compare_value(self, y_test, y_predict):
		print("{:<30} {:<30}".format("Giá trị thực tế", "Giá trị dự đoán"))
		print('-' * 60)
		for i in range(len(y_test)):
			print("{:<30} {:<30}".format(y_test[i][0], y_predict[i][0]))
			print('-' * 60)


	def get_loss(self):
		return self.loss_his


if __name__ == "__main__":
    data = pd.read_csv("financial.csv")
    
    # Shuffle data values
    np.random.shuffle(data.values)

    X = data.values[::, 0].reshape(-1, 1)
    y = data.values[::, 1].reshape(-1, 1)
    
    model = LinearRegression()

    # Show data 
    #model.plot_data(X, y, "Initial Data")

    # Train test split
    X_train, X_test, y_train, y_test = model.train_test_split(X, y, 0.3)

    learning_rate = 0.00003
    epoch = 1000000

    # Train model
    model.train(X_train, y_train, learning_rate, epoch)

    # Predict values
    y_predict = model.predict(X_test)
    #print(y_predict)

    # Compare y_test with y_predict
    #model.compare_value(y_test, y_predict)

    # Loss history
    loss_his = model.get_loss()
    print("Loss:", loss_his[-1])

    # Show loss
    x_axis = np.arange(len(loss_his))
    #model.plot_data(x_axis, loss_his)

    # Visualize 
    model.plot_model(X_test, y_test, y_predict)
