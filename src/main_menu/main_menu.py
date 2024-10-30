# Import the constants that store the main menu's 
# sub menu option names (magic strings)
from constants import (
    ENTER_INCOME,
    VIEW_BUDGET,
    MANAGE_EXPENSES,
    EXIT_MENU
)
from simple_term_menu import TerminalMenu
from utilities.clear_screen import clear_screen

# Import all of the main menu option subroutines
from .subroutines.view_budget import view_budget
from .subroutines.exit_program_menu import exit_program_menu
from .subroutines.manage_expenses_menu import manage_expenses_menu
from .subroutines.enter_income import enter_income

"""
Menu option subroutines dictionary
    key: menu option name
    value: menu option subroutine
"""
menu_option_functions = {
    ENTER_INCOME: enter_income,
    MANAGE_EXPENSES: manage_expenses_menu,
    VIEW_BUDGET: view_budget,
    EXIT_MENU: exit_program_menu,
}

def main_menu():
    """Main Menu

    Continuously prompts the user to select a menu option and
    invokes the selected menu option's subroutine.
    """
    # Determine the list of available
    options = list(menu_option_functions.keys())
    
    while True:
        # Create a terminal menu instance
        menu = TerminalMenu(
            options, # Provide a list of menu options
            cycle_cursor=True,
            title= (
                    "MAIN MENU\n"  
                +   "=========================\n"  
                +   "Please choose an option: \n"  
                +   "-------------------------"
            )
        )

        # Access the index of the menu option the user has selected
        selected_menu_option_index = menu.show()
                
        # Use the selected menu option index to access the 
        # subroutine associated with the selected menu option
        menu_option_subroutine = (
            menu_option_functions[
                options[selected_menu_option_index]
            ]
        )

        # Invoke the subroutine associated with the 
        # chosen menu option
        menu_option_subroutine()
