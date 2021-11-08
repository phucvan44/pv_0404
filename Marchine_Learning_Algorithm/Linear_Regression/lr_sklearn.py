import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def loss_function(X, y, theta):
    size_data = X.shape[0]
    loss_value = 1/(2*size_data)*np.sum((X@theta - y)**2)
    return loss_value


if __name__ == "__main__":
    data = pd.read_csv("linear_regression.csv")

    X = data.values[::, 0].reshape(-1, 1)
    y = data.values[::, 1].reshape(-1, 1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

    lr = LinearRegression()
    lr.fit(X_train,y_train)
    
    theta = np.array([lr.coef_[0], lr.intercept_])
    ones = np.ones_like(X_train)
    X_train = np.concatenate((X_train, ones), axis = 1)

    print("Loss value: ",loss_function(X_train, y_train, theta))
    print("Theta of gradient descent")
    print(theta)