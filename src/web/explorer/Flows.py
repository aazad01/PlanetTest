from src.web import Environment
from src.web.account.page.methods.SignInMethods import SignInMethods
from src.web.account.page.methods.AccountMethods import AccountMethods
from src.web.explorer.page.methods.SearchBarMethods import SearchBarMethods
from src.web.explorer.page.methods.WelcomeMethods import WelcomeMethods


def flow(driver, search_for):
    signin = SignInMethods(driver)
    signin.login(Environment.USERNAME, Environment.PASSWORD)

    account = AccountMethods(driver)
    account.verify_welcome()

    search = SearchBarMethods(driver)
    welcome = WelcomeMethods(driver)
    welcome.validate_header()
    search.click_on_search(search_for)
