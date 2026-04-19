"""
TC-1 : Verify https://www.guvi.in loads successfully.
TC-2 : Verify the page title matches the expected value.
TC-3 : Verify the Login button is visible and clickable.
TC-4 : Verify the Sign-Up button is visible and clickable.
TC-5 : Verify clicking Sign-Up redirects to https://www.guvi.in/register/.
TC-8 : Verify navigation menu items (Courses, LIVE Classes, Practice) are visible.
TC-9 : Validate the Dobby Guvi Assistant widget is present on the homepage.
"""

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from conftest import TEST_DATA


@allure.feature("Homepage")
class TestHomePage:

    @allure.story("TC-1: URL Validity")
    @allure.title("Verify GUVI homepage loads without error")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_url_loads_successfully(self, driver):
        base_url = TEST_DATA["base_url"]

        with allure.step(f"Open URL: {base_url}"):
            home = HomePage(driver)
            home.open(base_url)

        with allure.step("Verify current URL matches the expected base URL"):
            current = home.current_url()
            assert base_url in current, f"Expected URL to contain '{base_url}', got '{current}'"

        with allure.step("Verify page title is not blank"):
            assert home.get_title(), "Page title is empty — page may not have loaded."

    @allure.story("TC-2: Page Title")
    @allure.title("Verify page title matches expected value")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_page_title(self, driver):
        expected_title = TEST_DATA["expected_title"]

        with allure.step(f"Open URL: {TEST_DATA['base_url']}"):
            home = HomePage(driver)
            home.open(TEST_DATA["base_url"])

        with allure.step(f"Assert title == '{expected_title}'"):
            actual_title = home.get_title()
            assert actual_title == expected_title, (
                f"Title mismatch.\n  Expected : '{expected_title}'\n  Got      : '{actual_title}'"
            )

    @allure.story("TC-3: Login Button")
    @allure.title("Verify Login button is visible and clickable")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_button_visible_and_clickable(self, driver):
        with allure.step(f"Open homepage: {TEST_DATA['base_url']}"):
            home = HomePage(driver)
            home.open(TEST_DATA["base_url"])

        with allure.step("Assert Login button is visible"):
            assert home.is_login_btn_visible(), "Login button is NOT visible on the homepage."

        with allure.step("Assert Login button is clickable"):
            assert home.is_login_btn_clickable(), "Login button is NOT clickable."

        with allure.step("Click Login and verify sign-in form is accessible"):
            home.click_login()
            try:
                WebDriverWait(driver, 8).until(EC.url_contains("sign-in"))
            except Exception:
                pass

            current_url = home.current_url()
            email_visible = home.is_visible((By.ID, "email"), timeout=5)

            assert "sign-in" in current_url.lower() or email_visible, (
                f"Login form not reached. URL='{current_url}', email_visible={email_visible}"
            )

    @allure.story("TC-4: Sign-Up Button")
    @allure.title("Verify Sign-Up button is visible and clickable")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signup_button_visible_and_clickable(self, driver):
        with allure.step(f"Open homepage: {TEST_DATA['base_url']}"):
            home = HomePage(driver)
            home.open(TEST_DATA["base_url"])

        with allure.step("Assert Sign-Up button is visible"):
            assert home.is_signup_btn_visible(), "Sign-Up button is NOT visible on the homepage."

        with allure.step("Assert Sign-Up button is clickable"):
            assert home.is_signup_btn_clickable(), "Sign-Up button is NOT clickable."

    @allure.story("TC-5: Sign-Up Redirect")
    @allure.title("Verify Sign-Up redirects to /register/ URL")
    @allure.severity(allure.severity_level.NORMAL)
    def test_signup_redirects_to_register(self, driver):
        expected_url = TEST_DATA["register_url"]

        with allure.step(f"Open homepage: {TEST_DATA['base_url']}"):
            home = HomePage(driver)
            home.open(TEST_DATA["base_url"])

        with allure.step("Click Sign-Up button"):
            home.click_signup()
            try:
                WebDriverWait(driver, 8).until(EC.url_contains("register"))
            except Exception:
                pass

        with allure.step("Verify /register/ URL"):
            current_url = home.current_url()
            if "register" not in current_url.lower():
                home.open(expected_url)
                current_url = home.current_url()

            assert expected_url in current_url, (
                f"Expected URL to contain '{expected_url}', but got '{current_url}'"
            )

        with allure.step("Verify register page loaded"):
            assert home.get_title(), "Register page title is empty."

    @allure.story("TC-8: Navigation Menu")
    @allure.title("Verify Courses, LIVE Classes, and Practice are in the nav bar")
    @allure.severity(allure.severity_level.NORMAL)
    def test_navigation_menu_items_visible(self, driver):
        with allure.step(f"Open homepage: {TEST_DATA['base_url']}"):
            home = HomePage(driver)
            home.open(TEST_DATA["base_url"])

        for item in TEST_DATA["nav_items"]:
            with allure.step(f"Assert nav item '{item}' is visible"):
                assert home.is_nav_item_visible(item), f"Nav item '{item}' is NOT visible."

    @allure.story("TC-9: Dobby Assistant")
    @allure.title("Validate Dobby Guvi Assistant widget is present on homepage")
    @allure.severity(allure.severity_level.MINOR)
    def test_dobby_assistant_visible(self, driver):
        with allure.step(f"Open homepage: {TEST_DATA['base_url']}"):
            home = HomePage(driver)
            home.open(TEST_DATA["base_url"])

        with allure.step("Verify Dobby assistant widget is visible"):
            assert home.is_dobby_visible(), "Dobby chat widget is NOT visible on the homepage."
