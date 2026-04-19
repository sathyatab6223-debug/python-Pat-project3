"""
TC-10 : Log in with valid credentials, click Logout,
        and verify the user is returned to the homepage.
"""

import pytest
import allure
from pages.home_page import HomePage
from pages.login_page import LoginPage
from conftest import TEST_DATA


@allure.feature("Logout")
class TestLogout:

    @allure.story("TC-10: Logout")
    @allure.title("Verify user can logout and is redirected to homepage")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_logout(self, driver):
        user = TEST_DATA["users"]["valid_user"]
        email    = user["email"]
        password = user["password"]

        if not email or not password:
            pytest.skip("Valid credentials not provided in test_data.json.")

        with allure.step("Open homepage and navigate to login"):
            home = HomePage(driver)
            home.open(TEST_DATA["base_url"])
            home.click_login()
            login_page = LoginPage(driver)

        with allure.step("Login with valid credentials"):
            login_page.login(email, password)

        with allure.step("Verify login successful"):
            assert login_page.is_login_successful(), (
                f"Pre-condition failed: login unsuccessful. URL: {login_page.current_url()}"
            )

        with allure.step("Click avatar and logout"):
            login_page.logout()

        with allure.step("Verify user is logged out"):
            assert login_page.is_logged_out(), (
                f"Logout failed. Current URL: {login_page.current_url()}"
            )
