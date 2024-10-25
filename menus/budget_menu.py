from Finances.Finances import Finances, INCOME, EXPENSES

finances = Finances()

def budget_menu():
    income = finances.get_income()
    expenses = finances.get_expenses_total()
    essential_expenses = finances.get_essential_expenses_total()
    non_essential_expenses = finances.get_non_essential_expenses_total()

    print(f"{INCOME}, £{income:.2f}")
    print(f"{EXPENSES}, £{expenses:.2f}")

    if expenses < income:
        print(f"You're are within your budget.")
    elif expenses == income:
        print("You have reached your budget.")
    else: 
        print("You have exceeded your budget")
    
    return None