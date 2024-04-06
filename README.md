# Number-Analysis-Basic-Complex #


This script performs a Monte Carlo simulation to analyze the profit and loss outcomes of a trading "Crash" strategy based on provided data sets and exit levels. It provides insights into the potential profitability and risk associated with different exit strategies.

Just add a Historical Crash dataset of your choosing & timeframe and adjust the number of simulations to run. Default is set to 1000000. Input your starting capitol parameter to produce PNL outcomes. Target levels and max results can also be adjusted.


Function Definitions:

calculate_net_pnl: Calculates the net profit and loss (PNL) based on provided data sets and exit values.
run_simulation: Runs a Monte Carlo simulation to analyze the profit and loss under different scenarios.



Data Set and Parameters:

A provided data set, data_set, contains values representing performance outcomes.
main_levels represent exit levels for profit-taking.
starting_amount, bet_amount, and num_simulations are parameters for the simulation.



Calculating Net PNL:

The script calculates the net profit and loss (net_pnl) for each exit value provided in main_levels.



Running Simulations:

The script runs a Monte Carlo simulation using the run_simulation function.
It generates multiple simulations to analyze profit and loss outcomes under different conditions.



Analyzing Simulation Results:

The script prints various statistics derived from the simulation results, including average profit, maximum profit, minimum profit, percentiles, and standard deviation of profits.

It also analyzes additional exit levels, printing average profit, standard deviation of profits, percentage of simulations where used, and individual results.



