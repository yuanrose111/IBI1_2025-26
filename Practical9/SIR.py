

# Import libraries
# Set population, beta, gamma, time steps
# Initialize S=9999, I=1, R=0
# Create lists to save S, I, R
# Loop 1000 times:
#   Calculate new infected people
#   Calculate new recovered people
#   Update S, I, R
#   Save current values
# Plot S, I, R over time




import numpy as np
import matplotlib.pyplot as plt

N = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000

S = N - 1
I = 1
R = 0

S_history = [S]
I_history = [I]
R_history = [R]

for _ in range(time_steps):
    inf_prob = beta * I / N
    new_inf = np.random.binomial(S, inf_prob)
    new_rec = np.random.binomial(I, gamma)

    S -= new_inf
    I += new_inf - new_rec
    R += new_rec

    S_history.append(S)
    I_history.append(I)
    R_history.append(R)

plt.figure(figsize=(6,4), dpi=150)
plt.plot(S_history, label='Susceptible')
plt.plot(I_history, label='Infected')
plt.plot(R_history, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of individuals')
plt.title('Stochastic SIR Model')
plt.legend()
plt.show()