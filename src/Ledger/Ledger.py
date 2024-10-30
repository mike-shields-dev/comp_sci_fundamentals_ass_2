from typing import List
from src.Expense.Expense import Expense
from src.constants import INCOME, EXPENSES, ESSENTIAL, NON_ESSENTIAL, TITLE
from src.utilities.is_non_empty_string import is_non_empty_string
from src.utilities.is_positive_number import is_positive_number

class Ledger:
    """ 
    A class to manage a financial ledger, storing income and categorised expenses.

    Attributes:
        __state (dict): A dictionary containing income and categorised expenses.
    """
    def __init__(self):
        """
        Initialises a new ledgers instance with an income of 0.0 
        and categorized expense lists for essential and non-essential expenses.
        """
        self.__state = {
            INCOME: 0.0,
            EXPENSES: {
                ESSENTIAL: [],
                NON_ESSENTIAL: [],
            }
        }

    def get_state(self) -> dict:
        """
        Retrieves a copy of the ledgers' internal state.

        Returns: 
            dict: A copy of the ledgers' internal state.
        """
        return self.__state.copy()

    def get_income(self) -> float:
        """
        Retrieves the current income.

        Returns:
            float: The amount of income.
        """
        return self.__state[INCOME]

    def set_income(self, amount: float | int) -> None:
        """
        Sets the income to the provided amount.

        Args: 
            amount (float | int): The income amount (must be greater than 0.0).
        
        Raises: 
            ValueError: If `amount` is not a positive number.
        """
        if is_positive_number(amount):
            self.__state[INCOME] = amount
        else:
            raise ValueError(
                "Error: income must be a number greater than 0.0."
            )

    def get_expense_categories(self) -> List[str]:
        """
        Retrieves the list of expense categories.

        Returns:
            list: A list of expense categories.
        """
        return list(self.__state[EXPENSES].keys())
        

    def append_expense(self, expense: Expense) -> None:
        """
        Adds an expense to the specified category within the ledgers expenses.

        Args: 
            expense (Expense): An instance of the Expense class.

        Raises: 
            TypeError: If `expense` is not an instance of Expense.
            ValueError: If the expense's amount is not positive, 
                        the category is invalid, or the title is empty.
        """
        if not isinstance(expense, Expense):
            raise TypeError(
                "Error: Cannot add expense, it must be of type 'Expense'."
            )
        
        if not is_positive_number(expense.get_amount()):
            raise ValueError(
                "Error: Cannot add expense, its amount must be a number greater than 0.0."
            )
        
        if not self.is_valid_expense_category(expense.get_category()):
            raise ValueError(
                "Error: Cannot add expense, its category is not a valid expense category"
            )
        
        if not is_non_empty_string(expense.get_title()):
            raise ValueError(
                "Error: Cannot add expense, its title is not a valid expense category"
            )
        
        self.__state[EXPENSES][expense.get_category()].append(expense)

    def get_all_expenses(self) -> List[Expense]:
        """
        Returns a list of all of the expenses in all expense categories.
        """
        all_expenses = []
        for category in self.__state[EXPENSES].values():
            all_expenses.extend(category)
        
        return all_expenses
    
    def get_expenses_by_category(self, *categories: str) -> List[str]:
        """
        Returns a list of the expenses stored in the ledger's expenses 
        dictionary under the properties that match the provided
        category.

        Args:
            categories (str): One or more expense categories.
        
        Returns: 
            list: 
                A list of any expenses found in the ledger's expenses 
                dictionary under the properties that match the provided 
                categories.
        """ 
        expenses = []
        
        # set function is used to remove possible duplicate categories          
        for expense_category in self.get_expense_categories():  
            if expense_category in categories:
                # Assuming get_expenses_by_category is a method that returns expenses by category
                expenses.extend(self.__state[EXPENSES][expense_category])  

        return expenses
                
    def is_valid_expense_category(self, category: str) -> bool:
        """
        Checks if a given category exists in the ledgers' expenses.

        Args:
            category (str): The category to validate.

        Returns: 
            bool: True if the category is valid, False otherwise.
        """
        return category in self.__state[EXPENSES]
    

    def is_unique_expense_title(self, title) -> bool:
        """
        Checks that the provided expense title has
        not already been allocated to an expense 
        in all the expense category lists.
        """
        
        for expense in self.get_all_expenses():
            if expense.get_title() == title:
                return False
        
        return True
