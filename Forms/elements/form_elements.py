from locators.form_locators import FormEntryPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

class FormEntryPageElements(object):
     def __set__(self,obj,value):
         driver=obj.driver
         WebDriverWait(driver,10).until(EC.visibility_of_element_located(self.locator))
         driver.find_element(*self.locator).clear()
         driver.find_element(*self.locator).send_keys(value)
     def __get__(self,obj,owner):
         driver=obj.driver
         WebDriverWait(driver,10).until(EC.visibility_of_element_located(self.locator))  
         return driver.find_element(*self.locator).get_attribute("value")

class RadioElement(object):
     def __set__(self, obj, value):
         driver = obj.driver
         WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.locator))
         driver.find_element(*self.locator).click()   