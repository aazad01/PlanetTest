from src.web.explorer.page.objects.Welcome import Welcome


class WelcomeMethods(Welcome):

    def __init__(self, driver):
        super().__init__(driver)

    def validate_header(self):
        assert self.header().get_text() == 'Welcome to Planet Explorer!'
        self.skip().click()
