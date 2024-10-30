from src.utilities.is_non_empty_string import is_non_empty_string
import unittest
import coverage

class TestIsNonEmptyString(unittest.TestCase):
    """Unit tests for the is_non_empty_string function"""

    def test_is_non_empty_string(self):
        # Tests that True is returned if argument is "Hello"
        self.assertTrue(is_non_empty_string("Hello"))
        
        # Tests that False is returned if argument is a Boolean
        self.assertFalse(is_non_empty_string(True))
        
        # Tests that False is returned if argument is a List
        self.assertFalse(is_non_empty_string([0]))
        
        # Tests that False is returned if argument is a Dictionary
        self.assertFalse(is_non_empty_string({ "test": "example" }))

        # Tests that False is returned if argument is not a positive number
        self.assertFalse(is_non_empty_string(0))

        # Tests that False is returned if argument is negative number
        self.assertFalse(is_non_empty_string(-1))

        # Tests that True if argument is a positive number
        self.assertFalse(is_non_empty_string(1))

        # Tests that False is returned if argument is a string
        self.assertFalse(is_non_empty_string(0.01))


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