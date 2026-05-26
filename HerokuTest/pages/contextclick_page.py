from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContextMenuPage(BasePage):
      CONTEXTMENU=(By.ID, "hot-spot")
      def __init__(self,driver):
          super().__init__(driver)
          self.url="https://the-internet.herokuapp.com/context_menu"
      def load(self):
          self.visit(self.url)
      def context_click_alert(self):
          self.context_click(self.CONTEXTMENU)
          alert=self.check_alert()
          if alert:
             alert_window = self.driver.switch_to.alert
             alert_text = alert_window.text
             alert_window.accept()
             return alert_text
          else:
             return "No Alert"

          