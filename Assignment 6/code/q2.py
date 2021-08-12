import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import math
from tabulate import tabulate

def cal_posterior(fname, sigma):
    a_file = open(fname)
    file_contents = a_file.read()
    contents_split = file_contents.splitlines()
    data = np.zeros((5, 100))

    for i in range(len(contents_split)):
        contents_split[i] = contents_split[i].replace(' ', '')
        data_raw = contents_split[i].split(',')
        for j in range(len(data_raw)):
            data[i][j] = float(data_raw[j])
            
    mean_var = []
    a = 0
    b_sqr = 1
    n = data.shape[1]
    sigma_sqr = sigma ** 2
    se_sqr = sigma_sqr/n

    i = 1
    for dataline in data:
        x_bar = dataline.mean()

        x = ((b_sqr * x_bar) + (se_sqr * a)) / (b_sqr + se_sqr)
        y = (b_sqr * se_sqr) / (b_sqr + se_sqr)

        mean_var.append([i, x, y])

        a = x
        b_sqr = y
        i+=1
    
    print(tabulate(mean_var, headers=["Posterior", "Mean", "Variance"], tablefmt="grid"))     
    
    for i in range(len(mean_var)):  
        mu = mean_var[i][1]
        variance = mean_var[i][2]
        sigma = math.sqrt(variance)
        x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
        plt.plot(x, stats.norm.pdf(x, mu, sigma), label= " Posterior" + str(i+1))

    plt.xlabel("X-axis")
    plt.ylabel("Probability Density")
    plt.legend()
    plt.show()

cal_posterior('q2_sigma3.dat', 3)
cal_posterior('q2_sigma100.dat', 100)