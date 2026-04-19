from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    LOGIN_BTN  = (By.ID, "login-btn")
    SIGNUP_BTN = (By.XPATH, '//button[normalize-space(text())="Sign up"]')

    # Nav items are <p class="menu-hover"> tags, not <a> tags
    NAV_COURSES      = (By.XPATH, '//p[contains(@class,"menu-hover") and contains(text(),"Courses")]')
    NAV_LIVE_CLASSES = (By.XPATH, '//p[contains(@class,"menu-hover") and contains(text(),"LIVE")]')
    NAV_PRACTICE     = (By.XPATH, '//p[contains(@class,"menu-hover") and contains(text(),"Practice")]')

    DOBBY_WIDGET     = (By.XPATH, '//span[contains(@class,"zsiq-chat-icn")]')

    def click_login(self):
        self.click(self.LOGIN_BTN)

    def click_signup(self):
        self.click(self.SIGNUP_BTN)

    def is_login_btn_visible(self):
        return self.is_visible(self.LOGIN_BTN)

    def is_login_btn_clickable(self):
        return self.is_clickable(self.LOGIN_BTN)

    def is_signup_btn_visible(self):
        return self.is_visible(self.SIGNUP_BTN)

    def is_signup_btn_clickable(self):
        return self.is_clickable(self.SIGNUP_BTN)

    def is_nav_item_visible(self, item_text):
        locator = (By.XPATH, f'//p[contains(@class,"menu-hover") and contains(text(),"{item_text}")]')
        return self.is_visible(locator)

    def is_dobby_visible(self):
        return self.is_present(self.DOBBY_WIDGET, timeout=15)
