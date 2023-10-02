import time

import pytest

from pages.create_new_pet_page import CreateNewPetPage
from selenium.webdriver.common.by import By


@pytest.mark.smoke
@pytest.mark.regression
def test_create_new_pet_without_picture(browser, login):
    pets = browser.find_elements(By.CLASS_NAME, "col-12")
    quantity = len(pets)
    link = "http://34.141.58.52:8080/#/pet-new/pet"
    page = CreateNewPetPage(browser, link)
    page.open()
    page.go_to_name()
    page.go_to_age()
    page.go_to_type()
    page.choose_type_dog()
    page.go_to_gender()
    page.choose_gender_female()
    page.submit_btn()
    time.sleep(1)
    page.go_to_profile_link()
    time.sleep(3)
    browser.save_screenshot("create_new_pet_without_picture.png")
    pets = browser.find_elements(By.CLASS_NAME, "col-12")
    assert len(pets) != quantity
