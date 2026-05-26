import pytest
from pages.login_page import LoginPage

def test_successful_login(driver):
    login_page=LoginPage(driver)
    login_page.load()
    login_page.login("tomsmith","SuperSecretPassword!")
    message=login_page.get_flash_message_text()
    assert "You logged into a secure area!" in message

def test_invalid_login(driver):
    login_page=LoginPage(driver)
    login_page.load()
    login_page.login("wrong-user","wrong-password!")
    message=login_page.get_flash_message_text()
    assert "Your username is invalid!" in message