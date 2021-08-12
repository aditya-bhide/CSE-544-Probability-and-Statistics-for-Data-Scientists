import numpy as np
# Taking N as input
n = int(input("Enter value of n: "))
N = 10 ** n

np.random.seed(7)

##### Part a #####

p = 0.5
lac_wins = np.random.binomial(4, p, N)

# Number of times LAC won 3 out of first 4 games
N_a = np.count_nonzero(lac_wins == 3)
print("For N = ", N,  " the simulated value for part (a) is", (N_a / N))


##### Part c #####

den_wins = np.random.binomial(3, 0.5, N)

N_ba = 0
for i, j in zip(lac_wins, den_wins):
    # Intersection of LAC win 3 out of first four and DEN win 3 out of last 3
    if i == 3 and j == 3:
        N_ba += 1

print("For N = ", N, " the simulated value for part (c) is", (N_ba / N_a))


##### Part e #####
lac_wins = np.random.binomial(2, 0.75, N)  # Home LAC
lac_wins += np.random.binomial(2, 0.25, N)  # Home DEN

# Number of times LAC won 3 out of first 4 games
N_a = np.count_nonzero(lac_wins == 3)

den_wins = np.random.binomial(1, 0.25, N)  # Home LAC
den_wins += np.random.binomial(1, 0.75, N)  # Home DEN
den_wins += np.random.binomial(1, 0.25, N)  # Home LAC

N_ba = 0
for i, j in zip(lac_wins, den_wins):
    # Intersection of LAC win 3 out of first four and DEN win 3 out of last 3
    if i == 3 and j == 3:
        N_ba += 1

print("For N = ", N, " the simulated value for part (e) is", (N_ba / N_a))

##### OUTPUT #####
"""
Enter value of n: 7
For N =  10000000  the simulated value for part (a) is 0.2500839
For N =  10000000  the simulated value for part (c) is 0.12501364542059684
For N =  10000000  the simulated value for part (e) is 0.046768217584235286
"""
