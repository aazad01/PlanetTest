import pytest

from src.web import Environment
from src.web.explorer.Flows import *
from src.web.explorer.page.methods.SaveBarMethods import SaveBarMethods
from src.web.explorer.page.methods.SearchBarMethods import SearchBarMethods
from src.web.account.page.methods.SignInMethods import SignInMethods
from src.web.explorer.page.methods.WelcomeMethods import WelcomeMethods


class TestSearchSuggestions:

    def test_search_bar(self, before_test, valid_locations):
        search = SearchBarMethods(before_test)
        save = SaveBarMethods(before_test)
        save.click_on_search(search=valid_locations.split(',')[0])
        items = save.check_items()
        search.click_on_search(valid_locations, verify_saved=items)
        search.verify_suggestions(search=valid_locations, saved=items)

    def test_search_bar_invalid(self, before_test, invalid_locations):
        search = SearchBarMethods(before_test)
        search.click_on_search(search=invalid_locations)
        search.verify_suggestions(search=invalid_locations)
