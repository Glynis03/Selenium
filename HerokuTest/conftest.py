import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utils.excel_reader import get_url_by_page

@pytest.fixture(scope="function")
def driver():
     options=Options()
     options.add_argument("--start-maximized")
     options.add_argument("--disable-gpu")
     service=Service(EdgeChromiumDriverManager().install())
     driver=webdriver.Edge(service=service,options=options)
     yield driver
     driver.quit()

@pytest.fixture
def page_url(request):
    page_name = request.param
    return get_url_by_page(
                         "testdata/pages.xlsx",
                          "Sheet1",
                           page_name
                           )