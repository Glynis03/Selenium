from elements.form_elements import FormEntryPageElements
from locators.form_locators import FormEntryPageLocators
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC

class FirstNameElement(FormEntryPageElements):
      locator=FormEntryPageLocators.FIRST_NAME
class LastNameElement(FormEntryPageElements):
      locator=FormEntryPageLocators.LAST_NAME
class EmailElement(FormEntryPageElements):
      locator=FormEntryPageLocators.EMAIL
class MobileElement(FormEntryPageElements):
      locator=FormEntryPageLocators.MOBILE

class BasePage:
      def __init__(self, driver):
          self.driver=driver

class FormEntryPage(BasePage):
      firstname=FirstNameElement()
      lastname=LastNameElement()
      email=EmailElement()
      def click_gender(self):
          self.driver.find_element(*FormEntryPageLocators.GENDER_MALE_LABEL).click()
      
      mobile=MobileElement()
      def set_date_of_birth(self, day, month, year):
          self.driver.find_element(*FormEntryPageLocators.DATE_OF_BIRTH).click()
          wait = WebDriverWait(self.driver, 10)
          month_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "react-datepicker__month-select")))
          month_dropdown = Select(self.driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
          month_dropdown.select_by_visible_text(month)
          year_dropdown = Select(self.driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
          year_dropdown.select_by_visible_text(year)
          day_xpath = f"//div[contains(@class, 'react-datepicker__day--{day.zfill(3)}') and not(contains(@class, 'outside-month'))]"
          self.driver.find_element(By.XPATH, day_xpath).click()
      def click_login(self):
          submit_button=self.driver.find_element(*FormEntryPageLocators.SUBMIT_BUTTON)
          self.driver.execute_script("arguments[0].click();", submit_button)
class FormSubmissionPage(BasePage):
      def get_modal_title(self):
          element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg")))
          return element.text
      def get_table_data(self):
          table_body = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "table.table tbody")))
          rows = table_body.find_elements(By.TAG_NAME, "tr")
          scraped_data = {}
          for row in rows:
            columns = row.find_elements(By.TAG_NAME, "td")
            if len(columns) == 2: 
                label = columns[0].text.strip()
                value = columns[1].text.strip()
                scraped_data[label] = value
          return scraped_data
      def click_close(self):
          closebutton=WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID,"closeLargeModal")))
          closebutton.click()