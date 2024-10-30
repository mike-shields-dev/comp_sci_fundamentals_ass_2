import coverage
import unittest
from src.Expense import Expense
from src.Ledger import Ledger
from src.constants import (
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
        """Tests that `get_state` returns a copy of the ledger's current state."""
        expected_state = {
            INCOME: 0.0,
            EXPENSES: {
                ESSENTIAL: [],
                NON_ESSENTIAL: [],
            }
        }

        self.assertEqual(self.ledger.get_state(), expected_state)

  
class TestLedgerIncome(unittest.TestCase):
    """Unit tests for methods related to the ledgers income."""    
    
    def setUp(self):
        """Sets up the Ledger instance to be tested."""
        self.ledger = Ledger()

    
    def test_set_income_raises(self):
        """
        Tests that `set_income` raises a ValueError 
        if the income is not a valid positive number.
        """
        with self.assertRaisesRegex(ValueError, 
            "Error: income must be a number greater than 0.0."):
            self.ledger.set_income("£1000.00")

        with self.assertRaisesRegex(ValueError, 
            "Error: income must be a number greater than 0.0."):
            self.ledger.set_income(0)

        with self.assertRaisesRegex(ValueError, 
            "Error: income must be a number greater than 0.0."):
            self.ledger.set_income(-10)


    def test_get_income(self):
        """Tests that `get_income` returns the current income."""
        expected_income = 1234
        self.ledger.set_income(expected_income)

        self.assertEqual(self.ledger.get_income(), expected_income)
    

    def test_set_income(self):
        """
        Tests that `set_income` correctly updates the ledger's income 
        when a positive number is provided.
        """
        expected_income = 1000
        
        self.ledger.set_income(expected_income)
        self.assertEqual(self.ledger.get_income(), expected_income)


class TestLedgerExpenses(unittest.TestCase):
    """Unit tests for methods related to expenses in Ledger."""    
    
    def setUp(self):
        """Sets up a Ledger instance for each test."""
        self.ledger = Ledger()

    
    def test_get_expense_categories(self):
        """
        Tests that `get_expense_categories` returns a list of the categories
        in the expenses dictionary.
        """
        self.assertCountEqual(
            self.ledger.get_expense_categories(),
            [ESSENTIAL, NON_ESSENTIAL]
        )

    
    def test_append_expense_raises(self):
        """
        Tests that `append_expense` raises: 
            
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

        fake_expense = {
            "amount": 0,
            "category": ESSENTIAL,
            "title": "test expense"
        }
        
        with self.assertRaisesRegex(TypeError, 
            "Error: Cannot add expense, it must be of type 'Expense'."):
            self.ledger.append_expense(fake_expense)

        expense_invalid_amount = Expense(
            amount=-10, 
            category=ESSENTIAL, 
            title="Expense with invalid amount"
        )

        with self.assertRaisesRegex(ValueError, 
            "Error: Cannot add expense, its amount must be a number greater than 0.0."):
            self.ledger.append_expense(expense_invalid_amount)
            
        expense_invalid_category = Expense(
            amount= 100, 
            category="Non Existent Category", 
            title="Expense with invalid category"
        )

        with self.assertRaisesRegex(ValueError, 
            "Error: Cannot add expense, its category is not a valid expense category"):
            self.ledger.append_expense(expense_invalid_category)

        expense_invalid_title = Expense(
            amount= 100, 
            category=ESSENTIAL,
            title=""
        )

        with self.assertRaisesRegex(ValueError, 
            "Error: Cannot add expense, its title is not a valid expense category"):
            self.ledger.append_expense(expense_invalid_title)

    
    def test_get_all_expenses(self):
        
        expense_1 = Expense(80, ESSENTIAL, "Groceries")
        expense_2 = Expense(12, ESSENTIAL, "Phone Bill")
        expense_3 = Expense(40, ESSENTIAL, "Travel")

        self.ledger.append_expense(expense_1)
        self.ledger.append_expense(expense_2)
        self.ledger.append_expense(expense_3)

        self.assertCountEqual(self.ledger.get_all_expenses(), [expense_1, expense_2, expense_3])

    
    def test_get_expenses_by_category(self):
        """
        Tests that get_expenses_by_category returns
        a list of expenses by their categories
        """

        essential_expense = Expense(80, ESSENTIAL, "Groceries")
        non_essential_expense = Expense(20, NON_ESSENTIAL, "Cinema")

        self.ledger.append_expense(essential_expense)

        self.assertEqual(
            self.ledger.get_expenses_by_category(ESSENTIAL), 
            [essential_expense]
        )

        self.ledger.append_expense(non_essential_expense)

        self.assertEqual(
            self.ledger.get_expenses_by_category(NON_ESSENTIAL, non_essential_expense),
            [non_essential_expense]
        )

        self.assertEqual(
            self.ledger.get_expenses_by_category(ESSENTIAL, NON_ESSENTIAL), 
            [essential_expense, non_essential_expense]
        )

    def test_is_unique_expense_title(self):
        """
        Tests that `is_unique_expense_title` returns a boolean: 
            True: if the provided `title` is unique
            False: if the provided `title` is not unique
        """
        expense = Expense(
            amount=10, 
            category=NON_ESSENTIAL, 
            title="Chocolate"
        )
        
        self.ledger.append_expense(expense)

        self.assertEqual(
            self.ledger.is_unique_expense_title("Chocolate"), 
            False
        )

        self.assertEqual(
            self.ledger.is_unique_expense_title("Ice Cream"), 
            True
        )


if __name__ == '__main__':
    # Start coverage
    cov = coverage.Coverage()
    cov.start()

    # Run unit tests
    unittest.main(exit=False)

    # Stop coverage
    cov.stop()
    # Save coverage stats
    cov.save()

    # Display coverage report in the terminal
    cov.report()

    # Optionally, create an HTML coverage report
    cov.html_report(directory='coverage_html_report')