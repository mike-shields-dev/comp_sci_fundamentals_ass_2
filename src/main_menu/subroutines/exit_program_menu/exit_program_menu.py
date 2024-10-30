from utilities.clear_screen import clear_screen

from simple_term_menu import TerminalMenu

import sys

def exit_program_menu():
    should_exit = None
    
    while should_exit is None:
        menu = TerminalMenu(
            ["Resume", "Exit"], 
            cycle_cursor=True, 
            title="Are you sure you want to quit?"
        )

        should_exit = bool(menu.show())

    if should_exit:
        print("Thank you for using Personal Finance Calculator!")
        sys.exit()