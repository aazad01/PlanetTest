from src.helper.CustomWebElement import CustomWebElement


class SignIn:
    USERNAME_LOCATOR = ".//input[@id='idp-discovery-username']"
    REMEMBER_ME_LOCATOR = ".//input[@id='input47']"
    NEXT_LOCATOR = ".//input[@id='idp-discovery-submit']"

    PASSWORD_LOCATOR = ".//input[@id='okta-signin-password']"
    SIGIN_LOCATOR = ".//input[@id='okta-signin-submit']"

    def __init__(self, driver):
        self._driver = driver

    def username(self):
        return CustomWebElement.find_by_xpath(self._driver, SignIn.USERNAME_LOCATOR)

    def remember_me(self):
        return CustomWebElement.find_by_xpath(self._driver, SignIn.REMEMBER_ME_LOCATOR)

    def next(self):
        return CustomWebElement.find_by_xpath(self._driver, SignIn.NEXT_LOCATOR)

    def password(self):
        return CustomWebElement.find_by_xpath(self._driver, SignIn.PASSWORD_LOCATOR)

    def submit(self):
        return CustomWebElement.find_by_xpath(self._driver, SignIn.SIGIN_LOCATOR)
