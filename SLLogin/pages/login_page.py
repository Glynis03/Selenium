from locators.login_locator import SLLoginLocators
from elements.element import SLElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class SLUsernameElement(SLElement):
      locator=SLLoginLocators.USERNAME
class SLPasswordElement(SLElement):
      locator=SLLoginLocators.PASSWORD     
class BasePage:
      def __init__(self,driver):
          self.driver=driver
class SLLogin(BasePage):
      username=SLUsernameElement()
      password=SLPasswordElement()
      def SLLoginTitle(self):
          return WebDriverWait(self.driver, 10).until(EC.title_is(("Swag Labs")))
      def SLLoginButton(self):
          self.driver.find_element(*SLLoginLocators.LOGIN).click()
