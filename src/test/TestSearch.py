from src.web import Environment
from src.web.explorer.Flows import *
from src.web.explorer.page.methods.SearchBarMethods import SearchBarMethods
from src.web.account.page.methods.SignInMethods import SignInMethods
from src.web.explorer.page.methods.WelcomeMethods import WelcomeMethods


class TestSearch:

    def test_search_bar(self, setup, gen_test_data):
        flow(setup, search_for=gen_test_data)
