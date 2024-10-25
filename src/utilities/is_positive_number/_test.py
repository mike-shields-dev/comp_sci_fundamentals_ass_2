from utilities.is_positive_number.is_positive_number import is_positive_number
import unittest
import coverage

class TestIsPositiveNumber(unittest.TestCase):
    """A suite of tests for the is_positive_number function"""

    def test_is_positive_number_raises(self):
        """
        Asserts that the is_positive_number method
        raises an exception if no value argument is provided.
        """
        with self.assertRaises(
            TypeError,
        ):
            is_positive_number()

# Only run tests if file is executed directly  
if __name__ == '__main__':
    cov = coverage.Coverage()
    cov.start()

    unittest.main()

    cov.stop()
    cov.save()

    cov.html_report()
    print("Done.")