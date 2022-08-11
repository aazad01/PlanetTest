class CompareBar():
    COMPARE_LOCATOR = ".//button[@value='compare']"
    IMAGE_ENHANCEMENT_LOCATOR = ".//button[@value='colorenhance-drawer']"
    SPECIAL_ANALYSIS_LOCATOR = ".//button[@value='process-drawer']"
    STORIES_LOCATOR = ".//button[@value='stories']"

    def __init__(self, driver):
        self._driver = driver
