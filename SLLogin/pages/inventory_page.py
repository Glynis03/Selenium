from locators.inventory_locator import SLInventoryLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class BasePage:
      def __init__(self,driver):
          self.driver=driver
 
class SLInventory(BasePage):
      def is_title(self):
          element=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(SLInventoryLocators.TITLE))
          return element.text
      def filter(self,value):
          mapping = {
                      'Name (A to Z)': 'az',
                      'Name (Z to A)': 'za',
                      'Price (low to hiiigh)': 'lohi',
                      'Price (high to low)': 'hilo'
                    }
          select=Select(WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(SLInventoryLocators.FILTER)))
          select.select_by_value(mapping.get(value, 'lohi'))
      def checkprice(self,filter):
          celement=self.driver.find_elements(*SLInventoryLocators.PRICES)
          prices = []
          for e in celement:
               clean_price = float(e.text.replace("$", ""))
               prices.append(clean_price)
          if filter=="lohi":
               sort_price=sorted(prices)             
          else:
               sort_price=sorted(prices,reverse=True)
          return prices,sort_price
      def checkitemname(self,filter):
          nelement=self.driver.find_elements(*SLInventoryLocators.ITEM_NAME)
          names = []
          for e in nelement:
               names.append(e.text)
          if filter=="az":
             sort_name=sorted(names)            
          else:
             sort_name=sorted(names,reverse=True)
          return names,sort_name