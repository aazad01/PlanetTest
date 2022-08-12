from src.helper.CustomWebElement import CustomWebElement


class Account:
    WELCOME_LOCATOR = ".//h1[@data-testid='welcome!-page']"

    def __init__(self, driver):
        self._driver = driver

    def welcome(self):
        return CustomWebElement.find_by_xpath(self._driver, Account.WELCOME_LOCATOR)
