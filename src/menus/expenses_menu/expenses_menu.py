from typing import Callable
from Expense.Expense import Expense
from Ledger.ledger import ledger

from utilities.clear_screen import clear_screen

from .prompt_expense_amount import prompt_expense_amount
from .prompt_expense_category import prompt_expense_category
from .prompt_expense_title import prompt_expense_title

def expenses_menu() -> Callable | None:
    
    clear_screen()

    amount = None
    category = None
    title = None

    while amount is None:
        try: 
            amount = prompt_expense_amount()

        except Exception as e:
            amount = None
            print(str(e))
            print("Please try again.\n")

    while category is None:
        try: 
            category = prompt_expense_category()

        except Exception as e:
            category = None
            print(str(e))
            print("Please try again.\n")


    while title is None:
        try: 
            title = prompt_expense_title()

        except Exception as e:
            title = None
            print(str(e))
            print("Please try again.\n")

    ledger.append_expense(Expense(amount, category, title))