import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.linalg import inv

def get_equation(beta):
    eq = ''
    for i in range(beta.shape[0]):
        if beta[i] >= 0:
            eq += " +" +str(beta[i]) + " x_" + str(i) + " "
        else:
            eq += str(beta[i]) + " x_" + str(i)+ " "
    return eq

def pred_MLR(X, Y, part):
    X = X.to_numpy()
    Y = Y.to_numpy()
    
    X_train = X[:400]
    Y_train = Y[:400]

    X_test = X[400:]
    Y_test = Y[400:]
    
    p1 = inv(np.matmul(np.transpose(X_train), X_train))
    beta = np.matmul(np.matmul(p1, np.transpose(X_train)), Y_train)
    print("Equation for part "+part+":\n", get_equation(beta))

    Y_pred = np.matmul(X_test, beta)

    SSE = 0
    for i in range(Y_pred.shape[0]):
        SSE += (Y_test[i] - Y_pred[i]) ** 2

    print("SSE: ", SSE,"\n")
    
data = pd.read_csv('q5.csv')
Y = data['Chance of Admit']

X = data.drop(['Chance of Admit'], axis=1)
pred_MLR(X, Y, "a")

X = data[['TOEFL Score', 'SOP', 'LOR']]
pred_MLR(X, Y, "b")

X = data[['GRE Score', 'GPA']]
pred_MLR(X, Y, "c")