import time
import pytest
import requests
from pages.main_page import MainPage


@pytest.mark.smoke
def test_go_to_login_page(browser):
    link = "http://34.141.58.52:8080/#/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    browser.save_screenshot('go_to_login.png')
    response = requests.get("http://34.141.58.52:8080/#/login")
    status = response.status_code
    assert status == 200


@pytest.mark.smoke
def test_go_to_registration_page(browser):
    link = "http://34.141.58.52:8080/#/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_registration_page()
    browser.save_screenshot('go_to_registration.png')
    response = requests.get("http://34.141.58.52:8080/#/register")
    status = response.status_code
    assert status == 200


@pytest.mark.regression
def test_filter_by_type(browser):
    link = "http://34.141.58.52:8080/#/"
    page = MainPage(browser, link)
    page.open()
    page.filter_by_type()
    page.choose_type_cat()
    time.sleep(2)
    browser.save_screenshot('filter_by_type_cat.png')
    response = requests.get("http://34.141.58.52:8080/#/")
    status = response.status_code
    assert status == 200


@pytest.mark.regression
def test_filter_by_pet_name(browser):
    link = "http://34.141.58.52:8080/#/"
    page = MainPage(browser, link)
    page.open()
    page.filter_by_pet_name()
    time.sleep(2)
    browser.save_screenshot('filter_by_pet_name.png')
    response = requests.get("http://34.141.58.52:8080/#/")
    status = response.status_code
    assert status == 200
