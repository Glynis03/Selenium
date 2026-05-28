import pytest
from pages.login_page import LoginPage

@pytest.mark.order(1)
@pytest.mark.parametrize("page_url", ["login_page"], indirect=True)
class TestLogin:
    def test_successful_login(self,driver,page_url):
        login_page=LoginPage(driver)
        login_page.load(page_url)
        login_page.login("tomsmith","SuperSecretPassword!")
        message=login_page.get_flash_message_text()
        assert "You logged into a secure area!" in message

    def test_invalid_login(self,driver,page_url):
        login_page=LoginPage(driver)
        login_page.load(page_url)
        login_page.login("wrong-user","wrong-password!")
        message=login_page.get_flash_message_text()
        assert "Your username is invalid!" in message