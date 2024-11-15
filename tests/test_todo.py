import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.todo_page import TodoPage
import os
import xmlrunner

class TodoTest(unittest.TestCase):
    def setUp(self):
    
        print("Initializing WebDriver...")
        service = Service(executable_path="chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://todomvc.com/examples/react/dist/")
        self.todo_page = TodoPage(self.driver)
        print("WebDriver initialized and page loaded.")

    def test_add_task(self):
        """Test adding a new task"""
        print("Running test: Add Task")
        task_name = "Learn Selenium"
        self.todo_page.add_task(task_name)
        self.assertTrue(self.todo_page.is_task_present(task_name))
        print(f"Task '{task_name}' added successfully.")

    def test_mark_task_complete(self):
        """Test marking a task as complete"""
        print("Running test: Mark Task Complete")
        task_name = "Write test cases"
        self.todo_page.add_task(task_name)
        self.todo_page.mark_task_as_complete(task_name)
        self.assertTrue(self.todo_page.is_task_completed(task_name))
        print(f"Task '{task_name}' marked as complete.")

    def test_delete_task(self):
        """Test deleting a task"""
        print("Running test: Delete Task")
        task_name = "Clean workspace"
        self.todo_page.add_task(task_name)
        self.todo_page.delete_task(task_name)
        self.assertFalse(self.todo_page.is_task_present(task_name))
        print(f"Task '{task_name}' deleted successfully.")

    def tearDown(self):
        print("Tearing down test: Closing WebDriver...")
        self.driver.quit()
        print("WebDriver closed.")

if __name__ == "__main__":
    report_dir = os.path.join(os.getcwd(), "reports")
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
        print("Reports directory created.")

    report_file = os.path.join(report_dir, "TestReport.xml")

    print(f"Starting test run... Report will be saved to: {report_file}")

    suite = unittest.TestLoader().loadTestsFromTestCase(TodoTest)
    
    with open(report_file, "wb") as output:
        print(f"Generating report to {report_file}...")
        runner = xmlrunner.XMLTestRunner(output=output)
        runner.run(suite)

    print("Test run complete. Report generated.")
