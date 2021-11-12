import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def loss_function(X, y, theta):
	size_data = X.shape[0]
	loss_value = 1/(2*size_data) * np.sum((X @ theta - y)**2)
	return loss_value

if __name__ == "__main__":
	data = pd.read_csv("financial.csv")

	np.random.shuffle(data.values)

	X = data.values[::, 0].reshape(-1, 1)
	y = data.values[::, 1].reshape(-1, 1)

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

	model = LinearRegression()

	model.fit(X_train, y_train)

	theta = np.array([model.coef_[0], model.intercept_])

	X_test = np.concatenate((X_test, np.ones_like(X_test)), axis = 1)

	print("Loss: ", loss_function(X_test, y_test, theta))