import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from src.helper.Browser import BrowserTypes


@pytest.fixture(scope="session", autouse=True)
def gen_test_data():
    # TODO: Use Faker to generate some locations
    return ['San Franciso, CA']


@pytest.fixture(scope="session")
def setting():
    return BrowserTypes.FIREFOX


@pytest.fixture(scope="session")
def setup(setting):
    # TODO: Get this configuration wise to get multiple browser
    if setting == BrowserTypes.CHROME:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif setting == BrowserTypes.EDGE:
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(2)  # Seconds
    # driver.maximize_window()
    yield driver
    driver.quit()
