from menus import main_menu

def main_loop():
    next_menu = None

    while next_menu is None:
        if next_menu is None:
            # Run the main menu
            # to get the next menu
            next_menu = main_menu()

        # If menu is a menu function
        if callable(next_menu):
            # Run menu
            # to get the next menu
            next_menu = next_menu()

main_loop()