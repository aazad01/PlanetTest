from src.helper.CustomWebElement import CustomWebElement


class SaveSearchDialog:
    # Dialog Window

    HEADER = ".//h2"  # TODO: Needs a better locator
    SAVE_SEARCH_LOCATOR = ".//div[@data-qe='save-search-dialog']"
    CLOSE_LOCATOR = ".//button[@data-qe='dialog-close-button']"
    NAME_DIV_LOCATOR = ".//div[@data-qe='save-search-name']"
    NAME_LOCATOR = NAME_DIV_LOCATOR + "//input"
    NAME_ERROR_LOCATOR = NAME_DIV_LOCATOR + "//p"
    DATE_RANGE_LOCATOR = ".//div[@data-cy='save-search-dialog-folders']/div/span"
    NO_END_DATE_LOCATOR = ".//span[@data-qe='no-end-date']//input"
    SAVE_LOCATOR = ".//button[@data-cy='dialog-save-search-button']"  # Why is this data-cy?
    SAVE_NEW_SEARCH_LOCATOR = SAVE_SEARCH_LOCATOR + "//button[contains(text(),'Save as new search')]"
    UPDATE_LOCATOR = SAVE_SEARCH_LOCATOR + "//button[contains(text(),'Update')]"

    SAVED_SIDEBAR_LOCATOR = "//div[@data-qe='saved-searches-sidebar']"
    FILTER_BY_NAME_LOCATOR = ".//div[@data-qe='saved-search-text-filter']//input"

    def __init__(self, driver):
        self._driver = driver

    def header(self):
        return CustomWebElement.find_by_xpath(self._driver, SaveSearchDialog.HEADER)

    def saved_sidebar(self):
        return CustomWebElement.find_by_xpath(self._driver, SaveSearchDialog.SAVED_SIDEBAR_LOCATOR)

    def close(self):
        return CustomWebElement.find_by_xpath(self._driver, SaveSearchDialog.CLOSE_LOCATOR)

    def name(self):
        return CustomWebElement.find_by_xpath(self._driver, SaveSearchDialog.NAME_LOCATOR)

    def name_error(self):
        return CustomWebElement.find_by_xpath(self._driver, SaveSearchDialog.NAME_ERROR_LOCATOR)

    def date_range(self):
        return CustomWebElement.find_by_xpath(self._driver, SaveSearchDialog.DATE_RANGE_LOCATOR)

    def no_end_date(self):
        return CustomWebElement.find_by_xpath(self._driver, SaveSearchDialog.NO_END_DATE_LOCATOR)

    def save(self):
        return CustomWebElement.find_by_xpath(self._driver, SaveSearchDialog.SAVE_LOCATOR)

    def filter_search(self):
        return CustomWebElement.find_by_xpath(self._driver, SaveSearchDialog.FILTER_BY_NAME_LOCATOR)

    def update(self):
        return CustomWebElement.find_by_xpath(self._driver, SaveSearchDialog.UPDATE_LOCATOR)

    def create_new_search(self):
        return CustomWebElement.find_by_xpath(self._driver, SaveSearchDialog.SAVE_NEW_SEARCH_LOCATOR)

    def saved_search_dialog(self):
        return CustomWebElement.find_by_xpath(self._driver, SaveSearchDialog.SAVE_SEARCH_LOCATOR)
