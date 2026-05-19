import unittest
from selenium import webdriver
from pages.login_page import SLLogin
from pages.inventory_page import SLInventory
import time
class SwagsLabsInventoryTest(unittest.TestCase):
      def setUp(self):
          self.driver=webdriver.Edge()
          self.driver.maximize_window()
          self.driver.get("https://www.saucedemo.com/")
          login=SLLogin(self.driver)
          login.username='standard_user'
          login.password='secret_sauce'
          login.SLLoginButton() 
          self.inventory=SLInventory(self.driver)
      def test_title(self):
          checktitle=self.inventory.is_title()
          print(f"Logged in successfully. Header says:{checktitle}")
          self.assertEqual(checktitle,'Products')
      def test_prices_liho(self):
          self.inventory.filter("Price (high to low)")
          actual_list,expected_list=self.inventory.checkprice("hilo")
          self.assertEqual(actual_list, expected_list, "Prices are not sorted from High to Low")
          print("Prices are sorted High to Low")
      def test_prices_hilo(self):
          self.inventory.filter("Price (low to high)")
          actual_list,expected_list=self.inventory.checkprice("lohi")
          self.assertEqual(actual_list, expected_list, "Prices are not sorted from Low to High")
          print("Prices are sorted Low to High")
      def test_names_az(self):
          self.inventory.filter("Name (A to Z)")
          actual_list,expected_list=self.inventory.checkitemname("az")
          self.assertEqual(actual_list, expected_list, "Names are not sorted from A to Z")
          print("Names are sorted from A to Z")
      def test_names_za(self):
          self.inventory.filter("Name (Z to A)")
          actual_list,expected_list=self.inventory.checkitemname("za")
          self.assertEqual(actual_list, expected_list, "Names are not sorted from Z to A")
          print("Names are sorted from Z to A")

      def tearDown(self):
          self.driver.close()
if __name__=='_main__':
      unittest.main()