from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import requests
class BrokenImage(BasePage):
      IMAGE=(By.CSS_SELECTOR,'.example > img')
      def __init__(self,driver):
          super().__init__(driver)
      def load(self,url):
          self.visit(url)
      def check_brokenimage_request(self):
          elements=self.find_all_elements(self.IMAGE)
          data={}
          for img in elements:
              url=img.get_attribute("src")
              try:
                  response=requests.get(url,timeout=10)
                  if response.status_code>=400:
                     data[url]="Broken"
                  else:
                     data[url]="Valid"
              except Exception as e:
                  print("error")
          return data
      def check_brokenimage_script(self):
          elements=self.find_all_elements(self.IMAGE)
          data={}
          for img in elements:
              is_loaded = self.driver.execute_script("""
                           return arguments[0].complete &&
                             arguments[0].naturalWidth > 0;
                              """, img)
              url = img.get_attribute("src")
              if is_loaded:
                 data[url]="Valid"
              else:
                 data[url]="Broken"
          return data                     
    