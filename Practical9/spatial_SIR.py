"""
1. Initialize 100x100 grid with all susceptible (0)
2. Randomly set 1 cell to infected (1)
3. Define model parameters: beta=0.3, gamma=0.05, time_steps=100
4. For each time step from 0 to 99:
    a. Find all currently infected cells (value=1) using np.where()
    b. For each infected cell:
        i. Check all 8 neighboring cells
        ii. For each neighbor that is susceptible (0):
            - Infect with probability beta (set to 1)
        iii. The infected cell recovers with probability gamma (set to 2)
    c. Plot the current state of the grid to show disease spread
5. Ensure grid boundaries are handled (no out-of-bounds errors)
"""

# import necessary libraries
import numpy as np
import matplotlib . pyplot as plt

# --------------------------
# Step 1: Define model parameters
# --------------------------
# Grid size (100x100 population grid)
grid_size = 100
# Transmission rate (beta) and recovery rate (gamma)
beta = 0.3
gamma = 0.05
# Number of time steps to simulate
time_steps = 100

# make array of all susceptible population
population = np.zeros((100, 100))
# start with one random person infected
outbreak = np.random. choice(range(100), 2)
population [outbreak[0] , outbreak[1]] = 1

# plot this
plt.figure (figsize =(6,4),dpi=150)
plt.imshow(population , cmap='viridis' , interpolation='nearest')
plt.title('Initial State (Time 0)')
plt.colorbar(ticks=[0, 1, 2], label='State: 0=Susceptible, 1=Infected, 2=Recovered')
plt.show()

# --------------------------
# Step 3: Simulate spatial SIR model over time
# --------------------------
for step in range(time_steps):
    # find infected points
    infectedIndex = np.where(population == 1)
    
    # loop through all infected points
    for i in range(len(infectedIndex[0])):
        # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        
        # infect all 8 neighbours
        for xNeighbour in range(x-1, x+2):
            for yNeighbour in range(y-1, y+2):
                # don't infect yourself
                if (xNeighbour, yNeighbour) != (x, y):
                    # make sure don't fall off edge
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour != 100 and yNeighbour != 100:
                        # only infect susceptible neighbours
                        if population[xNeighbour, yNeighbour] == 0:
                            population[xNeighbour, yNeighbour] = np.random.choice(range(2), 1, p=[1-beta, beta])[0]
        
        # Recovery
        if np.random.rand() < gamma:
            population[x, y] = 2

    # ======================
    # PLOT AT TIME 10, 50, 100
    # ======================
    if step + 1 in [10, 50, 100]:
        plt.figure(figsize=(6,4), dpi=150)
        plt.imshow(population, cmap='viridis')
        plt.title(f"Spatial SIR Model (Time {step+1})")
        plt.colorbar(label='0=Susceptible, 1=Infected, 2=Recovered')
        plt.show()





    
