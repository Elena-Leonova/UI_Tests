import time
import pytest
from pages.login_page import LoginPage
import requests as requests


@pytest.mark.smoke
def test_login(browser):
    link = "http://34.141.58.52:8080/#/login"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.submit_login_button()
    time.sleep(3)
    browser.save_screenshot("login.png")
    response = requests.get("http://34.141.58.52:8080/#/profile")
    status = response.status_code
    assert status == 200
