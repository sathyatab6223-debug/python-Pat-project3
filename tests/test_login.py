"""
TC-6 : Valid credentials   → user is redirected to dashboard.
TC-7 : Invalid credentials → error message is shown.
"""

import pytest
import allure
from pages.home_page import HomePage
from pages.login_page import LoginPage
from conftest import TEST_DATA


@allure.feature("Login")
class TestLogin:

    def _go_to_login_page(self, driver):
        home = HomePage(driver)
        home.open(TEST_DATA["base_url"])
        home.click_login()
        return LoginPage(driver)

    @allure.story("TC-6: Valid Login")
    @allure.title("Verify login with valid credentials redirects to dashboard")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_valid_login(self, driver):
        user = TEST_DATA["users"]["valid_user"]
        email    = user["email"]
        password = user["password"]

        with allure.step("Navigate to GUVI login page"):
            login_page = self._go_to_login_page(driver)

        with allure.step(f"Enter valid email: {email}"):
            login_page.send_keys(LoginPage.EMAIL_INPUT, email)

        with allure.step("Enter valid password"):
            login_page.send_keys(LoginPage.PASSWORD_INPUT, password)

        with allure.step("Click Sign In"):
            login_page.click(LoginPage.SUBMIT_BTN)

        with allure.step("Verify redirect away from sign-in page"):
            assert login_page.is_login_successful(), (
                f"Login did not succeed. Current URL: {login_page.current_url()}"
            )

    @allure.story("TC-7: Invalid Login")
    @allure.title("Verify invalid credentials show an error message")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_login(self, driver):
        user = TEST_DATA["users"]["invalid_user"]

        with allure.step("Navigate to GUVI login page"):
            login_page = self._go_to_login_page(driver)

        with allure.step(f"Enter invalid email: {user['email']}"):
            login_page.send_keys(LoginPage.EMAIL_INPUT, user["email"])

        with allure.step("Enter invalid password"):
            login_page.send_keys(LoginPage.PASSWORD_INPUT, user["password"])

        with allure.step("Click Sign In"):
            login_page.click(LoginPage.SUBMIT_BTN)

        with allure.step("Verify login did not succeed"):
            current_url = login_page.current_url()
            assert not any(r in current_url for r in ["/home", "/dashboard", "/profile", "/course"]), (
                f"Invalid login redirected to authenticated route: '{current_url}'"
            )

        with allure.step("Verify error message is displayed"):
            assert login_page.is_error_displayed(), "No error message shown after invalid login."

        with allure.step("Log error message text"):
            error_text = login_page.get_error_message()
            allure.attach(error_text, name="Error Message", attachment_type=allure.attachment_type.TEXT)
            assert error_text, "Error element found but text is empty."
