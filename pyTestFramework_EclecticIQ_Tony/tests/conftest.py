import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

@pytest.fixture(scope="class")
def setup(request):

    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\SeleniumWebdriverPython\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\SeleniumWebdriverPython\\geckodriver.exe")

    driver.get("https://mystifying-beaver-ee03b5.netlify.app/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
