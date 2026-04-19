# Automated Testing of GUVI EdTech Platform

Automated UI test suite for [https://www.guvi.in](https://www.guvi.in) built with **Python + Selenium WebDriver + pytest + Allure**.

---

## Project Structure

```
python-Pat-project3/
├── pages/
│   ├── base_page.py        # Shared WebDriver helper methods (BasePage)
│   ├── home_page.py        # GUVI homepage — login btn, signup btn, nav, Dobby
│   └── login_page.py       # Login form, error detection, logout flow
├── tests/
│   ├── test_homepage.py    # TC-1, TC-2, TC-3, TC-4, TC-5, TC-8, TC-9
│   ├── test_login.py       # TC-6 (valid login), TC-7 (invalid login)
│   └── test_logout.py      # TC-10 (logout)
├── conftest.py             # pytest fixtures — Chrome driver, TEST_DATA
├── pytest.ini              # pytest config — paths, allure dir, markers
├── test_data.json          # Centralised test inputs (URLs, titles, credentials)
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## Test Cases Covered

| TC    | Scenario                                        | File                  |
|-------|-------------------------------------------------|-----------------------|
| TC-1  | Verify URL loads without error                  | test_homepage.py      |
| TC-2  | Verify page title matches expected value        | test_homepage.py      |
| TC-3  | Login button visible + clickable → login page   | test_homepage.py      |
| TC-4  | Sign-Up button visible + clickable              | test_homepage.py      |
| TC-5  | Sign-Up redirects to /register/                 | test_homepage.py      |
| TC-6  | Valid credentials → dashboard redirect          | test_login.py         |
| TC-7  | Invalid credentials → error message shown       | test_login.py         |
| TC-8  | Courses / LIVE Classes / Practice visible       | test_homepage.py      |
| TC-9  | Dobby AI Assistant widget present               | test_homepage.py      |
| TC-10 | Logout → redirect to homepage / login           | test_logout.py        |

---

## Prerequisites

- Python 3.9+
- Google Chrome (latest)
- ChromeDriver is managed automatically via `webdriver-manager`

---

## Setup

```bash
# 1. Clone / download the project
cd E:\python-Pat-project3

# 2. Create and activate a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt
```

---

## Add Your Credentials

Open `test_data.json` and fill in your GUVI account details:

```json
"valid_user": {
    "email": "your_email@example.com",
    "password": "your_password"
}
```

> TC-6 (valid login) and TC-10 (logout) will be **skipped** automatically if credentials are left empty — all other tests will still run.

---

## Running Tests

```bash
# Run the full test suite
pytest

# Run a specific test file
pytest tests/test_homepage.py

# Run a specific test case
pytest tests/test_homepage.py::TestHomePage::test_page_title

# Run with verbose output (no Allure)
pytest -v --no-header --alluredir=allure-results
```

---

## Generate Allure Report

```bash
# 1. Run tests (produces allure-results/)
pytest

# 2. Generate HTML report
allure generate allure-results -o allure-report --clean

# 3. Open in browser
allure open allure-report
```

---

## Design Highlights

| Principle        | Implementation                                                          |
|------------------|-------------------------------------------------------------------------|
| OOP / POM        | `BasePage` → `HomePage`, `LoginPage` — each page has its own class     |
| Exception handling | `is_visible()` / `is_clickable()` catch `TimeoutException` silently   |
| Credentials guard | TC-6 / TC-10 call `pytest.skip()` when credentials are empty          |
| Allure steps     | Every test step wrapped in `with allure.step(...)` for rich reports    |
| Auto-close       | `driver.quit()` always runs in the `yield` fixture teardown            |
| Reusable locators| All locators defined as class-level constants, reused across tests      |
