from selenium.webdriver.common.by import By 
from pages.base_page import BasePage

class LoginPage(BasePage):
      USERNAME_INPUT=(By.ID,"username")
      PASSWORD_INPUT=(By.ID,"password")
      LOGIN_BUTTON=(By.CSS_SELECTOR,"button[type='submit']")
      FLASH_MESSAGE=(By.ID,"flash")
      def __init__(self,driver):
          super().__init__(driver)
      def load(self,url):
          self.visit(url)
      def login(self,username,password):
          self.type(self.USERNAME_INPUT,username)
          self.type(self.PASSWORD_INPUT,password)
          self.click(self.LOGIN_BUTTON)
      def get_flash_message_text(self):
          return self.find(self.FLASH_MESSAGE).text
