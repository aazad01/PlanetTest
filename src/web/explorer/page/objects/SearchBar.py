from src.helper.CustomWebElement import CustomWebElement


class SearchBar:
    SEARCH_LOCATOR = ".//button[@value='search-drawer']"
    SAVED_SEARCHES_LOCATOR = ".//button[@value='saved-searches-drawer']"
    FOLDERS_LOCATOR = ".//button[@value='folders-drawer']"
    ORDERS_LOCATOR = ".//button[@value='orders-drawer']"
    TASKS_LOCATOR = ".//button[@value='taskingDashboard']"

    SEARCH_TEXTBOX_LOCATOR = ".//input[@data-qe='search-input']"
    DAILY_INTERVAL_LOCATOR = ".//button[@data-qe='daily-interval']"
    WEEKLY_INTERVAL_LOCATOR = ".//button[@data-qe='weekly-interval']"
    MONTHLY_INTERVAL_LOCATOR = ".//button[@data-qe='monthly-interval']"
    QUARTERLY_INTERVAL_LOCATOR = ".//button[@data-qe='quarterly-interval']"

    # DAILY
    FILTER_LOCATOR = ".//button[@data-qe='filters-button']"
    DATES_LOCATOR = ".//button[@data-qe='set-date-range-button']"
    SAVE_SEARCH_LOCATOR = ".//button[@data-qa='click-save-search-button']"

    # MONTHLY
    MONTHLY_SERIES_LOCATOR = ".//div[@data-qe='series-selector']"

    # SEARCH SUGGESTIONS
    SEARCH_SUGGESTIONS_LOCATOR = ".//div[@data-qe='search-suggestion']"

    RESULTS_LOCATOR = ".//div[@data-qe='result-list-item']"
    ITEM_COUNT_LOCATOR = ".//span[@data-qe='item-count']"
    ITEM_DATE_LOCATOR = ".//div[@data-qe='item-date']"
    ITEM_TYPE_LABEL_LOCATOR = ".//div[@data-qe='item-type-label']"
    PIXEL_RESOLUTION_LOCATOR = ".//div[@data-qe='item-pixel-resolution']"
    AREA_COVERAGE_LOCATOR = ".//div[@data-qe='area-coverage']"

    PARTIAL_INDICATOR_LOCATOR = ".//div[@data-qe='partial-rectification']"
    PURCHASE_LOCATOR = ".//button[@data-qe='result-item-access-button']"

    LOAD_MORE_LOCATOR = ".//button[@data-qe='load-more']"

    def __init__(self, driver):
        self._driver = driver

    def search(self):
        return CustomWebElement.find_by_xpath(self._driver, SearchBar.SEARCH_LOCATOR)

    def search_box(self):
        return CustomWebElement.find_by_xpath(self._driver, SearchBar.SEARCH_TEXTBOX_LOCATOR)

    def search_suggestions(self):
        return CustomWebElement.find_by_xpath(self._driver, SearchBar.SEARCH_SUGGESTIONS_LOCATOR)

    def results(self):
        return CustomWebElement.find_by_xpath(self._driver, SearchBar.RESULTS_LOCATOR)

    def saved_searches(self):
        return CustomWebElement.find_by_xpath(self._driver, SearchBar.SAVED_SEARCHES_LOCATOR)

    def folders(self):
        return CustomWebElement.find_by_xpath(self._driver, SearchBar.FOLDERS_LOCATOR)

    def orders(self):
        return CustomWebElement.find_by_xpath(self._driver, SearchBar.ORDERS_LOCATOR)

    def tasks(self):
        return CustomWebElement.find_by_xpath(self._driver, SearchBar.TASKS_LOCATOR)
