import pandas as pd


def getAction(file_path, separator):
    data = pd.read_csv(file_path, sep=separator)  # Read CSV file
    actions = []  # Empty table containing all actions

    # Retrieve column contents
    print(data.head())
    name_field = data['name']
    price_field = data['price']
    profit_field = data['profit']

    len_actions = len(name_field)
    for i in range(0, len_actions):
        actions.append({
            "name": name_field.get(i),
            "cost": int(float(price_field.get(i)) * 100),  # Multiply cost by 100
            "profit": int(float(profit_field.get(i)) * 100)  # Multiply profit by 100
        })

    print('\nTable of Actions :')
    print(f'{actions}\n')

    return actions


def displayResults(selected_actions):   # Show results
    actions_names_list = []

    total_cost = sum(action['cost'] for action in selected_actions) / 100  # Divide by 100 to display
    total_profit = sum(action['real_profit'] for action in selected_actions) / 100  # Divide by 100 to display

    print("Selected Actions:")
    for action in selected_actions:
        actions_names_list.append(action['name'])
        print(
            f"Action: {action['name']}\n"
            f"Price: {action['cost'] / 100}\n"  # Divide by 100 to display
            f"Profit: {action['profit'] / 100}\n"  # Divide by 100 to display
            f"Real profit: {action['real_profit'] / 100}\n"  # Divide by 100 to display
        )

    print(f"Actions Name List :")
    for name in actions_names_list:
        print(name)

    print(
        f"\nTotal Cost: {total_cost}\n"
        f"Total Real Profit: {total_profit}\n"
    )
