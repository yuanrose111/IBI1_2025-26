
# Import libraries
# Set population, infection rate, recovery rate
# Test vaccination rates from 0% to 100%
# For each vaccination rate:
#     Set initial S, I, R
#     Run simulation for 1000 steps
#     Calculate new infections and recoveries
#     Update S, I, R (never let them be negative)
#     Record infected numbers
# Plot all infection curves


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Parameters
N = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000
vaccination_rates = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

plt.figure(figsize=(6, 4), dpi=150)

for idx, rate in enumerate(vaccination_rates):
    vaccinated = int(N * rate)
    S = N - vaccinated - 1
    I = 1
    R = vaccinated
    I_history = [I]

    for _ in range(time_steps):
       
        if S > 0:
            inf_prob = beta * I / N
            new_inf = np.random.binomial(S, inf_prob)
        else:
            new_inf = 0

        
        if I > 0:
            new_rec = np.random.binomial(I, gamma)
        else:
            new_rec = 0

        
        S -= new_inf
        I += new_inf - new_rec
        R += new_rec

        
        S = max(S, 0)
        I = max(I, 0)

        I_history.append(I)

    # Plot
    plt.plot(I_history, label=f'{int(rate*100)}%', color=cm.viridis(idx * 25))

plt.xlabel('Time')
plt.ylabel('Infected individuals')
plt.title('SIR Model with Vaccination')
plt.legend(title='Vaccination rate')
plt.savefig('SIR_vaccination.png')
plt.show()