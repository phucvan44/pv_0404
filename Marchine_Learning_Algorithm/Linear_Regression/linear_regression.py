import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 


class Linear_Regression:

    def __init__(self):
        self.theta = []       # Theta of gradient descent
        self.X_label = []     # X_label for plot model after training data
        self.y_test = []      # y_test for compare with y_predict
        self.y_predict = []   # y_predict is predicted value
        self.loss_his = []    # loss_his is the loss list


    def plot_data(self, X, y):
        plt.plot(X, y, 'go')
        plt.title("Initial data")
        plt.xlabel("X")
        plt.ylabel("y")
        plt.show()


    def plot_model(self):
        plt.plot(self.X_label, self.y_test, 'go', self.X_label, self.y_predict)
        plt.title("Training data")
        plt.xlabel("X")
        plt.ylabel("y")
        plt.show()


    def plot_loss(self):
        x_label = np.arange(len(self.loss_his))
        plt.plot(x_label, self.loss_his, 'r')
        plt.title("Value of loss")
        plt.xlabel("X")
        plt.ylabel("y")
        plt.show()


    def train_test_split(self, X, y):
        
        X = X.reshape(len(X), 1)
        y = y.reshape(len(y), 1)

        limit = int(len(X)*8/10)

        X_train = X[:limit, ::]
        y_train = y[:limit, ::]

        X_test = X[limit:, ::]
        y_test = y[limit:, ::]

        X_label = X_test 
        self.X_label = X_label
        self.y_test = y_test

        # Concatenate X with 0
        ones_matrix_train = np.ones_like(X_train)
        ones_matrix_test = np.ones_like(X_test)
        X_train = np.concatenate((X_train, ones_matrix_train), axis = 1)
        X_test = np.concatenate((X_test, ones_matrix_test), axis = 1)

        return (X_train, X_test, y_train, y_test)


    def gradient_descent(self, X, y):
        n_data = X.shape[0]
        new_theta = (1/n_data)*X.T.dot(X.dot(self.theta) - y)
        return new_theta.reshape(self.theta.shape)

    
    def loss_function(self, X, y):
        n_data = X.shape[0]
        loss = 1/(2*n_data)*np.sum((X.dot(self.theta) - y)**2)
        return loss
    

    def predict(self, X):
        predict_value = X.dot(self.theta) # Shape of predict value is: (1,)
        self.y_predict.append(predict_value[0])
        return predict_value[0]


    def train(self, X, y, learning_rate, iter):

        # Initial theta of gradient descent
        self.theta = np.random.normal(size = 2).reshape([2, 1])

        for i in range(iter):
            new_theta = self.gradient_descent(X, y)
            self.theta -= new_theta*learning_rate
            loss = self.loss_function(X, y)
            self.loss_his.append(loss)


    def get_loss(self):
        return self.loss_his[-1]


    def compare_model(self):
        print("{:<30} {:<30}".format("Giá trị thực tế", "Giá trị dự đoán"))
        print('-'*60)
        
        for i in range(len(self.y_test)):
            print("{:<30} {:<30}".format(self.y_test[i][0], self.y_predict[i]))
            print('-'*60)


if __name__ == "__main__":

    data = pd.read_csv("linear_regression.csv")
    
    X = data.values[::, 0]
    y = data.values[::, 1]

    lr = Linear_Regression()

    # plot data
    #lr.plot_data(X, y) -- Code

    X_train, X_test, y_train, y_test = lr.train_test_split(X, y)

    learning_rate = 0.02
    iter = 10000

    lr.train(X_train, y_train, learning_rate, iter)

    n_data = X_test.shape[0]

    for i in range(n_data):
        predict_value = lr.predict(X_test[i])
    
    print("Loss value: ",lr.get_loss())

    # Compare y_predict with y_test
    #lr.compare_model()

    # Theta of model
    print("Theta of gradient descent")
    print(lr.theta)

    lr.plot_model()

