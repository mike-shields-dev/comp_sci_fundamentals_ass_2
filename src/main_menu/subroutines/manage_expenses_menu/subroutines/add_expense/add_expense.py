from Ledger.ledger import ledger
from Expense import Expense
from utilities.clear_screen import clear_screen
from .prompts import prompt_expense_amount
from .prompts import prompt_expense_category
from .prompts import prompt_expense_title
from utilities.is_positive_number import is_positive_number
from utilities.is_non_empty_string import is_non_empty_string

def add_expense():
    """
    Prompts the user to enter: 
        amount: The expense's amount
        category: The expense's category
        title: The expense's title

    If all provided inputs are valid, 
    a new expense is appended to the the
    ledger's expenses under the appropriate category
    """
    # Create a new expense instance to be added to the 
    # ledgers expenses
    new_expense = Expense()

    while new_expense.get_amount() is None:
        try: 
            # prompt the user for the expense's amount
            new_expense.set_amount(prompt_expense_amount())
        
        except Exception as e:
            clear_screen()
            
            # Print the error message
            print(str(e))

    while new_expense.get_category() is None:
        try:
            new_expense.set_category(prompt_expense_category())
        
        except Exception as e:
            clear_screen()

            # Print the error message
            print(str(e))

    while new_expense.get_title() is None:
        try: 
            title = prompt_expense_title()          
            
            # Validate that the provided expense title is unique
            if not ledger.is_unique_expense_title(title):
                raise ValueError(
                    f"Error: An expense with title \"{title}\" already exists\n"
                )
            
            new_expense.set_title(title)
            
        except Exception as e:
            clear_screen()
            
            # Print the error message in the raised ValueError
            print(str(e))


    ledger.append_expense(new_expense)