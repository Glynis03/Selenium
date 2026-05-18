import unittest
from selenium import webdriver
from pages.form_page import FormEntryPage, FormSubmissionPage
import time	
class FormEntryPageSubmit(unittest.TestCase):
      def setUp(self):
          self.driver=webdriver.Edge()
          self.driver.maximize_window()
          self.driver.get("https://demoqa.com/automation-practice-form")
      def test_Form_page_submit(self):
          formentrypage=FormEntryPage(self.driver)
          formentrypage.firstname="Gname"
          formentrypage.lastname="Lname"
          formentrypage.email="gname.lname@gmail.com"
          formentrypage.click_gender()
          formentrypage.mobile='9876543210'
          formentrypage.set_date_of_birth("17", "May", "1999")
          print(f"Logged in as :{formentrypage.firstname}")
          formentrypage.click_login()
          submitted = FormSubmissionPage(self.driver)
          data = submitted.get_modal_title()
          print(data)
          self.assertEqual(data, "Thanks for submitting the form")
          data = submitted.get_table_data()
          print("\n--- Form Submission Results ---")
          #print(data)
          for label, value in data.items():
            print(f"Submitted {label}: {value}")
          submitted.click_close()
          print("close")
        # 3. Add Unittest Assertions using the dictionary data
         #self.assertEqual(data.get("Student Name"), "gsdf fadaf")
         #self.assertEqual(data.get("Mobile"), "6468411544")

      def tearDown(self):
          print("Test finished. Waiting 15 seconds before closing...")
          time.sleep(10)
          self.driver.close()

if __name__=='__main__':
      unittest.main()