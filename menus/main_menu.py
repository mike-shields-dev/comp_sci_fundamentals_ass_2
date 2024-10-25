from simple_term_menu import TerminalMenu

# Import the option names for the main menu
from constants import (
    INCOME_MENU,
    BUDGET_MENU, 
    EXPENSE_MENU,
    EXIT_MENU
)

from menus.budget_menu import budget_menu
from menus.exit_menu import exit_menu
from menus.expenses_menu import expenses_menu
from menus.income_menu import income_menu

"""
    Create a dictionary where:
    key = main menu option
    value = sub menu function
"""
sub_menus = {
    INCOME_MENU: income_menu,
    EXPENSE_MENU: expenses_menu,
    BUDGET_MENU: budget_menu,
    EXIT_MENU: exit_menu,
}

def main_menu():
    selected_sub_menu = None
    options = list(sub_menus.keys())
    
    main_menu = TerminalMenu(
        sub_menus.keys(), 
        cycle_cursor=True, 
        title="--Main Menu--"
    )
    
    selected_index = main_menu.show()
    
    if type(selected_index) is int:
        selected_sub_menu = sub_menus[options[selected_index]]
    else:
        selected_sub_menu = None

    return selected_sub_menu
