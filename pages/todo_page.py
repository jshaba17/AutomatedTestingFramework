from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TodoPage(BasePage):
    TASK_INPUT = (By.CLASS_NAME, "new-todo")
    TASK_LIST = (By.CSS_SELECTOR, ".todo-list li")
    TASK_COMPLETE = (By.CLASS_NAME, "toggle")
    DELETE_BUTTON = (By.CLASS_NAME, "destroy")

    def add_task(self, task_name):
        self.enter_text(self.TASK_INPUT, task_name)
        self.find_element(self.TASK_INPUT).send_keys("\n")

    def is_task_present(self, task_name):
        tasks = [task.text for task in self.find_elements(self.TASK_LIST)]
        return task_name in tasks

    def mark_task_as_complete(self, task_name):
        tasks = self.find_elements(self.TASK_LIST)
        for task in tasks:
            if task_name in task.text:
                task.find_element(*self.TASK_COMPLETE).click()
                break

    def delete_task(self, task_name):
        tasks = self.find_elements(self.TASK_LIST)
        for task in tasks:
            if task_name in task.text:
                self.driver.execute_script("arguments[0].style.display = 'block';", task.find_element(*self.DELETE_BUTTON))
                task.find_element(*self.DELETE_BUTTON).click()
                break

    def is_task_completed(self, task_name):
        tasks = self.find_elements(self.TASK_LIST)
        for task in tasks:
            if task_name in task.text:
                return "completed" in task.get_attribute("class")
        return False
