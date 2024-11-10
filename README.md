# Monte Carlo Simulation of Project Costs

This project simulates the distribution of total project costs using a Monte Carlo method. The simulation models the variability in three main cost components: **material costs**, **labor costs**, and **overhead costs**. Each cost component has its own probability distribution, reflecting real-world uncertainties in budgeting.

## Project Structure and Key Elements

1. **Cost Parameters**: The simulation uses three primary cost categories with predefined mean and standard deviation values:
   - **Material Costs**: Modeled as a normal distribution with a mean of $10,000,000 and a standard deviation of $1,000,000.
   - **Labor Costs**: Modeled as a normal distribution with a mean of $6,000,000 and a standard deviation of $600,000.
   - **Overhead Costs**: Modeled as a uniform distribution ranging between $500,000 and $1,000,000.

2. **Monte Carlo Simulation**: 
   - The simulation iterates **10,000 times** (configurable) to generate a distribution of total project costs.
   - In each iteration, the code generates random values for each cost component based on its respective distribution and calculates the total cost by summing these values.

3. **Statistical Analysis**:
   - The code calculates the **average total cost**, the **standard deviation**, and the **90th percentile** of the total costs after all simulations.
   - These metrics provide insights into the expected project cost and the range of possible cost outcomes.

4. **Visualization**:
   - A histogram of the total costs is generated to show the distribution. 
   - The plot includes vertical lines indicating the **average cost** (in green) and the **90th percentile** (in red) to help identify key points in the cost distribution.
