from src.utilities.format_to_sterling import format_to_sterling
import unittest
import coverage

class TestFormatToSterling(unittest.TestCase):
    """Unit tests for the format_to_sterling function"""

    def test_format_to_sterling_raises(self):
        with self.assertRaisesRegex(
            ValueError,
            "Error: Cannot format provided amount, the amount must be number"
        ):
            format_to_sterling("Hello")
        
        with self.assertRaisesRegex(
            ValueError,
            "Error: Cannot format provided amount, the amount must be number"
        ):
            format_to_sterling(True)
        
        with self.assertRaisesRegex(
            ValueError,
            "Error: Cannot format provided amount, the amount must be number"
        ):
            format_to_sterling([0])

        with self.assertRaisesRegex(
            ValueError,
            "Error: Cannot format provided amount, the amount must be number"
        ):
            format_to_sterling({ "test": "example" })
        
        with self.assertRaisesRegex(
            ValueError,
            "Error: Cannot format provided amount, the amount must be number"
        ):
            format_to_sterling("0.50")

    def test_format_to_string(self):
        self.assertEqual(
            format_to_sterling(0.50),
            "£0.50"
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