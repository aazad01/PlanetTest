from src.helper.CustomWebElement import CustomWebElement


class FilterResults:
    SEARCH_LOCATOR = ".//button[@value='search-drawer']"

    def __init__(self, driver):
        self._driver = driver
