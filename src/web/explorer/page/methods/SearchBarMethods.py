import datetime
import string
import random
import time

from faker import Faker
from selenium.webdriver import Keys

from src.web import Environment
from src.web.explorer.page.objects.FilterResults import FilterResults
from src.web.explorer.page.objects.SaveSearchDialog import SaveSearchDialog
from src.web.explorer.page.objects.SearchBar import SearchBar


class SearchBarMethods(SearchBar, FilterResults, SaveSearchDialog):

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
        if enter:
            search_box.send_input(search + Keys.ENTER)
            search_box.click()
            # Click the first one
            self.search_suggestions().find().click()

    def verify_suggestions(self, search, saved=None):
        self.search_box().send_input(search)
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
        self.search_box().clear()

    def verify_result(self):
        resutls = self.results().find_all()

    def save_search_flow(self, custom_name="", saved_search=None, is_saved_search=False, create_new=False):
        self.save_search().click()
        # timestamp = str(datetime.datetime.now())
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(10))

        # TODO: name character limit check
        # TODO: Date Verification
        # TODO: return Satellite Constellation for validation
        if is_saved_search:
            name = self.name().get_attribute('value').split("UniqueID")[0]
            self.name().send_input(f"{name} {custom_name}")
            self.update().click()
        elif create_new and saved_search:
            self.create_new_search().click()
            if self.name_error().is_displayed():
                random_string = ''.join(random.choice(letters) for i in range(10))
                assert "A saved search already exists with that name" in self.name_error().get_text()

                custom_name = f"{self.name().get_attribute('value').split('UniqueID')[0]} UniqueID: {random_string}"
                self.name().clear()
                self.name().send_input(f"{custom_name}")
                self.create_new_search().click()

        else:
            if not custom_name:
                custom_name = f"UniqueID: {random_string}"
            self.name().send_input(f" {custom_name}")
            self.save().click()
        # FLAKY_WARNING: There is a slight timing issue here, where after the click the dialog doesn't go away quick enough
        time.sleep(1)
