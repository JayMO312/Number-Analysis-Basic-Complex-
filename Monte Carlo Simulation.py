import random
import numpy as np
import matplotlib.pyplot as plt
import time

def calculate_net_pnl(data_set, exit_values, starting_amount, bet_amount):
    pnl = {exit_value: starting_amount for exit_value in exit_values}

    for value in data_set:
        for exit_value in exit_values:
            if value >= exit_value:
                pnl[exit_value] += (exit_value - 1) * bet_amount  # Profit for winning round
            else:
                pnl[exit_value] -= bet_amount  # Loss for losing round

    return pnl

def run_simulation(data_set, exit_values, starting_amount, bet_amount, num_simulations, top_n=1, max_individual_results=5):
    total_rounds = len(data_set)
    results = []
    exit_level_profits = {exit_value: [] for exit_value in exit_values}

    start_time = time.time()  # Start timing the simulations

    for _ in range(num_simulations):
        cumulative_pnl = starting_amount
        for value in random.choices(data_set, k=total_rounds):
            if cumulative_pnl <= 0:
                break  # Player busted, end simulation for this trial
            if exit_values and value >= min(exit_values):
                exit_value_to_use = max([exit_value for exit_value in exit_values if value >= exit_value])
            else:
                exit_value_to_use = 1.0
            if value >= exit_value_to_use:
                cumulative_pnl += (exit_value_to_use - 1) * bet_amount
            else:
                cumulative_pnl -= bet_amount
            # Move the assignment inside the loop
            for exit_value in exit_values:
                if exit_value == exit_value_to_use:
                    exit_profits = exit_level_profits[exit_value_to_use]
                    exit_profits.append(cumulative_pnl - starting_amount)
                    exit_level_profits[exit_value_to_use] = exit_profits

        results.append(cumulative_pnl)

    end_time = time.time()  # End timing the simulations

    # Find the top N exit levels with the highest average profit
    sorted_exit_levels = sorted(exit_level_profits.items(), key=lambda x: sum(x[1]) / num_simulations, reverse=True)
    best_exit_levels = [exit_level[0] for exit_level in sorted_exit_levels[:top_n]]

    # Limit the number of individual results printed for each exit value
    for exit_value, profits in exit_level_profits.items():
        exit_level_profits[exit_value] = profits[:max_individual_results]

    return results, total_rounds, best_exit_levels, exit_level_profits, end_time - start_time


# Provided data set
data_set = [29, 3.42, 1.83, 1.30, 18.50, 1.50, 2.14, 1.07, 2.91, 1.1, 3.03, 1.20, 3.05, 12.94, 1.0, 1.1, 10, 1.99, 1.72, 1.41, 1.23, 1.64, 22.87, 8.41, 1.15, 99.80, 1.26, 6.68, 8.09, 2.40, 3.64, 20.87, 2.28, 1.8, 1.52, 1.82, 5.67, 1.00, 1.42, 1.86, 2.12, 5.34, 1.07, 1.25, 1.38, 1.53, 3.65, 1.27, 42.58, 7.57, 2.67, 10.33, 1.47, 1.0, 7, 2.011, 4.02, 1.72, 4.12, 6.37, 37.70, 1.09, 11.93, 1.36, 1.71, 1.57, 4.25, 2.45, 1.78, 4.98, 1.62, 8.62, 2.21, 1.20, 1.25, 2.05, 85.25, 1.10, 3.85]
main_levels = [1.1, 1.25, 1.5, 1.75, 2.0]  # Your main levels
starting_amount = 100
bet_amount = 1
num_simulations = 1000000
max_individual_results = 5  # Maximum number of individual results to print for each exit value

net_pnl = calculate_net_pnl(data_set, main_levels, starting_amount, bet_amount)
for exit_value, profit_loss in net_pnl.items():
    print(f"Exit value: {exit_value:.2f}x, Total PNL: ${profit_loss:.2f}, Net PNL: ${profit_loss - starting_amount:.2f}")

simulation_results, total_rounds, best_exit_levels, exit_level_profits, simulation_time = run_simulation(data_set, main_levels, starting_amount, bet_amount, num_simulations, top_n=3, max_individual_results=max_individual_results)

# Analyze results
average_profit = sum(simulation_results) / num_simulations
max_profit = max(simulation_results)
min_profit = min(simulation_results)
percentiles = np.percentile(simulation_results, [10, 25, 50, 75, 90])
std_dev = np.std(simulation_results)

print("\nMonte Carlo Simulation Results:")
print("Average Profit:", average_profit)
print("Maximum Profit:", max_profit)
print("Minimum Profit:", min_profit)
print("Profit at Percentiles:", percentiles)
print("Standard Deviation of Profits:", std_dev)
print("Total Simulations:", num_simulations)
print("Total Rounds:", total_rounds)
print("Best Exit Levels:", best_exit_levels)
print("Simulation Runtime:", simulation_time, "seconds")

# Additional Exit Levels Analysis
for exit_value, profits in exit_level_profits.items():
    avg_profit = np.mean(profits)
    std_dev_exit = np.std(profits)
    used_percentage = sum(1 for profit in profits if profit > 0) / len(profits) * 100
    print(f"\nExit Value: {exit_value:.2f}x")
    print(f"  Average Profit: {avg_profit:.2f}")
    print(f"  Standard Deviation of Profits: {std_dev_exit:.2f}")
    print(f"  Percentage of Simulations Where Used: {used_percentage:.2f}%")
    print("  Individual Results:")
    for profit in profits:
        print(f"    Profit: ${profit:.2f}")

