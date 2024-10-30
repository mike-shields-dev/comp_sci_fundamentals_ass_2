import coverage
import unittest
from src.Expense import Expense
from src.constants import ESSENTIAL, AMOUNT, CATEGORY, TITLE

class TestExpense(unittest.TestCase):
    """
    Unit tests for the Expense class's methods related to 
    getting and setting expense attributes such as amount and category.
    """
    def setUp(self):
        """
        Initializes a sample Expense instance for use in the test methods.
        """
        self.expense = Expense(
            amount=100, 
            category=ESSENTIAL, 
            title="Groceries"
        )

    def test_get_state(self):
        """
        Tests that `get_state` returns a copy of the expenses current state
        """

        self.assertEqual(
            self.expense.get_state(),
            { 
                AMOUNT: 100,
                CATEGORY: ESSENTIAL,
                TITLE: "Groceries"
            }
        )

    def test_get_amount(self):
        """
        Tests that `get_amount` returns the correct expense amount.
        """
        self.assertEqual(self.expense.get_amount(), 100)


    def test_set_amount_raises(self):
        """
        Tests that `set_amount` raises a ValueError if the amount 
        is not a valid positive number.
        """
        with self.assertRaisesRegex(
            ValueError, 
            "Error: The expense's amount can only be set to a number greater than 0.0"
        ):
            self.expense.set_amount("£50")

        with self.assertRaisesRegex(
            ValueError,
            "Error: The expense's amount can only be set to a number greater than 0.0"
        ):
            self.expense.set_amount(-50)

        with self.assertRaisesRegex(
            ValueError,
            "Error: The expense's amount can only be set to a number greater than 0.0"
        ):
            self.expense.set_amount(0)


    def test_set_amount(self):
        """
        Tests that `set_amount` correctly updates the expense's amount.
        """
        self.expense.set_amount(333)

        self.assertEqual(self.expense.get_amount(), 333)


    def test_get_category(self):
        """
        Tests that `get_category` returns the correct category.
        """
        self.assertEqual(self.expense.get_category(), "Essential")

    
    def test_set_category_raises(self):
        """
        Tests that `set_category` raises a ValueError if the amount 
        is not a non-empty string.
        """
        with self.assertRaisesRegex(
            ValueError, 
            "Error: The expense's category must be a non-empty string"
        ):
            self.expense.set_category("")

        with self.assertRaisesRegex(
            ValueError,
            "Error: The expense's category must be a non-empty string"
        ):
            self.expense.set_category(" ")

        with self.assertRaisesRegex(
            ValueError,
            "Error: The expense's category must be a non-empty string"
        ):
            self.expense.set_category(0)
        
        with self.assertRaisesRegex(
            ValueError,
            "Error: The expense's category must be a non-empty string"
        ):
            self.expense.set_category(True)       


    def test_set_category(self):
        """
        Tests that `set_category` correctly updates the expense's category.
        """
        self.expense.set_category("Test Category")
        self.assertEqual(self.expense.get_category(), "Test Category")


    def test_set_title_raises(self):
        """
        Tests that `set_category` raises:

        ValueError: 
            if the provided category is not a non-empty string
        """
        
        with self.assertRaisesRegex(
            ValueError,
            "Error: The expense's title must be a non-empty string."
        ):
            self.expense.set_title("")

        with self.assertRaisesRegex(
            ValueError, 
            "Error: The expense's title must be a non-empty string."
        ):
            self.expense.set_title(" ")

        with self.assertRaisesRegex(
            ValueError, 
            "Error: The expense's title must be a non-empty string."
        ):
            self.expense.set_title(1)

        with self.assertRaisesRegex(
            ValueError, 
            "Error: The expense's title must be a non-empty string."
        ):
            self.expense.set_title(True)


    def test_set_title(self):
        """
        Tests that `set_title` set the expense `title`
        property to the provided `title` argument
        """
        self.expense.set_title("Groceries")

        self.assertEqual(
            self.expense.get_title(),
            "Groceries"
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