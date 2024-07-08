actions = [
    {"name": "Action-1", "cost": 20, "profit": 5},  # Profit in % ( 2 years )
    {"name": "Action-2", "cost": 30, "profit": 10},
    {"name": "Action-3", "cost": 50, "profit": 15},
    {"name": "Action-4", "cost": 70, "profit": 20},
    {"name": "Action-5", "cost": 60, "profit": 17},
    {"name": "Action-6", "cost": 80, "profit": 25},
    {"name": "Action-7", "cost": 22, "profit": 7},
    {"name": "Action-8", "cost": 26, "profit": 11},
    {"name": "Action-9", "cost": 48, "profit": 13},
    {"name": "Action-10", "cost": 34, "profit": 27},
    {"name": "Action-11", "cost": 42, "profit": 17},
    {"name": "Action-12", "cost": 110, "profit": 9},
    {"name": "Action-13", "cost": 38, "profit": 23},
    {"name": "Action-14", "cost": 14, "profit": 1},
    {"name": "Action-15", "cost": 18, "profit": 3},
    {"name": "Action-16", "cost": 8, "profit": 8},
    {"name": "Action-17", "cost": 4, "profit": 12},
    {"name": "Action-18", "cost": 10, "profit": 14},
    {"name": "Action-19", "cost": 24, "profit": 21},
    {"name": "Action-20", "cost": 114, "profit": 18},
]

print(f'Actions sans real profit {actions}')

# Calculer le bénéfice réel pour chaque action
for action in actions:
    action['real_profit'] = action['cost'] * (action['profit'] / 100)

print(f'Actions avec real profit {actions}')

# Initialiser les variables
max_budget = 500
len_actions = len(actions)

# Initialiser le tableau pour la programmation dynamique avec des valeurs à 0 par default
# dp = Tableau 2D : [[x, x], [x, x]]
# (len_actions + 1) lignes et (max_budget + 1) colonnes.
dp = [[0 for i in range(max_budget + 1)] for j in range(len_actions + 1)]
print(f'Empty dp {dp}')

# Algorithme de sac à dos
for i in range(1, len_actions + 1):     # boucle sur la taille des actions
    for budget in range(max_budget + 1):     # boucle sur toutes les valeurs possible de max_budget ( ici 0 - 500 )
        if actions[i - 1]['cost'] <= budget:     # vérifie que le coût de l'action actuelle est inférieur ou egal au budget
            dp[i][budget] = max(dp[i - 1][budget], dp[i - 1][budget - actions[i - 1]['cost']] + actions[i - 1]['real_profit'])  # on compare : le max du (profit maximum réalisable sans prendre l'action & profit maximum réalisable en prenant l'action)
        else:
            dp[i][budget] = dp[i - 1][budget]

# Trouver les actions sélectionnées
selected_actions = []
for i in range(len_actions, 0, -1):  # Parcourt les actions en ordre inverse pour déterminer quelles actions ont été sélectionnées.
    if dp[i][max_budget] != dp[i - 1][max_budget]:  # cela signifie que l'action i a été incluse dans la solution optimale
        selected_actions.append(actions[i - 1])     # ajoute l'aciton dans la liste
        max_budget -= actions[i - 1]['cost']        # Retire le coût de l'action du budget

selected_actions.reverse()  # Pour avoir les actions dans l'ordre initial

# Afficher les résultats
total_cost = sum(action['cost'] for action in selected_actions)
total_profit = sum(action['real_profit'] for action in selected_actions)
result = {
    "actions": selected_actions,
    "total_cost": total_cost,
    "total_profit": total_profit
}

for action in result['actions']:
    print(
        f' Action : {action['name']}\n'
        f' Price : {action['cost']}\n'
        f' Profit : {action['profit']}\n'
        f' Real profit : {action['real_profit']}\n'
    )

print(
    f' Total Cost : {result['total_cost']}\n'
    f' Total Real Profit : {result['total_profit']}\n'
)
