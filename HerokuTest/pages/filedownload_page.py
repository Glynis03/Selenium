import os
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class FileDownload_page(BasePage):
      FILEDOWNLOAD=(By.CSS_SELECTOR,'div.example > a')
      path=r'C:\Users\Avinash Family\Downloads'
      def __init__(self,driver):
          super().__init__(driver)
      def load(self,url):
          self.visit(url)
      def download_file(self,filename):
          elements=self.find_all_elements(self.FILEDOWNLOAD)
          for e in elements:
              if e.text==filename:
                 e.click()
                 return os.path.join(self.path,filename)
          return "No File"
             
