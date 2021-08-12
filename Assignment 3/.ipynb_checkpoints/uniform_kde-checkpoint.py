import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import norm

a3_q7 = pd.read_csv('a3_q7.csv')
a3_q7_numpy = a3_q7.to_numpy()
D = a3_q7_numpy
x_array = np.arange(start=-0.01, stop=1.01, step=0.01)
h_array = [0.0001,  0.0005,  0.001,  0.005,  0.05]


def ker(u):
    if(u <= 1 and u >= -1):
        return 0.5
    else:
        return 0


def uniform_kde(x, h, D):
    sum_k = 0
    for points in D:
        u = (x-points[1])/h
        sum_k = sum_k + ker(u)

    return sum_k/(len(D)*h)


for i in range(len(h_array)):
    y = []
    for x in x_array:
        y.append(uniform_kde(x, h_array[i], D))
    tag = "h = "+str(h_array[i])
    plt.plot(x_array, y,label=tag)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend(bbox_to_anchor=(1.1, 1.05))
    plt.show()