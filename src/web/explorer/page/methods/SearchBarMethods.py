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
            search_box.send_input(search)
            search_box.click()
            time.sleep(1)
            # Click the first one
            self.search_suggestions().find().click()

    def verify_suggestions(self, search, saved=None):
        self.search_box().send_input(search)
        time.sleep(1)  # suggestions take a sec while to load
        suggestions = self.search_suggestions().find_all()

        if saved:
            for i in range(len(saved)):
                assert "Saved Search" in suggestions[i].get_text()

        def validation(elem, search):
            print(elem.get_text())
            search = search.split(",")[0]
            if search in elem.get_text():
                """  
                TODO: This doesn't work when states are 2 syllables
                Also when providing random words, search of business and point of interest are found
                """
                print(elem.get_text())
            else:
                assert search == elem.get_text()

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
        custom_name = custom_name[:20]
        """Custom naming breaks the search bar as there a odd behavior with words of small sizes.
            i.e Miami, Florida would return an address in Miami, before it hits the city
            This throws a curve ball in handling this issue.  
            Suspecting the search algo isn't placing weight on hierarchy of location name"""

        # TODO: name character limit check
        # TODO: Date Verification
        # TODO: return Satellite Constellation for validation

        def enter_new_title(name):
            self.name().clear()
            self.name().send_input(name)

        if is_saved_search:
            custom_name = f"{custom_name} UniqueID: {random_string}"
            enter_new_title(custom_name)
            self.update().click()
        elif create_new and saved_search:
            self.create_new_search().click()
            if self.name_error().is_displayed():
                assert "A saved search already exists with that name" in self.name_error().get_text()

                random_string = ''.join(random.choice(letters) for i in range(10))
                custom_name = f"{custom_name} Unique: {random_string}"
                enter_new_title(custom_name)
                self.create_new_search().click()
        else:
            custom_name = f"{custom_name} UniqueID: {random_string}"
            enter_new_title(custom_name)
            self.save().click()
        # FLAKY_WARNING: There is a slight timing issue here, where after the click the dialog doesn't go away quick enough
        time.sleep(1)
