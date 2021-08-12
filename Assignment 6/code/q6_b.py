import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import math
import pandas as pd

data = pd.read_csv('q6.csv').to_numpy()
sigma = 1.0
mu = 0.5
def MAP_decision(X, p):
    r = ((sigma**2)/(2 * mu)) * (np.log(p/(1 - p)))
    l = np.sum(X)
    if l <= r:
        return 0
    else:
        return 1
    

probs = [0.1, 0.3, 0.5, 0.8]

for p in probs:
    print("\n For P(H_0) = "+ str(p) +", the hypotheses selected are : ", end=" ")
    for i in range(0, data.shape[1]):
        c = MAP_decision(data[:,i], p)
        print(c, end=" ")