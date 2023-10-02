import time

import pytest
import requests
from selenium.webdriver.common.by import By

from pages.profile_page import ProfilePage


@pytest.mark.regression
def test_go_to_new_pet(browser, login):
    link = "http://34.141.58.52:8080/#/profile"
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_new_pet()
    time.sleep(2)
    browser.save_screenshot("go_to_new_pet.png")
    response = requests.get("http://34.141.58.52:8080/#/pet-new/pet")
    status = response.status_code
    assert status == 200


@pytest.mark.regression
def test_go_to_edit(browser, login):
    link = "http://34.141.58.52:8080/#/profile"
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_edit()
    time.sleep(2)
    browser.save_screenshot("go_to_edit.png")
    response = requests.get("http://34.141.58.52:8080/#/pet-edit")
    status = response.status_code
    assert status == 200


@pytest.mark.regression
def test_deletion_confirm_yes(browser, login):
    pets = browser.find_elements(By.CLASS_NAME, "col-12")
    quantity = len(pets)
    link = "http://34.141.58.52:8080/#/profile"
    page = ProfilePage(browser, link)
    page.open()
    page.delete_exist_pet()
    time.sleep(3)
    page.confirm_yes_button()
    time.sleep(3)
    browser.save_screenshot("delete_exist_pet.png")
    pets = browser.find_elements(By.CLASS_NAME, "col-12")
    assert len(pets) == quantity - 1


@pytest.mark.regression
def test_deletion_confirm_no(browser, login):
    pets = browser.find_elements(By.CLASS_NAME, "col-12")
    quantity = len(pets)
    link = "http://34.141.58.52:8080/#/profile"
    page = ProfilePage(browser, link)
    page.open()
    page.delete_exist_pet()
    time.sleep(3)
    page.confirm_no_button()
    time.sleep(3)
    browser.save_screenshot("delete_confirm_no.png")
    pets = browser.find_elements(By.CLASS_NAME, "col-12")
    assert len(pets) == quantity


@pytest.mark.skip
def test_deletion_confirm_no(browser, login):
    link = "http://34.141.58.52:8080/#/profile"
    page = ProfilePage(browser, link)
    page.open()
    page.delete_all_pets()
    time.sleep(3)
    page.confirm_yes_button()
    time.sleep(3)
    browser.save_screenshot("delete_all_pets.png")
    pets = browser.find_elements(By.CLASS_NAME, "col-12")
    assert len(pets) == 0
