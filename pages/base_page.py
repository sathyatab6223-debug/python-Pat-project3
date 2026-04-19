import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException


class BasePage:

    TIMEOUT = 15

    def __init__(self, driver):
        self.driver = driver

    def _wait(self, timeout=None):
        return WebDriverWait(self.driver, timeout or self.TIMEOUT)

    def find_element(self, locator):
        return self._wait().until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        self._wait().until(EC.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self._wait().until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        """Retries on StaleElementReferenceException caused by Qwik DOM re-hydration."""
        for attempt in range(3):
            try:
                element = self._wait().until(EC.element_to_be_clickable(locator))
                element.clear()
                element.send_keys(text)
                return
            except StaleElementReferenceException:
                if attempt == 2:
                    raise
                time.sleep(0.5)

    def get_text(self, locator):
        return self.find_element(locator).text

    def is_present(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def is_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def is_clickable(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def current_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def open(self, url):
        self.driver.get(url)
