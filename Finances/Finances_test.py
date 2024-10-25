import coverage
import unittest
from Finances import Finances
from constants import (
    INCOME, 
    EXPENSES, 
    ESSENTIAL, 
    NON_ESSENTIAL
)

class TestFinancesState(unittest.TestCase):
    """Unit tests for Finances class's state management methods."""    
    def setUp(self):
        """Sets up a Finances instance for each test."""
        self.finances = Finances()

    def test_get_state(self):
        """Tests that `Finances.get_state` returns a copy of the current state."""
        expected_state = {
            INCOME: 0.0,
            EXPENSES: {
                ESSENTIAL: [],
                NON_ESSENTIAL: [],
            }
        }
        self.assertEqual(self.finances.get_state(), expected_state)

  
class TestFinancesIncome(unittest.TestCase):
    """Unit tests for methods related to the income attribute in Finances."""    
    def setUp(self):
        """Sets up a Finances instance for each test."""
        self.finances = Finances()

    def test_set_income_raises(self):
        """
        Tests that `Finances.set_income` raises a ValueError 
        if the income is not a valid positive number.
        """
        with self.assertRaisesRegex(ValueError, 
            "Error: Cannot set the finances' income. The provided income must be a positive number greater than 0.0."):
            self.finances.set_income("£1000.00")

        with self.assertRaisesRegex(ValueError, 
            "Error: Cannot set the finances' income. The provided income must be a positive number greater than 0.0."):
            self.finances.set_income(0)

        with self.assertRaisesRegex(ValueError, 
            "Error: Cannot set the finances' income. The provided income must be a positive number greater than 0.0."):
            self.finances.set_income(-10)

    def test_set_income(self):
        """
        Tests that `Finances.set_income` correctly updates the income 
        when a valid positive number is provided.
        """
        expected_income = 1000
        self.finances.set_income(expected_income)
        self.assertEqual(self.finances.get_income(), expected_income)

    def test_get_income(self):
        """Tests that `Finances.get_income` returns the current income."""
        expected_income = 2000
        self.finances.set_income(expected_income)
        self.assertEqual(self.finances.get_income(), expected_income)


class TestFinancesExpenses(unittest.TestCase):
    """Unit tests for methods related to expenses in Finances."""    
    def setUp(self):
        """Sets up a Finances instance for each test."""
        self.finances = Finances()

    def test_get_expense_categories(self):
        """
        Tests that `Finances.get_expense_categories` returns a list of the categories
        in the expenses dictionary.
        """
        self.assertCountEqual(
            self.finances.get_expense_categories(),
            [ESSENTIAL, NON_ESSENTIAL]
        )

    def test_append_expense_raises(self):
        """
        Tests that `Finances.append_expense` raises: 
            
            - TypeError if the provided expense is not an Expense instance. 
            - ValueError if the provided expense has: 
                - an invalid category.
                - an empty or non-string title.
                - a non-positive amount.
        """
        with self.assertRaisesRegex(TypeError, 
            "Error: Cannot add expense, it must be of type 'Expense'."):
            self.finances.append_expense("A string")

        with self.assertRaisesRegex(TypeError, 
            "Error: Cannot add expense, it must be of type 'Expense'."):
            self.finances.append_expense(1000)

        with self.assertRaisesRegex(TypeError, 
            "Error: Cannot add expense, it must be of type 'Expense'."):
            self.finances.append_expense(True)

        with self.assertRaisesRegex(TypeError, 
            "Error: Cannot add expense, it must be of type 'Expense'."):
            self.finances.append_expense(None)

def test_get_sum_expenses_by_categories_raises(self):
        """Unit tests for the `Finances.get_sum_expenses_by_categories` raises: 
            
            - ValueError: If no categories are provided. 
            - ValueError: If any category is invalid.
            - TypeError: If any category is not a string.
        """
        with self.assertRaisesRegex(ValueError, 
            "Error: At least one category must be provided."):
            self.finances.get_sum_expenses_by_categories()
        
        with self.assertRaisesRegex(TypeError, 
            "Error: The provided categories must be non-empty strings."):
            self.finances.get_sum_expenses_by_categories(1, 2)

        with self.assertRaisesRegex(ValueError, 
            "Error: No expenses for the provided category: \"Unknown Category\" were found."):
            self.finances.get_sum_expenses_by_categories("Unknown Category")

if __name__ == '__main__':
    # Start coverage
    cov = coverage.Coverage()
    cov.start()

    # Run unit tests
    unittest.main()

    # Stop coverage
    cov.stop()
    # Save coverage stats
    cov.save()