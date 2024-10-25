from typing import List
from Expense.Expense import Expense
from constants import INCOME, EXPENSES, ESSENTIAL, NON_ESSENTIAL
from utilities.is_non_empty_str.is_non_empty_str import is_non_empty_str
from utilities.is_positive_number.is_positive_number import is_positive_number

class Finances:
    """ 
    A class to manage a financial ledger, storing income and categorized expenses.

    Attributes:
        __state (dict): A dictionary containing income and categorized expenses.
    """
    def __init__(self):
        """
        Initializes a new Finances instance with an income of 0.0 
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
        Retrieves a copy of the finances' internal state.

        Returns: 
            dict: A copy of the finances' internal state.
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
                "Error: Cannot set the finances' income. The provided income must be a positive number greater than 0.0."
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
        Adds an expense to the specified category within the finances.

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
        
        if not is_positive_number(expense.amount):
            raise ValueError(
                "Error: The expense amount must be a positive number greater than 0.0."
            )
        
        if not self.is_valid_expense_category(expense.category):
            raise ValueError(
                f"Error: The expense category must be one of: {self.get_expense_categories()}."
            )
        
        if not is_non_empty_str(expense.title):
            raise ValueError(
                "Error: The expense title must be a non-empty string."
            )
        
        self.__state[EXPENSES][expense.category].append(expense)

    def get_sum_expenses_by_categories(self, *categories: str) -> float:
        """
        Calculates the sum of expenses for the specified categories.

        Args:
            categories (str): One or more category names to sum expenses for.
        
        Raises:
            TypeError: If any category is not a string.
            ValueError: If any category is invalid or none are provided.
        
        Returns: 
            float: The total sum of expenses for the specified categories.
        """
        if len(categories) == 0:
            raise ValueError(
                "Error: At least one category must be provided."
            )

        total = 0.0
        for category in categories:
            if not isinstance(category, str):
                raise TypeError(
                    "Error: The provided categories must be non-empty strings."
                )

            if category not in self.get_expense_categories():
                raise ValueError(
                    f"Error: No expenses for the provided category: \"{category}\" were found."
                )
            
            total += sum(exp.amount for exp in self.__state[EXPENSES][category])

        return total
                
    def is_valid_expense_category(self, category: str) -> bool:
        """
        Checks if a given category exists in the finances' expenses.

        Args:
            category (str): The category to validate.

        Returns: 
            bool: True if the category is valid, False otherwise.
        """
        return category in self.__state[EXPENSES]
