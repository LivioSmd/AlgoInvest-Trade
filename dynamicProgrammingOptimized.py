#KnapSack algo
import Tools

max_budget = 500
file_path = './datas/dataset2_Python.csv'
separator = ','
actions = Tools.getAction(file_path, separator)
len_actions = len(actions)

# Calculer le bénéfice réel pour chaque action
for action in actions:
    action['real_profit'] = action['cost'] * (action['profit'] / 100)

print(f'Actions avec real profit {actions}\n')

# Initialiser le tableau pour la programmation dynamique avec des valeurs à 0 par default
# dp = Tableau 2D : [[x, x], [x, x]]
# (len_actions + 1) lignes et (max_budget + 1) colonnes.
dp = [[0 for i in range(max_budget + 1)] for j in range(len_actions + 1)]

# Algorithme de sac à dos
for i in range(1, len_actions + 1):     # boucle sur la taille des actions
    for budget in range(max_budget + 1):     # boucle sur toutes les valeurs possible de max_budget ( ici 0 - 500 )
        if 0 < actions[i - 1]['cost'] <= budget:     # vérifie que le coût de l'action actuelle supérieur à 0 et est inférieur ou egal au budget
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

Tools.displayResults(selected_actions)  # Afficher les resultats

#   résolution : programmation dynamique (celui la), précis
#   résolution : algo glouton (aller voir), solution approchée
#   Tester les fichiers
#   Verifier les données qui n'ont pas de sens