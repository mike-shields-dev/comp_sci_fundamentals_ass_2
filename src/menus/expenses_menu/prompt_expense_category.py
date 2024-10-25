from simple_term_menu import TerminalMenu
from Ledger.ledger import ledger

def prompt_expense_category() -> str | None:
    category = None
    options = ledger.get_expense_categories()

    while category is None:
        menu = TerminalMenu(
            options,
            cycle_cursor = True,
            title="Please choose an expense category"
        )

        selected_index = menu.show()
        category = options[selected_index]

    print("category", category)
    return category