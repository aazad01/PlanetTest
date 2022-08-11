import pytest

from src.web.explorer import Environment
from src.web.explorer.page.methods.SearchBarMethods import SearchBarMethods
from src.web.account.page.methods.SignInMethods import SignInMethods


class TestSearch:

    def test_search_bar(self, setup, gen_test_data):
        signin = SignInMethods(setup)
        signin.enter_username(Environment.USERNAME)
        signin.click_next()
        signin.enter_password(Environment.PASSWORD)
        signin.click_submit()

        search = SearchBarMethods(setup)
        search.click_on_search()
