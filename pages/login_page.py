from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL_INPUT    = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BTN     = (By.CSS_SELECTOR, "a.login-btn")  # targets <a> not <button id="login-btn">
    ERROR_MSG      = (By.CSS_SELECTOR, ".invalid-feedback, .alert, .error-msg")

    LOGIN_BTN   = (By.ID, "login-btn")
    USER_AVATAR = (By.XPATH, "//div[contains(@class,'account')]//img[@alt='Profile']")
    LOGOUT_LINK = (By.ID, "signout")

    def login(self, email, password):
        self.send_keys(self.EMAIL_INPUT, email)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BTN)

    def logout(self):
        self.click(self.USER_AVATAR)
        self.is_visible(self.LOGOUT_LINK, timeout=10)  # wait for dropdown to open
        signout = self.find_element(self.LOGOUT_LINK)
        self.driver.execute_script("arguments[0].click();", signout)

    def is_login_successful(self, timeout=20):
        try:
            WebDriverWait(self.driver, timeout).until(EC.none_of(EC.url_contains("sign-in")))
            return True
        except TimeoutException:
            return False

    def get_error_message(self):
        if self.is_visible(self.ERROR_MSG, timeout=8):
            return self.get_text(self.ERROR_MSG)
        return ""

    def is_error_displayed(self):
        return self.is_visible(self.ERROR_MSG, timeout=8)

    def is_logged_out(self):
        return self.is_visible(self.LOGIN_BTN, timeout=15)
