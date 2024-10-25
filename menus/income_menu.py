# Import the Finances (singleton) instance.
from ledger import ledger

def income_menu():
    while ledger.get_income() == 0.0:
        try:
            PROMPT = "Please enter your income: "
            ledger.set_income(float(input(PROMPT)))
        
        except ValueError as e:
            print(str(e))        
        
    if ledger.get_income() == 0.0:
        return income_menu