from constants import ADD_EXPENSE, REMOVE_EXPENSE
from simple_term_menu import TerminalMenu

from utilities.clear_screen import clear_screen
from .subroutines import add_expense, remove_expense

menu_option_subroutines = {
    ADD_EXPENSE: add_expense,
    REMOVE_EXPENSE: remove_expense,
}

def manage_expenses_menu() -> None:
    options = list(menu_option_subroutines.keys())
    
    while True:
        clear_screen()

        menu = TerminalMenu(            
            options, 
            cycle_cursor=True,
            title = (
                    "=========================\n"    
                +   "MANAGE EXPENSES\n"  
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
            menu_option_subroutines[
                options[selected_menu_option_index]
            ]
        )

        # Invoke the subroutine associated with the 
        # chosen menu option
        menu_option_subroutine()



        
