import pytest
from pages.contextclick_page import ContextMenuPage

@pytest.mark.run(order=3)
def test_context_click(driver):
      contextclick=ContextMenuPage(driver)
      contextclick.load()
      message=contextclick.context_click_alert()
      assert message == "You selected a context menu", f"Expected menu message but got: '{message}'"

      