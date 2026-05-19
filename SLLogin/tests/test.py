import unittest
from selenium import webdriver
from pages.login_page import SLLogin
from pages.inventory_page import SLInventory
class SwagsLabsTest(unittest.TestCase):
      def setUp(self):
          self.driver=webdriver.Edge()
          self.driver.maximize_window()
          self.driver.get("https://www.saucedemo.com/")
      def test_SL_Login(self):
          login=SLLogin(self.driver)
          login.SLLoginTitle()
          print(f"{self.driver.title} is loaded")
          self.assertEqual(self.driver.title,"Swag Labs")
          login.username='standard_user'
          login.password='secret_sauce'
          login.SLLoginButton() 
          inventory=SLInventory(self.driver)
          checktitle=inventory.is_title()
          print(f"Logged in successfully. Header says:{checktitle}")
          self.assertEqual(checktitle,'Products')
      def tearDown(self):
          self.driver.close()
if __name__=='__main__':
   unittest.main()