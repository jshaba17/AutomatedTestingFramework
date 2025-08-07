# Automated Testing Framework

This project is an automated testing framework for testing a web application (specifically, the TodoMVC React app) using Selenium WebDriver and Python. It demonstrates the Page Object Model (POM) design pattern for maintainable and organized test code. Test results are generated as **HTML reports** using [HtmlTestRunner](https://pypi.org/project/html-testRunner/).

---

## Prerequisites

- **Python**: Make sure Python is installed. Check with:
  ```
  python --version
  ```
- **Selenium**: Install via pip:
  ```
  pip install selenium
  ```
- **HtmlTestRunner**: Install via pip:
  ```
  pip install html-testRunner
  ```
- **WebDriver**: Download the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome).  
  - [ChromeDriver download](https://googlechromelabs.github.io/chrome-for-testing/)
  - Place the `chromedriver.exe` in your project directory or in your system's PATH.

---

## Project Structure

```
AutomatedTestingFramework/
│
├── pages/         # Page Object classes for web app pages
├── tests/         # Test scripts using page objects
├── reports/       # Folder where HTML reports are saved
├── run_tests.py   # Script to run all tests and generate HTML reports
├── requirements.txt
└── README.md
```

---

## Setup Instructions

1. **Clone the Repository**
   ```
   git clone https://github.com/jshaba17/AutomatedTestingFramework.git
   cd AutomatedTestingFramework
   ```

2. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

3. **Download WebDriver**
   - Download the correct ChromeDriver for your Chrome version.
   - Place `chromedriver.exe` in the project folder or add it to your PATH.

---

## Running the Tests

- **Run All Tests and Generate HTML Report**
  ```
  python run_tests.py
  ```
  - This will run all tests in the `tests/` directory and save an HTML report in the `reports/` folder.

- **Run Tests Manually (without report)**
  ```
  python -m unittest discover tests
  ```

---

## Generating Reports

- **HTML reports** are saved in the `reports/` directory.
- Each test run creates a new HTML file with detailed results, including pass/fail status, errors, and execution times.

---

## Example Output

**Console:**
```
Initializing WebDriver...
WebDriver initialized and page loaded.
Running test: Add Task
Task 'Learn Selenium' added successfully.
Tearing down test: Closing WebDriver...
WebDriver closed.
...
Ran 3 tests in 19.249s
OK
```

**HTML Report:**
- Open the generated `.html` file in the `reports/` folder to view detailed results in your browser.

---

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit (`git commit -am 'Add new feature'`).
5. Push (`git push origin feature-branch`).
6. Open a pull request.

---

## License

This project is open-source and available under the MIT License.

---

**Notes:**
- You can add more test cases or page objects by following the current structure.
- To use a different browser, update the WebDriver initialization in your test