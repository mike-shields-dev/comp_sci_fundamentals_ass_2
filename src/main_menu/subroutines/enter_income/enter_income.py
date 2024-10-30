# Import the Ledger instance (singleton).
from Ledger.ledger import ledger

from utilities.clear_screen import clear_screen

def enter_income():
    # Declare income variable to control 
    # while loop continuation
    income = None

    # Loop while income is None
    while income is None:        
        try:
            # Get the user's income
            income = float(input("Please enter your income: "))
            # Store the user's income in the ledger
            ledger.set_income(income)
        
        except ValueError as e:
            clear_screen()
            # Display the error message to the user
            print(str(e))        

            # Reset income to none to continue
            # while loop iteration
            income = None