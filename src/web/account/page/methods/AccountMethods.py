from src.web.account.page.objects.Account import Account


class AccountMethods(Account):

    def __init__(self, driver):
        super().__init__(driver)

    def verify_welcome(self):
        # self.welcome().find()
        assert self.welcome().get_text() == 'Welcome!'
