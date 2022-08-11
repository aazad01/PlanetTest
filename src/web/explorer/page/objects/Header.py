class TopBar():
    LOGO_LOCATOR = ".//*[@id='logo-mini']"
    MENU_LOCATOR = ".//button[@data-qe='application-menu-button']"
    PROFILE_LOCATOR = ".//div[@data-qe='menu-avatar']"
    """
    Suggestion:
    - data-qe should probably be in the button element to keep standard
    """

    def __init__(self, driver):
        self._driver = driver