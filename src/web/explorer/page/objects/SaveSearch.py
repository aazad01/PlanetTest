from src.helper.CustomWebElement import CustomWebElement


class SaveSearch:
    SAVED_SEARCHES_LOCATOR = ".//button[@value='saved-searches-drawer']"

    SAVED_SIDEBAR_LOCATOR = ".//div[@data-qe='saved-searches-sidebar']"
    FILTER_BY_NAME_LOCATOR = ".//div[@data-qe='saved-search-text-filter']//input"

    # Left Tab
    ITEMS_LOCATOR = ".//li[@data-qe='search-list-item']"
    ITEMS_TITLE_LOCATOR = ITEMS_LOCATOR + "//h6[@data-qe='search-list-item-title']"
    DELETE_LOACTOR = ".//button[@data-qe='menu-search-item-delete']"

    def __init__(self, driver):
        self._driver = driver

    def saved_searches(self):
        return CustomWebElement.find_by_xpath(self._driver, SaveSearch.SAVED_SEARCHES_LOCATOR)

    def saved_sidebar(self):
        return CustomWebElement.find_by_xpath(self._driver, SaveSearch.SAVED_SIDEBAR_LOCATOR)

    def items(self):
        return CustomWebElement.find_by_xpath(self._driver, SaveSearch.ITEMS_LOCATOR)

    def delete(self):
        return CustomWebElement.find_by_xpath(self._driver, SaveSearch.DELETE_LOACTOR)

    def items_title(self):
        return CustomWebElement.find_by_xpath(self._driver, SaveSearch.ITEMS_TITLE_LOCATOR)

    def filter_search(self):
        return CustomWebElement.find_by_xpath(self._driver, SaveSearch.FILTER_BY_NAME_LOCATOR)
