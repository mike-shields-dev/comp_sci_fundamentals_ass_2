# Import the constants that store the main menu's 
# sub menu option names (magic strings)
from constants import (
    INCOME_MENU,
    BUDGET_MENU, 
    EXPENSE_MENU,
    EXIT_MENU
)

from simple_term_menu import TerminalMenu

# Import all of the sub menus functions
from menus.budget_menu import budget_menu
from menus.exit_menu import exit_menu
from menus.expenses_menu.expenses_menu import expenses_menu
from menus.income_menu import income_menu


from utilities.clear_screen import clear_screen

"""
Create sub menu dictionary
key = sub menu option name
value = sub menu function
"""
sub_menus = {
    INCOME_MENU: income_menu,
    EXPENSE_MENU: expenses_menu,
    BUDGET_MENU: budget_menu,
    EXIT_MENU: exit_menu,
}

def main_menu():
    
    clear_screen()

    selected_sub_menu = None
    options = list(sub_menus.keys())
    
    main_menu = TerminalMenu(
        sub_menus.keys(), 
        cycle_cursor=True,
        title= "=================\n  Main Menu\n================="
    )
    
    selected_index = main_menu.show()
    
    if type(selected_index) is int:
        selected_sub_menu = sub_menus[options[selected_index]]
    else:
        selected_sub_menu = None

    return selected_sub_menu
