from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckboxesPage(BasePage):

    CHECKBOXES = (By.CSS_SELECTOR, "input[type='checkbox']")

    def __init__(self, driver):
        super().__init__(driver)
    
    def load(self,url):
          self.visit(url)

    def get_checkboxes(self):
        return self.driver.find_elements(*self.CHECKBOXES)

    def select_checkbox(self, index):
        checkboxes = self.get_checkboxes()
        if not checkboxes[index].is_selected():
            checkboxes[index].click()

    def unselect_checkbox(self, index):
        checkboxes = self.get_checkboxes()
        if checkboxes[index].is_selected():
            checkboxes[index].click()

    def is_checkbox_selected(self, index):
        checkboxes = self.get_checkboxes()
        return checkboxes[index].is_selected()