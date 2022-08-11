from src.helper.CustomWebElement import CustomWebElement
from src.web.explorer import Environment
from src.web.explorer.page.objects.SearchBar import SearchBar


class SearchBarMethods(SearchBar):

    def __init__(self, driver):
        super().__init__(driver)
        if driver.current_url not in Environment.URL.EXPLORER:
            driver.get(Environment.URL.EXPLORER)

    def click_on_search(self):
        self.search().click()
