from src.helper.CustomWebElement import CustomWebElement


class SearchBar:
    SEARCH_LOCATOR = ".//button[@value='search-drawer']"
    SAVED_SEARCHES_LOCATOR = ".//button[@value='saved-searches-drawer']"
    FOLDERS_LOCATOR = ".//button[@value='folders-drawer']"
    ORDERS_LOCATOR = ".//button[@value='orders-drawer']"
    TASKS_LOCATOR = ".//button[@value='taskingDashboard']"

    def __init__(self, driver):
        self._driver = driver

    def search(self):
        return CustomWebElement.find_by_xpath(self._driver, SearchBar.SEARCH_LOCATOR)

    def saved_searches(self):
        return CustomWebElement.find_by_xpath(self._driver, SearchBar.SAVED_SEARCHES_LOCATOR)

    def folders(self):
        return CustomWebElement.find_by_xpath(self._driver, SearchBar.FOLDERS_LOCATOR)

    def orders(self):
        return CustomWebElement.find_by_xpath(self._driver, SearchBar.ORDERS_LOCATOR)

    def tasks(self):
        return CustomWebElement.find_by_xpath(self._driver, SearchBar.TASKS_LOCATOR)
