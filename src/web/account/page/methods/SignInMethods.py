from src.web.account.page.objects.SignIn import SignIn
from src.web import Environment


class SignInMethods(SignIn):

    def __init__(self, driver):
        super().__init__(driver)
        driver.get(Environment.URL.ACCOUNT)

    def login(self, username, password):
        self.username().send_input(username)
        self.next().click()
        self.password().send_input(password)
        self.submit().click()
