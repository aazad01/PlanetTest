from selenium.webdriver import Keys

from src.web import Environment
from src.web.explorer.page.objects.FilterResults import FilterResults
from src.web.explorer.page.objects.SaveSearch import SaveSearch
from src.web.explorer.page.objects.SearchBar import SearchBar


class SearchBarMethods(SearchBar, FilterResults, SaveSearch):

    def __init__(self, driver):
        super().__init__(driver)
        super(SearchBar, self).__init__(driver)
        super(FilterResults, self).__init__(driver)
        if driver.current_url not in Environment.URL.EXPLORER:
            driver.get(Environment.URL.EXPLORER)

    def click_on_search(self, search, verify_saved=None, enter=False):
        if not self.search_sidebar().is_displayed():
            self.search().click()
        search_box = self.search_box()
        if search_box.get_attribute('value'):
            search_box.clear()
        search_box.send_input(search.split(',')[0])
        self.verify_suggestions(search[:5], verify_saved)
        search_box.clear()
        if enter:
            search_box.send_input(search + Keys.ENTER)

    def verify_suggestions(self, search, saved=None):
        suggestions = self.search_suggestions().find_all()

        if saved:
            for found_saved_filters in saved:
                assert "Saved Search" in suggestions[0].get_text()

        def validation(elem, search):
            print(elem.get_text())
            assert search in elem.get_text()

        result = list(map(
            lambda web_elements: validation(web_elements, search), self.search_suggestions().find_all()
        ))

    def verify_result(self):
        resutls = self.results().find_all()
