from menus import main_menu

menu = None

while menu is None:
    if menu is None:
        # Run the main menu
        # to get the next menu
        menu = main_menu()

    # If menu is a menu function
    if callable(menu):
        # Run menu
        # to get the next menu
        menu = menu()
