import numpy as np
import matplotlib.pyplot as plt

# Constants for the simulation parameters
MATERIAL_COST_MEAN = 10_000_000
MATERIAL_COST_STD = 1_000_000

LABOR_COST_MEAN = 6_000_000
LABOR_COST_STD = 600_000

OVERHEAD_COST_MIN = 500_000
OVERHEAD_COST_MAX = 1_000_000

NUM_SIMULATIONS = 10_000

# Store total costs for each simulation run
total_costs = []

# Monte Carlo simulation loop
for _ in range(NUM_SIMULATIONS):
    # Generate random costs based on defined distributions
    material_cost = np.random.normal(MATERIAL_COST_MEAN, MATERIAL_COST_STD)
    labor_cost = np.random.normal(LABOR_COST_MEAN, LABOR_COST_STD)
    overhead_cost = np.random.uniform(OVERHEAD_COST_MIN, OVERHEAD_COST_MAX)

    # Calculate the total cost for this iteration
    total_cost = material_cost + labor_cost + overhead_cost
    total_costs.append(total_cost)

# Convert list to a NumPy array for statistical analysis
total_costs = np.array(total_costs)
average_cost = total_costs.mean()
cost_std_dev = total_costs.std()
cost_90th_percentile = np.percentile(total_costs, 90)

# Output statistical results
print(f'Average Total Cost: {average_cost:,.2f}')
print(f'Standard Deviation of Total Cost: {cost_std_dev:,.2f}')
print(f'90th Percentile of Total Cost: {cost_90th_percentile:,.2f}')

# Plot the distribution of total costs
plt.figure(figsize=(8, 6))
plt.hist(total_costs, color="skyblue", edgecolor="black", bins=50)
plt.title('Distribution of Total Costs')
plt.xlabel('Total Cost')
plt.ylabel('Frequency')
plt.axvline(average_cost, color='green', linestyle='dashed', label='Average')
plt.axvline(cost_90th_percentile, color='red', linestyle='dashed', label='90th Percentile')
plt.legend()
plt.show()
