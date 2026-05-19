from locators.inventory_locator import SLInventoryLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:
      def __init__(self,driver):
          self.driver=driver
 
class SLInventory(BasePage):
      def is_title(self):
          element=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(SLInventoryLocators.TITLE))
          return element.text