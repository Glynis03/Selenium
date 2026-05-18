from selenium.webdriver.common.by import By

class FormEntryPageLocators(object):
     FIRST_NAME=(By.ID,"firstName")
     LAST_NAME=(By.ID,"lastName")
     EMAIL=(By.ID,"userEmail")
     MOBILE=(By.ID,"userNumber")
     GENDER_MALE_LABEL = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
     DATE_OF_BIRTH=(By.ID,"dateOfBirthInput")
     SUBMIT_BUTTON = (By.ID, "submit")
     