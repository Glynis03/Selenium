from selenium.webdriver.common.by import By 
from pages.base_page import BasePage

class DragDropPage(BasePage):
      COLUMN_A=(By.CSS_SELECTOR, "#column-a > header")
      COLUMN_B=(By.CSS_SELECTOR, "#column-b > header")
      def __init__(self,driver):
          super().__init__(driver)
          self.url="https://the-internet.herokuapp.com/drag_and_drop"
      def load(self):
          self.visit(self.url)
      def check_dragdrop_AtoB(self):
          self.drag_drop(self.COLUMN_A,self.COLUMN_B)
          text_a=self.get_text(self.COLUMN_A)
          text_b=self.get_text(self.COLUMN_B)
          return text_a,text_b
      def check_dragdrop_BtoA(self):
          self.drag_drop(self.COLUMN_B,self.COLUMN_A)
          text_a=self.get_text(self.COLUMN_A)
          text_b=self.get_text(self.COLUMN_B)
          return text_a,text_b
 
     
          