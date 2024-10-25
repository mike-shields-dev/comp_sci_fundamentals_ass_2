from simple_term_menu import TerminalMenu
from Ledger.ledger import ledger
from utilities.is_non_empty_string import is_non_empty_string

def prompt_expense_title() -> str | None:
    expense_title = None

    while expense_title is None:
        try:
            expense_title = input("Enter a title for the expense: ")
        except ValueError as e:
            expense_title = None
            print(str(e))


    return expense_title