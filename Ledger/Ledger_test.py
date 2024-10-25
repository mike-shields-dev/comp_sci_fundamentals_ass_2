import coverage
import unittest
from Ledger import Ledger
from constants import (
    INCOME, 
    EXPENSES, 
    ESSENTIAL, 
    NON_ESSENTIAL
)

class TestLedgerState(unittest.TestCase):
    """Unit tests for Ledger class"""    
    def setUp(self):
        """Sets up the Ledger instance to be tested."""
        self.ledger = Ledger()

    def test_get_state(self):
        """Tests that get_state returns a copy of the current state."""
        initial_state = {
            INCOME: 0.0,
            EXPENSES: {
                ESSENTIAL: [],
                NON_ESSENTIAL: [],
            }
        }
        self.assertEqual(self.ledger.get_state(), initial_state)

  
class TestLedgerIncome(unittest.TestCase):
    """Unit tests for methods related to the ledgers income."""    
    def setUp(self):
        """Sets up the Ledger instance to be tested."""
        self.ledger = Ledger()

    def test_set_income_raises(self):
        """
        Tests that set_income raises a ValueError 
        if the income is not a valid positive number.
        """
        with self.assertRaisesRegex(ValueError, 
            "Error: Cannot set the ledgers' income. The provided income must be a positive number greater than 0.0."):
            self.ledger.set_income("£1000.00")

        with self.assertRaisesRegex(ValueError, 
            "Error: Cannot set the ledgers' income. The provided income must be a positive number greater than 0.0."):
            self.ledger.set_income(0)

        with self.assertRaisesRegex(ValueError, 
            "Error: Cannot set the ledgers' income. The provided income must be a positive number greater than 0.0."):
            self.ledger.set_income(-10)

    def test_set_income(self):
        """
        Tests that set_income correctly updates the ledger's income 
        when a valid positive number is provided.
        """
        expected_income = 1000
        self.ledger.set_income(expected_income)
        self.assertEqual(self.ledger.get_income(), expected_income)

    def test_get_income(self):
        """Tests that `Ledger.get_income` returns the current income."""
        expected_income = 2000
        self.ledger.set_income(expected_income)
        self.assertEqual(self.ledger.get_income(), expected_income)


class TestLedgerExpenses(unittest.TestCase):
    """Unit tests for methods related to expenses in Ledger."""    
    def setUp(self):
        """Sets up a Ledger instance for each test."""
        self.ledger = Ledger()

    def test_get_expense_categories(self):
        """
        Tests that `Ledger.get_expense_categories` returns a list of the categories
        in the expenses dictionary.
        """
        self.assertCountEqual(
            self.ledger.get_expense_categories(),
            [ESSENTIAL, NON_ESSENTIAL]
        )

    def test_append_expense_raises(self):
        """
        Tests that `Ledger.append_expense` raises: 
            
            - TypeError if the provided expense is not an Expense instance. 
            - ValueError if the provided expense has: 
                - an invalid category.
                - an empty or non-string title.
                - a non-positive amount.
        """
        with self.assertRaisesRegex(TypeError, 
            "Error: Cannot add expense, it must be of type 'Expense'."):
            self.ledger.append_expense("A string")

        with self.assertRaisesRegex(TypeError, 
            "Error: Cannot add expense, it must be of type 'Expense'."):
            self.ledger.append_expense(1000)

        with self.assertRaisesRegex(TypeError, 
            "Error: Cannot add expense, it must be of type 'Expense'."):
            self.ledger.append_expense(True)

        with self.assertRaisesRegex(TypeError, 
            "Error: Cannot add expense, it must be of type 'Expense'."):
            self.ledger.append_expense(None)

    def test_get_sum_expenses_by_categories_raises(self):
            """Unit tests for the `Ledger.get_sum_expenses_by_categories` raises: 
                
                - ValueError: If no categories are provided. 
                - ValueError: If any category is invalid.
                - TypeError: If any category is not a string.
            """
            with self.assertRaisesRegex(ValueError, 
                "Error: At least one category must be provided."):
                self.ledger.get_sum_expenses_by_categories()
            
            with self.assertRaisesRegex(TypeError, 
                "Error: The provided categories must be non-empty strings."):
                self.ledger.get_sum_expenses_by_categories(1, 2)

            with self.assertRaisesRegex(ValueError, 
                "Error: No expenses for the provided category: \"Unknown Category\" were found."):
                self.ledger.get_sum_expenses_by_categories("Unknown Category")

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