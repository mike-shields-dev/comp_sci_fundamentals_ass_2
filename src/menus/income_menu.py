# Import the Ledger instance (singleton).
from Ledger.ledger import ledger

from utilities.clear_screen import clear_screen

def income_menu():
    
    clear_screen()
    
    income = None

    while income is None:
        try:
            income = float(input("Please enter your income: "))
            ledger.set_income(income)
        
        except ValueError as e:
            income = None
            print(str(e))        
        
    if ledger.get_income() == 0.0:
        return income_menu