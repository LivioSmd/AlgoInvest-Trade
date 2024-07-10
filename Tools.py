import pandas as pd


def getAction(file_path):
    data = pd.read_csv(file_path, sep=';')  # Lire le fichier CSV
    actions = []  # Tableau vide qui contiendra l'ensemble des actions

    # Récupérer le contenu des colonnes
    name_field = data['name']
    price_field = data['price']
    profit_field = data['profit']

    len_actions = len(name_field)

    for i in range(0, len_actions):
        actions.append({"name": name_field.get(i), "cost": int(price_field.get(i)), "profit": int(profit_field.get(i))})

    print('\nTable of Actions :')
    print(f'{actions}\n')

    return actions


def displayResults(selected_actions):   # Afficher les résultats
    total_cost = sum(action['cost'] for action in selected_actions)
    total_profit = sum(action['real_profit'] for action in selected_actions)

    print("Selected Actions:")
    for action in selected_actions:
        print(
            f"Action: {action['name']}\n"
            f"Price: {action['cost']}\n"
            f"Profit: {action['profit']}\n"
            f"Real profit: {action['real_profit']}\n"
        )

    print(
        f"Total Cost: {total_cost}\n"
        f"Total Real Profit: {total_profit}\n"
    )

