import pytest
from pages.dropdown_page import DropDownPage

@pytest.mark.order(6)
@pytest.mark.parametrize("page_url",["dropdown_page"],indirect=True)
class TestDropDown:
      def test_dropdown_1(self,driver,page_url):
          dropdown=DropDownPage(driver)
          dropdown.load(page_url)
          option=dropdown.dropdown_page("1")
          assert option=="Option 1" , f"Expected Option 1 but got {option}"

      def test_dropdown_2(self,driver,page_url):
          dropdown=DropDownPage(driver)
          dropdown.load(page_url)
          option=dropdown.dropdown_page("2")
          assert option=="Option 2" , f"Expected Option 1 but got {option}"






     