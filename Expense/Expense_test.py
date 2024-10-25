import coverage
import unittest
from Expense import Expense

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
            category="Essential", 
            amount=100, 
            title="Groceries"
        )

    def test_get_amount(self):
        """
        Tests that `Expense.get_amount` returns the correct expense amount.
        """
        self.assertEqual(self.expense.get_amount(), 100)

    def test_set_amount_raises(self):
        """
        Tests that `Expense.set_amount` raises a ValueError if the amount 
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
        Tests that `Expense.set_amount` correctly updates the expense's amount.
        """
        self.expense.set_amount(333)
        self.assertEqual(self.expense.get_amount(), 333)

    def test_get_category(self):
        """
        Tests that `Expense.get_category` returns the correct category.
        """
        self.assertEqual(self.expense.get_category(), "Essential")

    def test_set_category(self):
        """
        Tests that `Expense.set_category` correctly updates the expense's category.
        """
        self.expense.set_category("Test Category")
        self.assertEqual(self.expense.get_category(), "Test Category")


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