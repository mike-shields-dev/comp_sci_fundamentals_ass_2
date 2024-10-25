from simple_term_menu import TerminalMenu

# Import the Finances (singleton) instance.
from ledger import ledger
from Expense.Expense import Expense

def expenses_menu():
    expense = Expense()
    
    while expense.get_amount() == 0.0:
        while expense.get_amount() == 0.0:
            PROMPT = "Please enter an expense amount"
            try:
                user_input = float(input(PROMPT))
                if finances.is_valid_amount(user_input):
                    expense_amount = user_input

            except ValueError as e: 
                print(str(e))       
    
    if expense_amount == 0.0:
        return expenses_menu

    category = None

    while category is None:
        menu = TerminalMenu(
            categories = finances.get_expense_categories(),
            cycle_cursor = True,
            title="Please choose an expense category"
        )

        selected_index = menu.show()
        category = category[selected_index]

    finances.append_expense({
        category,
        expense_amount
    })
      