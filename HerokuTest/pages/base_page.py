from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
class BasePage:
      def __init__(self,driver):
          self.driver=driver
          self.wait=WebDriverWait(driver,10)
      def visit(self,url):
          self.driver.get(url)
          self.driver.implicitly_wait(3)
      def find(self,locator):
          return self.wait.until(EC.visibility_of_element_located(locator))
      def type(self,locator,text):
          element=self.find(locator)
          element.clear()
          element.send_keys(text)
      def click(self,locator):
          self.find(locator).click()
      def context_click(self,locator):
          element=self.find(locator)
          actions = ActionChains(self.driver)
          actions.context_click(element).perform()
      def check_alert(self):
          return self.wait.until(EC.alert_is_present())
      def drag_drop(self,drag,drop):
          source=self.find(drag)
          target=self.find(drop)
          actions= ActionChains(self.driver)
          actions.drag_and_drop(source,target).perform()
      def get_text(self,locator):
          return self.find(locator).text