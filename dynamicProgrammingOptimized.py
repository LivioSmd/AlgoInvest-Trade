#KnapSack algo
import Tools

max_budget = 50000  # Multiply budget by 100
file_path = './datas/dataset1_Python.csv'
separator = ','
actions = Tools.getAction(file_path, separator)
len_actions = len(actions)

# Calculate the real profit for each action
for action in actions:
    action['real_profit'] = action['cost'] * (action['profit'] / 10000)  # (profit / 100), cost already multiplied by 100

print(f'Actions avec real profit {actions}\n')

# Initialize array for dynamic programming with default values of 0
# dp = array 2D : [[x, x], [x, x]]
# (len_actions + 1) lines & (max_budget + 1) columns.
dp = [[0 for i in range(max_budget + 1)] for j in range(len_actions + 1)]

# KnapSack algo
for i in range(1, len_actions + 1):     # loop on actions size
    for budget in range(max_budget + 1):     # loop over all possible max_budget values
        if 0 < actions[i - 1]['cost'] <= budget:     # Checks if the cost of the current action > 0 & =< the budget
            # we compare: the max of (maximum profit without taking the action & maximum profit by taking the action)
            dp[i][budget] = max(dp[i - 1][budget], dp[i - 1][budget - actions[i - 1]['cost']] + actions[i - 1]['real_profit'])
        else:
            dp[i][budget] = dp[i - 1][budget]

# Find selected actions
selected_actions = []
remaining_budget = max_budget
for i in range(len_actions, 0, -1):  # Scrolls through the actions in reverse order to determine which actions have been selected.
    if dp[i][remaining_budget] != dp[i - 1][remaining_budget]:  # this means that action i has been included in the optimal solution
        selected_actions.append(actions[i - 1])     # adds the action to the list
        remaining_budget -= actions[i - 1]['cost']  # Remove the cost of the action from the budget

selected_actions.reverse()  # To have the actions in their original order

Tools.displayResults(selected_actions)  # Display results
