from selenium.webdriver import Keys

from src.web import Environment
from src.web.explorer.page.objects.FilterResults import FilterResults
from src.web.explorer.page.objects.SaveSearch import SaveSearch
from src.web.explorer.page.objects.SearchBar import SearchBar


class SaveBarMethods(SearchBar, SaveSearch):

    def __init__(self, driver):
        super().__init__(driver)
        super(SearchBar, self).__init__(driver)
        if driver.current_url not in Environment.URL.EXPLORER:
            driver.get(Environment.URL.EXPLORER)

    def click_on_search(self, search):
        if not self.search_sidebar().is_displayed():
            self.search().click()
        search_box = self.search_box()
        if search_box.get_attribute('value'):
            search_box.clear()
