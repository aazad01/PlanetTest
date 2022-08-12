import pytest

from src.web import Environment
from src.web.explorer.Flows import *
from src.web.explorer.page.methods.SaveBarMethods import SaveBarMethods
from src.web.explorer.page.methods.SearchBarMethods import SearchBarMethods
from src.web.account.page.methods.SignInMethods import SignInMethods
from src.web.explorer.page.methods.WelcomeMethods import WelcomeMethods


class TestSearchSuggestions:

    def test_search_bar(self, before_test, gen_test_data):
        search = SearchBarMethods(before_test)
        save = SaveBarMethods(before_test)
        save.click_on_search('')

        search.click_on_search(gen_test_data)
        search.verify_suggestions(gen_test_data)
