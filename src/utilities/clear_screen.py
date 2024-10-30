import os

def clear_screen() -> None:
    """
    A utility function that clears the console
    remove any previous output.
    """
    os.system("cls" if os.name == "nt" else "clear")