import unittest
import xmlrunner

# Discover tests in the "tests" folder and run them
suite = unittest.defaultTestLoader.discover('tests', pattern='test_*.py')

# Run the tests and generate an XML report
with open('reports/test_report.xml', 'wb') as output:
    runner = xmlrunner.XMLTestRunner(output=output)
    runner.run(suite)
