import unittest
import HtmlTestRunner

# Discover tests in the "tests" folder and run them
suite = unittest.defaultTestLoader.discover('tests', pattern='test_*.py')

# Run the  tests and generate an HTML report
runner = HtmlTestRunner.HTMLTestRunner(output='reports')
runner.run(suite)