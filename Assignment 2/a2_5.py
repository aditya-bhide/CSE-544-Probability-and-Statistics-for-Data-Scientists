import numpy as np

# Transition matrix columns in sequence CC CS SC SS
P = [[0.9, 0, 0.1, 0],
[0.8, 0, 0.2, 0],
[0, 0.5, 0, 0.5],
[0, 0.1, 0, 0.9]]

P = np.array(P)

def steady_state_power (P):
    power = 1
    current_state = P.copy()
    previous_state = np.linalg.matrix_power(P, power)
    
    # Keep calculating new state until steady state is achieved
    while True:
        power += 1
        current_state = np.linalg.matrix_power(P, power)
        
        # Check if previous state is same as current state
        if np.array_equal(previous_state, current_state):
            print("\nSteady state achieved after ", power, "iterations.")
            break
            
        # current state becomes previous state  
        previous_state = current_state.copy()
        
    a = current_state[0]
    return a, steady_state_matrix

steady_states, steady_state_matrix = steady_state_power(P)
print(steady_states)


pr_three_days = np.linalg.matrix_power(steady_state_matrix, 3)
print("\nSteady state probability after 3 days: ",pr_three_days[0])
print("\nProbability that it will be snowy after 3 days: ", (pr_three_days[0][1] + pr_three_days[0][3]))



########## OUTPUT ##########
"""
Steady state achieved after  1761 iterations.
[0.53333333 0.06666667 0.06666667 0.33333333]

Steady state probability after 3 days:  [0.53333333 0.06666667 0.06666667 0.33333333]

Probability that it will be snowy after 3 days:  0.4
"""