import pytest
from pages.checkbox_page import CheckboxesPage

@pytest.mark.order(2)
@pytest.mark.parametrize("page_url", ["checkbox_page"], indirect=True)
class TestCheckbox:
    def test_select_first_checkbox(self,driver,page_url):
        checkbox_page = CheckboxesPage(driver)
        checkbox_page.load(page_url)
        checkbox_page.select_checkbox(0)
        assert checkbox_page.is_checkbox_selected(0)


    def test_unselect_second_checkbox(self,driver,page_url):
        checkbox_page = CheckboxesPage(driver)
        checkbox_page.load(page_url)
        checkbox_page.unselect_checkbox(1)
        assert not checkbox_page.is_checkbox_selected(1)