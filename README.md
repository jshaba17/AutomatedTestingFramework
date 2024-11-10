Automated Testing Framework
This project is an automated testing framework for testing a web application (in this case, a TodoMVC application) using Selenium WebDriver and Python. It demonstrates the use of the Page Object Model (POM) design pattern, which helps organize the test code and makes it more maintainable.

Table of Contents
Prerequisites
Project Structure
Setup Instructions
Running the Tests
Generating Reports
Contributing
License
Prerequisites
Before you start, ensure that you have the following installed:

Python 3.x: Make sure Python is installed on your system. You can check by running:

css
Copy code
python --version
Selenium: Selenium WebDriver is used for browser automation. It needs to be installed via pip:

Copy code
pip install selenium
WebDriver: For Selenium to control the browser, you need to install the appropriate WebDriver (e.g., ChromeDriver for Google Chrome).

Download ChromeDriver (make sure to download the version that corresponds to your installed version of Chrome).
Place the chromedriver executable in your project directory or in a directory that’s added to your system's PATH.
Optional (For XML Reports):

Python's built-in unittest module already supports XML reports, and this project generates reports in XML format.
Project Structure
Here's an overview of the project directory structure:

bash
Copy code
AutomatedTestingFramework/
│
├── pages/
│   ├── base_page.py       # Base Page class with common methods
│   └── todo_page.py       # Page Object for Todo page
│
├── tests/
│   └── test_todo.py       # Test cases for Todo application
│
├── reports/               # Folder where test reports will be saved
│
├── requirements.txt       # List of Python dependencies
├── run_tests.py           # Script to run tests and generate reports
└── README.md              # Project documentation (this file)
pages/: Contains the Page Object classes that represent different pages of the web application. These classes define elements and actions on the pages.
tests/: Contains test scripts that use the page objects to perform specific tests on the application.
reports/: Folder where XML reports will be saved after the tests are executed.
run_tests.py: A Python script that runs all the tests and generates reports.
requirements.txt: Lists all the required dependencies for the project.
Setup Instructions
Clone the Repository: Clone this repository to your local machine.

bash
Copy code
git clone https://github.com/jshaba17/AutomatedTestingFramework.git
cd AutomatedTestingFramework
Install Dependencies: Install the required Python packages using pip.

bash
Copy code
pip install -r requirements.txt
Download WebDriver:

Download the appropriate WebDriver for your browser (ChromeDriver for Chrome, GeckoDriver for Firefox).
Ensure the chromedriver executable is located in the project folder or added to your system's PATH.
Update WebDriver Path (if necessary): If you are using a WebDriver in a different location, update the webdriver.Chrome(executable_path="path/to/chromedriver") in your test_todo.py file to match the path to your WebDriver executable.

Running the Tests
Run Tests from Command Line: To run the tests, use the unittest module:

bash
Copy code
python -m unittest discover tests
This command will discover and execute all the test cases in the tests/ directory.

Run Tests with Report Generation: To run the tests and generate a report, execute the run_tests.py script:

bash
Copy code
python run_tests.py
This will run the tests and save the XML reports in the reports/ directory.

Generating Reports
The test results will be saved in the reports/ directory.
The results will be saved in XML format as test_report.xml by default.
Example Output in Console:
bash
Copy code
Initializing WebDriver...
WebDriver initialized and page loaded.
Running test: Add Task
Task 'Learn Selenium' added successfully.
Tearing down test: Closing WebDriver...
WebDriver closed.

Running test: Delete Task
Task 'Clean workspace' deleted successfully.

Running test: Mark Task Complete
Task 'Write test cases' marked as complete.

Ran 3 tests in 10.610s
OK
Example Output in XML Report:
The XML report will include the status of each test case, details of any failures, and execution times. This format is compatible with CI/CD systems for further processing.
Contributing
If you'd like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Open a pull request.
License
This project is open-source and available under the MIT License.

Notes:
Test Case Organization: You can add more test cases or page objects by following the same pattern used in the current setup.
Custom Web Drivers: If you prefer to use a different browser or WebDriver, you can update the driver initialization in the test_todo.py or run_tests.py files.