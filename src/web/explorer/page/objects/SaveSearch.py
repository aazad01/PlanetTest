from src.helper.CustomWebElement import CustomWebElement


class SaveSearch:
    # Dialog Window
    HEADER = ".//h2"  # TODO: Needs a better locator
    CLOSE_LOCATOR = ".//button[@data-qe='dialog-close-button']"
    NAME_LOCATOR = ".//div[@data-qe='save-search-name']//input"
    DATE_RANGE_LOCATOR = ".//div[@data-cy='save-search-dialog-folders']/div/span"
    NO_END_DATE_LOCATOR = ".//span[@data-qe='no-end-date']//input"
    SAVE_LOCATOR = ".//button[@data-cy='dialog-save-search-button']"  # Why is this data-cy?

    # Left Tab
    ITEMS_LOCATOR = ".//li[@data-qe='search-list-item']"
    DELETE_LOACTOR = ".//button[@data-qe='menu-search-item-delete']"

    def __init__(self, driver):
        self._driver = driver

    def header(self):
        return CustomWebElement.find_by_xpath(self._driver, SaveSearch.HEADER)

    def close(self):
        return CustomWebElement.find_by_xpath(self._driver, SaveSearch.CLOSE_LOCATOR)

    def name(self):
        return CustomWebElement.find_by_xpath(self._driver, SaveSearch.NAME_LOCATOR)

    def date_range(self):
        return CustomWebElement.find_by_xpath(self._driver, SaveSearch.DATE_RANGE_LOCATOR)

    def no_end_date(self):
        return CustomWebElement.find_by_xpath(self._driver, SaveSearch.NO_END_DATE_LOCATOR)

    def save(self):
        return CustomWebElement.find_by_xpath(self._driver, SaveSearch.SAVE_LOCATOR)

    def items(self):
        return CustomWebElement.find_by_xpath(self._driver, SaveSearch.ITEMS_LOCATOR)

    def delete(self):
        return CustomWebElement.find_by_xpath(self._driver, SaveSearch.DELETE_LOACTOR)

