from pages.base_page import BasePage
from selenium.webdriver.common.by import By
class DropDownPage(BasePage):
      DROPDOWN=(By.ID,"dropdown")
      def __init__(self,driver):
          super().__init__(driver)
      def load(self,url):
          self.visit(url)
      def dropdown_page(self,value):
          option=self.drop_down(self.DROPDOWN,value)
          return option

          