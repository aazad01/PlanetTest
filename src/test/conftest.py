import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from src.helper.Browser import BrowserTypes
from src.web import Environment
from src.web.account.page.methods.AccountMethods import AccountMethods
from src.web.account.page.methods.SignInMethods import SignInMethods
from src.web.explorer.page.methods.SearchBarMethods import SearchBarMethods
from src.web.explorer.page.methods.WelcomeMethods import WelcomeMethods


def pytest_generate_tests(metafunc):
    if "gen_test_data" in metafunc.fixturenames:
        # if metafunc.config.getoption("all"):
        #     metafunc.parametrize("gen_test_data", ['Random'])
        # else:
        #     metafunc.parametrize("gen_test_data", ['San Franciso, CA', 'Latham, NY'])
        metafunc.parametrize("gen_test_data", ['San Franciso, CA', 'Latham, NY'])


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="session")
def setting():
    return BrowserTypes.FIREFOX


@pytest.fixture(scope="session")
def setup(request):
    # TODO: Get this configuration wise to get multiple browser
    if request == BrowserTypes.CHROME:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif request == BrowserTypes.EDGE:
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(5)  # Seconds
    # driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def before_test(setup):
    signin = SignInMethods(setup)
    signin.login(Environment.USERNAME, Environment.PASSWORD)

    account = AccountMethods(setup)
    account.verify_welcome()
    search = SearchBarMethods(setup)
    welcome = WelcomeMethods(setup)
    welcome.validate_header()
    yield setup
