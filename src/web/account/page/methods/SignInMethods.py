from src.web.account.page.objects.SignIn import SignIn
from src.web.explorer import Environment


class SignInMethods(SignIn):

    def __init__(self, driver):
        super().__init__(driver)
        driver.get(Environment.URL.ACCOUNT)

    def enter_username(self, username):
        self.username().send_input(username)

    def enter_password(self, password):
        self.password().send_input(password)

    def click_next(self):
        self.next().click(required=False)

    def click_submit(self):
        self.submit().click()
