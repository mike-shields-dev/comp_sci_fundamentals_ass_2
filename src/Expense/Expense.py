from utilities.is_positive_number import is_positive_number
from utilities.is_non_empty_string import is_non_empty_string

from constants import AMOUNT, CATEGORY, TITLE

class Expense:
    """
    A class that represents a monetary expense.

    Attributes: 
        amount (float | int): The amount of the expense.
        category (str): The category of the expense, e.g., "Essential" or "Non Essential".
        title (str): The title of the expense.
    """
    def __init__(
            self, 
            amount: float | int = None,
            category: str = None, 
            title: str = None
        ):
        """
        Initializes a new Expense instance with specified attributes.

        Args:
            amount (float | int): The amount of the expense.
            category (str): The category of the expense.
            title (str): The title of the expense.
        """
        self.__state = {
            AMOUNT: amount,
            CATEGORY: category,
            TITLE: title,
        }


    def get_state(self) -> dict:
        """
        Retrieves a copy of the expense's internal state.

        Returns: 
            dict: A dictionary containing the expense's state.
        """
        return self.__state.copy()

    
    def set_amount(self, amount: float | int) -> None:
        """
        Sets the amount of the expense.

        Args: 
            amount (float | int): The expense's amount.

        Raises: 
            ValueError: If `amount` is not a positive number.
        """
        if not is_positive_number(amount):
            raise ValueError(
                "Error: The expense's amount can only be set to a number greater than 0.0"
            )

        self.__state[AMOUNT] = float(amount)

    
    def get_amount(self) -> float | None:
        """
        Retrieves the amount of the expense.

        Returns: 
            float: The amount of the expense.
        """
        return self.__state[AMOUNT]


    def set_category(self, category: str) -> None:
        """
        Sets the category of the expense.

        Args: 
            category (str): The category of the expense.

        Raises:
            ValueError: If `category` is not a non-empty string.
        """
        if not is_non_empty_string(category):
            raise ValueError(
                "Error: The expense's category must be a non-empty string."
            )
        
        self.__state[CATEGORY] = category
        

    def get_category(self) -> str | None:
        """
        Retrieves the category of the expense.

        Returns: 
            str: The category of the expense.
        """
        return self.__state[CATEGORY]
    

    def set_title(self, title: str) -> None:
        """
        Sets the title of the expense.

        Args:
            title (str): The title of the expense.

        Raises: 
            ValueError: If `title` is not a non-empty string.
        """
        if not is_non_empty_string(title):
            raise ValueError(
                "Error: The expense's title must be a non-empty string."
            )    
        
        self.__state[TITLE] = title
    

    def get_title(self) -> str | None:
        """
        Retrieves the title of the expense.

        Returns: 
            str: The title of the expense.
        """
        return self.__state[TITLE]