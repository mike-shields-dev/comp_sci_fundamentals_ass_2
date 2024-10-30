from simple_term_menu import TerminalMenu
from Ledger.ledger import ledger
from utilities.clear_screen.clear_screen import clear_screen
from utilities.is_positive_number import is_positive_number
from Expense import Expense

def prompt_expense_amount() -> float | None:
    """
    Prompts the user for an expense amount.

    Raises: 
        ValueError: 
            If the provided expense amount
            fails validation according to 
            the `is_positive_number` utility function.
    """
    expense_amount = None
    
    while expense_amount == None:
        expense_amount = float(input("Please enter an expense amount: "))


    return expense_amount

def prompt_expense_category() -> str | None:
    category = None
    options = ledger.get_expense_categories()

    while category is None:
        # Create a terminal menu interface
        menu = TerminalMenu(
            options,
            cycle_cursor = True,
            title="Please choose an expense category"
        )

        # Access the index of the user's selected option
        selected_index = menu.show()
        # Use the selected_index to access the category
        # that the user selected
        category = options[selected_index]

    # return the category
    return category


def prompt_expense_title() -> str | None:
    expense_title = None

    while expense_title is None:
        try:
            expense_title = input("Enter a title for the expense: ")
            
        except ValueError as e:
            expense_title = None
            print(str(e))


    return expense_title