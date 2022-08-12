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

    def click_on_search(self, search):
        self.search().click()
        self.search_box().send_input(search[:5])
        self.verify_suggestions(search[:5])

    def verify_suggestions(self, search):
        assert all(
            list(map(lambda web_elements: search in web_elements.get_text(), self.search_suggestions().find_all())))
