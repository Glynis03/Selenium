from pages.checkbox_page import CheckboxesPage

@pytest.mark.run(order=2)
def test_select_first_checkbox(driver):
    checkbox_page = CheckboxesPage(driver)
    checkbox_page.load()
    checkbox_page.select_checkbox(0)
    assert checkbox_page.is_checkbox_selected(0)


def test_unselect_second_checkbox(driver):
    checkbox_page = CheckboxesPage(driver)
    checkbox_page.load()
    checkbox_page.unselect_checkbox(1)
    assert not checkbox_page.is_checkbox_selected(1)