from selenium.webdriver import Keys

from src.web import Environment
from src.web.explorer.page.objects.FilterResults import FilterResults
from src.web.explorer.page.objects.SaveSearch import SaveSearch
from src.web.explorer.page.objects.SearchBar import SearchBar


class SaveBarMethods(SaveSearch):

    def __init__(self, driver):
        super().__init__(driver)
        if driver.current_url not in Environment.URL.EXPLORER:
            driver.get(Environment.URL.EXPLORER)

    def click_on_search(self, search=None):
        if not self.saved_sidebar().is_displayed():
            self.saved_searches().click()
        filter = self.filter_search()
        if filter.get_attribute('value'):
            filter.clear()
        if search:
            filter.send_input(search)

    def check_items(self):
        if len(self.items().find_all()) > 0:
            return list(map(lambda elm: elm.get_text(), self.items_title().find_all()))
        return []

    def validate_items_date(self):
        raise NotImplemented("Not complete")

    def validate_items_type(self):
        raise NotImplemented("Not complete")

    def delete_searches(self, all=False):
        if all:
            for elem in self.delete().find_all():
                elem.click()
