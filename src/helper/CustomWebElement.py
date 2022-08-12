import platform

from selenium.common.exceptions import StaleElementReferenceException, ElementNotInteractableException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class CustomWebElement:
    max_retry_count = 3
    max_wait_time = 30
    poll_frequency = 1.0
    ignored_exceptions = StaleElementReferenceException

    def __init__(self, driver: WebDriver, locator_strategy=None, locator=None, web_element=None):
        self._driver = driver
        self._locator_strategy = locator_strategy
        self._locator = locator
        self._web_element = web_element

    @staticmethod
    def find_by_web_element(driver, web_element):
        return CustomWebElement(driver, web_element=web_element)

    @staticmethod
    def find_by_xpath(driver, locator):
        return CustomWebElement(driver, locator_strategy=By.XPATH, locator=locator)

    @staticmethod
    def find_by_id(driver, locator):
        return CustomWebElement(driver, locator_strategy=By.ID, locator=locator)

    @staticmethod
    def find_by_tag_name(driver, locator):
        return CustomWebElement(driver, locator_strategy=By.TAG_NAME, locator=locator)

    @staticmethod
    def find_by_name(driver, locator):
        return CustomWebElement(driver, locator_strategy=By.NAME, locator=locator)

    @staticmethod
    def find_by_link_text(driver, locator):
        return CustomWebElement(driver, locator_strategy=By.LINK_TEXT, locator=locator)

    @staticmethod
    def find_by_partial_link_text(driver, locator):
        return CustomWebElement(driver, locator_strategy=By.PARTIAL_LINK_TEXT, locator=locator)

    @staticmethod
    def find_by_class_name(driver, locator):
        return CustomWebElement(driver, locator_strategy=By.CLASS_NAME, locator=locator)

    @staticmethod
    def find_by_css_selector(driver, locator):
        return CustomWebElement(driver, locator_strategy=By.CSS_SELECTOR, locator=locator)

    @property
    def expected_condition(self):
        return EC

    @property
    def locator_strategy(self):
        return self._locator_strategy

    @property
    def locator(self):
        return self._locator

    def get_identifier(self):
        return tuple((self._locator_strategy, self._locator))

    def get_driver_wait(self, max_wait_time=None, poll_frequency=None, ignored_exceptions=None):
        if max_wait_time is None:
            max_wait_time = self.max_wait_time

        if poll_frequency is None:
            poll_frequency = self.poll_frequency

        if ignored_exceptions is None:
            ignored_exceptions = self.ignored_exceptions

        return WebDriverWait(self._driver, max_wait_time, poll_frequency, ignored_exceptions)

    def process_wait(self, wait, max_retry_count, ecs, until=True):
        ele = None
        for i in range(max_retry_count):
            try:
                for ec in ecs:
                    # If until then wait for expected_conditions (ecs) to be met
                    if until:
                        ele = wait.until(ec, f"until: exception -> {self._locator_strategy}: {self._locator}")
                    else:
                        # Else wait until they are not met
                        ele = wait.until_not(ec, f"until_not: exception -> {self._locator_strategy}: {self._locator}")
                return ele
            except BaseException:
                if i == max_retry_count - 1:
                    raise
        return ele

    def find(self, max_wait_time=max_wait_time, max_retry_count=max_retry_count, poll_frequency=poll_frequency,
             ignored_exceptions=None, ecs=None, until=True) -> WebElement:
        # If obj was created with an existing WebElement then we will not have locator - so simply return the element
        # passed in
        if self._web_element is not None:
            return self._web_element

        if ecs is None:
            ecs = []

        # Add default expected_condition to whatever list is passed in
        ecs.append(EC.presence_of_element_located(self.get_identifier()))
        return self.process_wait(self.get_driver_wait(max_wait_time=max_wait_time, poll_frequency=poll_frequency,
                                                      ignored_exceptions=ignored_exceptions),
                                 max_retry_count=max_retry_count, ecs=ecs)

    def find_all(self):
        return list(map(
            lambda ele: self.find_by_web_element(self._driver, ele),
            self._driver.find_elements(self._locator_strategy, self._locator)
        ))

    def wait_for_text(self, text, use_value_attr=False, max_wait_time=max_wait_time, should_exist=True, required=True):
        try:
            self.wait_to_appear(max_wait_time=max_wait_time)
            self.process_wait(self.get_driver_wait(max_wait_time=max_wait_time), self.max_retry_count, [
                self.expected_condition.text_to_be_present_in_element_attribute(
                    self.get_identifier(),
                    "value" if use_value_attr else "innerText",
                    text)],
                              until=should_exist)
            return True
        except BaseException:
            if required:
                raise
            else:
                return False

    def wait_for_attribute_value(self, expected_attr_value, max_wait_time=max_wait_time, should_exist=True,
                                 required=True):
        try:
            self.wait_to_appear(max_wait_time=max_wait_time)
            self.process_wait(self.get_driver_wait(max_wait_time=max_wait_time), self.max_retry_count, [
                self.expected_condition.text_to_be_present_in_element_attribute(
                    self.get_identifier(),
                    expected_attr_value[0],
                    expected_attr_value[1])],
                              until=should_exist)
            return True
        except BaseException:
            if required:
                raise
            else:
                return False

    def wait_to_appear(self, max_wait_time=max_wait_time, poll_frequency=poll_frequency, required=True, until=True):
        try:
            self.find(max_wait_time=max_wait_time, max_retry_count=1, poll_frequency=poll_frequency, until=until)
            return True
        except BaseException:
            if required:
                raise
            else:
                return False

    def wait_to_disappear(self, max_wait_time=max_wait_time, poll_frequency=poll_frequency, required=True):
        self.wait_to_appear(max_wait_time=max_wait_time, required=required, poll_frequency=poll_frequency, until=False)

    def wait_to_appear_and_disappear(self, max_wait_time_to_appear=5, max_wait_time_to_disappear=max_wait_time,
                                     required=False):
        self.wait_to_appear(max_wait_time=max_wait_time_to_appear, poll_frequency=0.5, required=False)
        self.wait_to_disappear(max_wait_time=max_wait_time_to_disappear)

    def click(self, use_js=False, expected_element=None, expected_attr_value=None, max_wait_time=None,
              should_exist=True, required=True):
        ele = self.find()
        self.get_driver_wait().until(self.expected_condition.visibility_of(ele))
        for i in range(self.max_retry_count):
            try:
                if use_js:
                    self._driver.execute_script("arguments[0].click();", ele)
                else:
                    ele.click()
                if expected_element is not None:
                    expected_element.find(max_retry_count=1, max_wait_time=max_wait_time, until=should_exist)
                elif not should_exist and expected_attr_value is None:
                    self.find(max_retry_count=1, max_wait_time=max_wait_time, until=should_exist)

                if expected_attr_value is not None:
                    ele = expected_element.get_identifier() if expected_element is not None else self.get_identifier()
                    self.process_wait(self.get_driver_wait(max_wait_time=max_wait_time), self.max_retry_count,
                                      [self.expected_condition.text_to_be_present_in_element_attribute(
                                          ele,
                                          expected_attr_value[0],
                                          expected_attr_value[1])],
                                      until=should_exist)
                return
            except BaseException:
                if i == self.max_retry_count - 1:
                    if required:
                        raise
                    else:
                        pass

    def click_js(self, expected_element=None, expected_attr_value=None, max_wait_time=None, should_exist=True,
                 required=True):
        self.click(use_js=True, expected_element=expected_element, expected_attr_value=expected_attr_value,
                   max_wait_time=max_wait_time, should_exist=should_exist, required=required)

    def send_input(self, text):
        if text is not None:
            self.find().send_keys(text)

    def clear(self):
        ele = self.find()
        try:
            if platform.platform().lower().find("mac") != -1:
                ele.send_keys(Keys.COMMAND + "a")
            else:
                ele.send_keys(Keys.CONTROL + "a")
            ele.send_keys(Keys.DELETE)
        except ElementNotInteractableException:
            ele.clear()

    def get_attribute(self, attribute):
        return self.find().get_attribute(attribute)

    def get_text(self, use_value_attr=False):
        return self.get_attribute("value") if use_value_attr else self.get_attribute("innerText")

    def get_location(self):
        return self.find().location

    def is_html5_validity(self):
        return bool(self._driver.execute_script("return arguments[0].validity.valid;", self.find()))

    def is_selected(self):
        return self.find().is_selected()

    def is_enabled(self, use_attribute=False):
        return str(self.get_attribute("enabled").lower()) == "true" if use_attribute else self.find().is_enabled()

    def is_displayed(self):
        return self.find().is_displayed()
