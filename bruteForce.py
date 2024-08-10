# KnapSack algo
import itertools
import Tools

max_budget = 50000
file_path = './datas/brute_force_actions.csv'

separator = ";"
actions = Tools.getAction(file_path, separator)
for action in actions:
    action['real_profit'] = action['cost'] * (action['profit'] / 10000)

# Generate all possible combinations and find the best one
best_combination = []
best_profit = 0

for i in range(1, len(actions) + 1):
    for combination in itertools.combinations(actions, i):
        total_cost = sum(action['cost'] for action in combination)
        total_profit = sum(action['real_profit'] for action in combination)

        #   Checks if the total cost of the current combination =< the maximum budget.
        #   Checks if the total profit of the current combination > the best profit found for now.
        if total_cost <= max_budget and total_profit > best_profit:
            best_combination = combination
            best_profit = total_profit

Tools.displayResults(best_combination)
