import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt


class LinearRegression:

	
	def __init__(self):
		self.theta = []
		self.loss = 0.0


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

		#Concatenate X with one_matrix
		X = np.concatenate((X, np.ones_like(X)), axis = 1)

		# Calculate limit of data
		limit = int(size_data * (1 - test_size))

		# Split X_train, y_train
		X_train = X[:limit, ::]
		y_train = y[:limit, ::]

		# Split X_test, y_test
		X_test = X[limit:, ::]
		y_test = y[limit:, ::]

		return (X_train, X_test, y_train, y_test)


	def normal_equation(self, X, y, theta):
		theta = np.linalg.inv(X.T @ X) @ (X.T @ y)
		return theta


	def loss_function(self, X, y, theta):
		size_data = X.shape[0]
		loss_value = (1/size_data) * np.sum((X @ theta - y)**2)
		return loss_value


	def fit(self, X, y):
		# Initial theta
		self.theta = self.normal_equation(X, y, self.theta)
		self.loss = self.loss_function(X, y, self.theta)


	def predict(self, X):
		return X @ self.theta


	def compare_value(self, y_test, y_predict):
		print("{:<30} {:<30}".format("Giá trị thực tế", "Giá trị dự đoán"))
		print('-' * 60)
		for i in range(len(y_test)):
			print("{:<30} {:<30}".format(y_test[i][0], y_predict[i][0]))
			print('-' * 60)


	def get_loss(self):
		return self.loss


if __name__ == "__main__":
    data = pd.read_csv("linear_regression.csv")
    
    X = data.values[::, 0].reshape(-1, 1)
    y = data.values[::, 1].reshape(-1, 1)
    
    model = LinearRegression()

    # Show data 
    #model.plot_data(X, y, "Initial Data")

    # Train test split
    X_train, X_test, y_train, y_test = model.train_test_split(X, y, 0.2)

    # Train model
    model.fit(X_train, y_train)

    # Predict values
    y_predict = model.predict(X_test)
    #print(y_predict)

    # Compare y_test with y_predict
    #model.compare_value(y_test, y_predict)

    # Loss history
    loss_value = model.get_loss()
    print("Loss:", loss_value)

    # Visualize 
    model.plot_model(X_test, y_test, y_predict)
