import json
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

with open("test_data.json", encoding="utf-8") as _f:
    TEST_DATA = json.load(_f)


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    chrome_driver = webdriver.Chrome(options=options)


    yield chrome_driver
    chrome_driver.quit()
    time.sleep(3)
