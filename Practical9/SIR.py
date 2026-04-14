#1. Initialize parameters: N=10000, S0=9999, I0=1, R0=0, beta=0.3, gamma=0.05, time_steps=1000
#2. Create empty lists S, I, R, and append initial values S0, I0, R0
#3. For each time step from 0 to 999:
#    a. Get current S, I, R values from the end of the lists
#    b. Calculate infection probability: infection_prob = beta * (current_I / N)
#    c. Simulate new infections:
#        - Randomly select current_S individuals with infection_prob to become infected
#        - Count the number of new infections
#    d. Simulate new recoveries:
#        - Randomly select current_I individuals with gamma probability to recover
#        - Count the number of new recoveries
#    e. Update next_S = current_S - new_infections
#       Update next_I = current_I + new_infections - new_recoveries
#       Update next_R = current_R + new_recoveries
#    f. Append next_S, next_I, next_R to the lists S, I, R
#4. Plot S, I, R over time with labels, title, and legend
# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# --------------------------
# Step 1: Define model parameters and initial conditions
# --------------------------
# Total population size
N = 10000
# Initial number of susceptible, infected, recovered individuals
S0 = N - 1
I0 = 1
R0 = 0
# Transmission rate (beta) and recovery rate (gamma)
beta = 0.3
gamma = 0.05
# Number of time steps to simulate
time_steps = 1000

# --------------------------
# Step 2: Initialize arrays to track population over time
# --------------------------
S = [S0]
I = [I0]
R = [R0]

# --------------------------
# Step 3: Simulate the SIR model over time
# --------------------------
for t in range(time_steps):
    # Get current number of individuals in each compartment
    current_S = S[-1]
    current_I = I[-1]
    current_R = R[-1]
    
    # Calculate infection probability for susceptible individuals
    # Probability = beta * (proportion of infected individuals in population)
    infection_prob = beta * (current_I / N)
    
    # Simulate new infections: randomly select susceptible individuals to become infected
    # 1 = infected, 0 = remains susceptible
    infection_outcomes = np.random.choice([0, 1], size=current_S, p=[1 - infection_prob, infection_prob])
    new_infections = np.sum(infection_outcomes)
    
    # Simulate recoveries: randomly select infected individuals to recover
    # 1 = recovered, 0 = remains infected
    recovery_outcomes = np.random.choice([0, 1], size=current_I, p=[1 - gamma, gamma])
    new_recoveries = np.sum(recovery_outcomes)
    
    # Update the counts for the next time step
    next_S = current_S - new_infections
    next_I = current_I + new_infections - new_recoveries
    next_R = current_R + new_recoveries
    
    # Append new values to the tracking arrays
    S.append(next_S)
    I.append(next_I)
    R.append(next_R)

# --------------------------
# Step 4: Plot the results
# --------------------------
# Set up figure dimensions and resolution
plt.figure(figsize=(6, 4), dpi=150)

# Plot each compartment over time
plt.plot(S, label='susceptible', color='#1f77b4')
plt.plot(I, label='infected', color='#ff7f0e')
plt.plot(R, label='recovered', color='#2ca02c')

# Add plot labels and title
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()

# Save the plot to a file
plt.savefig('SIR_model_plot.png', format='png')

# Show the plot
plt.show()
