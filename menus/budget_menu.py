from Ledger import Ledger
from constants import INCOME, EXPENSES

ledger = Ledger()

def budget_menu():
    income = ledger.get_income()
    expenses = ledger.get_expenses_total()
    essential_expenses = ledger.get_essential_expenses_total()
    non_essential_expenses = ledger.get_non_essential_expenses_total()

    print(f"{INCOME}, £{income:.2f}")
    print(f"{EXPENSES}, £{expenses:.2f}")

    if expenses < income:
        print(f"You're are within your budget.")
    elif expenses == income:
        print("You have reached your budget.")
    else: 
        print("You have exceeded your budget")
    
    return None