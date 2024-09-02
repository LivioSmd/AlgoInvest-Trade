# KnapSack algo
import Tools

max_budget = 500
file_path = './datas/dataset1_Python.csv'
separator = ','

# Retrieve actions with Tools method & Calculate the real profit for each action
actions_table = Tools.getAction(file_path, separator)
for action in actions_table:
    action['real_profit'] = action['cost'] * (action['profit'] / 100)


def main_method_greedy_algo(actions, budget_max=500):

    sorted_actions = sorted(
        [action for action in actions if action['cost'] > 0],  # Ignore actions with cost 0
        key=lambda x: x['real_profit'] / x['cost'],
        reverse=True
    )

    selected_actions = []
    total_cost = 0.0

    for action in sorted_actions:
        if total_cost + action['cost'] <= budget_max:
            selected_actions.append(action)
            total_cost += action['cost']

    return selected_actions


actions_list = main_method_greedy_algo(actions_table, max_budget)
Tools.displayResults(actions_list)
