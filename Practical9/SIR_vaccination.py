import numpy as np
import matplotlib.pyplot as plt

# --------------------------
# Step 1: Define model parameters
# --------------------------
# Total population size
N = 10000
# Transmission rate (beta) and recovery rate (gamma)
beta = 0.3
gamma = 0.05
# Number of time steps to simulate
time_steps = 1000
# Vaccination rates to test (0% to 100% in 10% increments)
vaccination_rates = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
# Color map for plotting (matches the example gradient)
colors = plt.cm.viridis(np.linspace(0, 1, len(vaccination_rates)))

# --------------------------
# Step 2: Define simulation function for a given vaccination rate
# --------------------------
def simulate_SIR_vaccination(vaccine_rate, N, beta, gamma, time_steps):
    """
    Simulate SIR model with a given vaccination rate.
    Returns the time series of infected individuals.
    """
    # Initial conditions: vaccinated people are removed from susceptible pool
    V0 = int(N * vaccine_rate)
    S0 = max(0, N - V0 - 1)   # 1 initial infected, rest susceptible (minus vaccinated)
    I0 = 1
    R0 = 0
    
    # Initialize arrays to track population over time
    S = [S0]
    I = [I0]
    R = [R0]
    V = [V0]  # Vaccinated population remains constant (no waning immunity)
    
    # Simulate over time steps
    for t in range(time_steps):
        current_S = S[-1]
        current_I = I[-1]
        current_R = R[-1]
        current_V = V[-1]
        
        # Calculate infection probability for susceptible individuals
        # Only susceptible people can be infected; vaccinated are immune
        infection_prob = beta * (current_I / N)
        
        # Simulate new infections
        infection_outcomes = np.random.choice([0, 1], size=current_S, p=[1 - infection_prob, infection_prob])
        new_infections = np.sum(infection_outcomes)
        
        # Simulate new recoveries
        recovery_outcomes = np.random.choice([0, 1], size=current_I, p=[1 - gamma, gamma])
        new_recoveries = np.sum(recovery_outcomes)
        
        # Update population counts
        next_S = current_S - new_infections
        next_I = current_I + new_infections - new_recoveries
        next_R = current_R + new_recoveries
        next_V = current_V  # Vaccinated count stays the same
        
        # Append to tracking arrays
        S.append(next_S)
        I.append(next_I)
        R.append(next_R)
        V.append(next_V)
    
    # Return only the infected time series for plotting
    return I

# --------------------------
# Step 3: Run simulations for all vaccination rates
# --------------------------
infected_series = []
for rate in vaccination_rates:
    infected = simulate_SIR_vaccination(rate, N, beta, gamma, time_steps)
    infected_series.append(infected)

# --------------------------
# Step 4: Plot the results
# --------------------------
# Set up figure dimensions and resolution
plt.figure(figsize=(8, 5), dpi=150)

# Plot infected curves for each vaccination rate
for i, (rate, infected) in enumerate(zip(vaccination_rates, infected_series)):
    plt.plot(infected, label=f'{int(rate*100)}%', color=colors[i])

# Add plot labels, title, and legend
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
plt.legend(title='Vaccination rate')
plt.grid(False)

# Save the plot to a file
plt.savefig('SIR_vaccination_plot.png', format='png')

# Show the plot
plt.show()
