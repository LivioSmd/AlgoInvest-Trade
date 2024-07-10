# KnapSack algo
import itertools
import Tools

max_budget = 500
file_path = './datas/brute_force_actions.csv'

actions = Tools.getAction(file_path)
for action in actions:
    action['real_profit'] = action['cost'] * (action['profit'] / 100)

# Générer toutes les combinaisons possibles et trouver la meilleure
best_combination = []
best_profit = 0

for r in range(1, len(actions) + 1):
    for combination in itertools.combinations(actions, r):
        total_cost = sum(action['cost'] for action in combination)
        total_profit = sum(action['real_profit'] for action in combination)

        if total_cost <= max_budget and total_profit > best_profit:
            best_combination = combination
            best_profit = total_profit

Tools.displayResults(best_combination)
