import time
import pytest
import requests

from pages.registration_page import RegistrationPage


@pytest.mark.smoke
def test_registration(browser):
    link = "http://34.141.58.52:8080/#/register"
    page = RegistrationPage(browser, link)
    page.open()
    page.go_to_reg_login()
    page.go_to_reg_pass()
    page.go_to_conf_reg_pass()
    page.submit_button()
    time.sleep(3)
    browser.save_screenshot('registration.png')
    response = requests.get("http://34.141.58.52:8080/#/profile")
    status = response.status_code
    assert status == 200
