from src.utilities.is_positive_number import is_positive_number
import unittest
import coverage

class TestIsPositiveNumber(unittest.TestCase):
    """Unit tests for the is_positive_number function"""

    def test_is_positive_number(self):
        
        # Tests that False is returned if argument is a String
        self.assertFalse(is_positive_number("Hello"))
        
        # Tests that False is returned if argument is a Boolean
        self.assertFalse(is_positive_number(True))
        
        # Tests that False is returned if argument is a List
        self.assertFalse(is_positive_number([0]))
        
        # Tests that False is returned if argument is a Dictionary
        self.assertFalse(is_positive_number({ "test": "example" }))

        # Tests that False is returned if argument is not a positive number
        self.assertFalse(is_positive_number(0))

        # Tests that False is returned if argument is negative number
        self.assertFalse(is_positive_number(-1))

        # Tests that True if argument is a positive number
        self.assertTrue(is_positive_number(1))

        # Tests that False is returned if argument is a string
        self.assertTrue(is_positive_number(0.01))


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