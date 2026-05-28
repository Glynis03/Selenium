import pytest
from pages.contextclick_page import ContextMenuPage

@pytest.mark.order(4)
@pytest.mark.parametrize("page_url", ["contextclick_page"], indirect=True)
class TestContextClick:
    def test_context_click(self,driver,page_url):
          contextclick=ContextMenuPage(driver)
          contextclick.load(page_url)
          message=contextclick.context_click_alert()
          assert message == "You selected a context menu", f"Expected menu message but got: '{message}'"

      