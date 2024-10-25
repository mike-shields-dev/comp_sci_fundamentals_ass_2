from constants import ESSENTIAL, NON_ESSENTIAL

# Import the Ledger instance (singleton).
from Ledger.ledger import ledger

# Import the clear screen function
from utilities.clear_screen import clear_screen

# Import the constants storing magic strings.
from constants import INCOME, EXPENSES

def budget_menu():
    
    clear_screen()

    income = ledger.get_income()
    expenses = ledger.get_sum_expenses_by_categories(ESSENTIAL, NON_ESSENTIAL)
    essential_expenses = ledger.get_sum_expenses_by_categories(ESSENTIAL)
    non_essential_expenses = ledger.get_sum_expenses_by_categories(NON_ESSENTIAL)

    print(f"{INCOME}, £{income:.2f}")
    print(f"{EXPENSES}, £{expenses:.2f}")

    if expenses < income:
        print(f"You're are within your budget.")
    elif expenses == income:
        print("You have reached your budget.")
    else: 
        print("You have exceeded your budget")
        
    print("\nHit the Enter key to return to the main menu")

    input()

    return None