from src.helper.CustomWebElement import CustomWebElement


class Welcome:
    HEADER_LOCATOR = ".//h2[@data-qe='tour-dialog-title']"
    PARAGRAPH_LOCATOR = HEADER_LOCATOR + "/following-sibling::div/p"
    SKIP_LOCATOR = ".//button[@data-qe='skip-tour-button']"
    START_TOUR_LOCATOR = ".//button[@data-qe='start-tour-button']"

    def __init__(self, driver):
        self._driver = driver

    def header(self):
        return CustomWebElement.find_by_xpath(self._driver, Welcome.HEADER_LOCATOR)

    def paragraph(self):
        return CustomWebElement.find_by_xpath(self._driver, Welcome.PARAGRAPH_LOCATOR)

    def skip(self):
        return CustomWebElement.find_by_xpath(self._driver, Welcome.SKIP_LOCATOR)

    def start_tour(self):
        return CustomWebElement.find_by_xpath(self._driver, Welcome.START_TOUR_LOCATOR)
