import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

@pytest.fixture(scope="class")
def setup(request):

    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="/Users/ramanbadyal/Desktop/chromedriver")
        driver.get("https://rahulshettyacademy.com/angularpractice/")
    elif browser_name == "firefox":
        print("this is firefox browser")
    elif browser_name == "IE":
        print("this is IE")


    request.cls.driver = driver

    yield

    driver.quit()
