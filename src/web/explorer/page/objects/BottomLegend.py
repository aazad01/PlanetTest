class BottomLegend:
    TIMELINE_LOCATOR = ".//div[@data-tour='timeline']"
    TIMELINE_SELECTOR_LOCATOR = ".//div[@data-qe='timeline-interval-selector']"

    def __init__(self, driver):
        self._driver = driver