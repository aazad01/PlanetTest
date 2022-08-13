import pytest

from src.web.explorer.page.methods.SaveBarMethods import SaveBarMethods
from src.web.explorer.page.methods.SearchBarMethods import SearchBarMethods


class TestDeleteSavedSearches:

    def test_delete_saved_searches(self, before_test):
        save = SaveBarMethods(before_test)
        save.click_on_search()
        items_0 = save.check_items()
        if items_0:
            save.delete_searches()
            items_1 = save.check_items()
            assert len(items_0) > len(items_1)
        else:
            pytest.skip("No saved searches to delete")
