import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture(scope="function")
def driver():
     options=Options()
     options.add_argument("--start-maximized")
     options.add_argument("--disable-gpu")
     service=Service(EdgeChromiumDriverManager().install())
     driver=webdriver.Edge(service=service,options=options)
     yield driver
     driver.quit()