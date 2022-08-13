from src.web import Environment
from src.web.explorer.Flows import *
from src.web.explorer.page.methods.SaveBarMethods import SaveBarMethods
from src.web.explorer.page.methods.SearchBarMethods import SearchBarMethods
from src.web.account.page.methods.SignInMethods import SignInMethods
from src.web.explorer.page.methods.WelcomeMethods import WelcomeMethods


class TestSearch:

    def test_search_and_save_new(self, before_test, valid_locations):
        search = SearchBarMethods(before_test)
        save = SaveBarMethods(before_test)
        # TODO - State acronym aren't handled properly
        save.click_on_search(search=valid_locations.split(',')[0])
        items_0 = save.check_items()
        search.click_on_search(valid_locations, enter=True)

        if not items_0:
            search.save_search_flow(custom_name=valid_locations, create_new=True)
        else:
            search.save_search_flow(custom_name=valid_locations, create_new=True, saved_search=items_0)
        save.click_on_search(search=valid_locations.split(',')[0])
        items_1 = save.check_items()
        assert len(items_1) > len(items_0)
        # TODO:  Probably clean up

    def test_search_and_update(self, before_test, valid_locations):
        search = SearchBarMethods(before_test)
        save = SaveBarMethods(before_test)
        save.click_on_search(search=valid_locations.split(',')[0])
        items_0 = save.check_items()
        if not items_0:
            search.click_on_search(valid_locations, enter=True)
            search.save_search_flow(custom_name=valid_locations)
            save.click_on_search(search=valid_locations.split(',')[0])
            items_0 = save.check_items()
        search.click_on_search(valid_locations, enter=True)
        search.save_search_flow(custom_name=valid_locations, is_saved_search=True)
        save.click_on_search(search=valid_locations.split(',')[0])
        items_1 = save.check_items()
        assert len(items_1) == len(items_0)
