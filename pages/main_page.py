import time
from .locators import MainPageLocators
from .base_page import BasePage
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_registration_page(self):
        registration_link = self.browser.find_element(*MainPageLocators.REGISTRATION_LINK)
        registration_link.click()

    def filter_by_type(self):
        drop_down = self.browser.find_element(*MainPageLocators.FILTER_BY_TYPE)
        drop_down.click()
        time.sleep(2)

    def choose_type_cat(self):
        choose_cat = self.browser.find_element(*MainPageLocators.CHOOSE_CAT)
        choose_cat.click()

    def filter_by_pet_name(self):
        filter_by_pet_name = self.browser.find_element(*MainPageLocators.FILTER_PET_NAME)
        filter_by_pet_name.send_keys("Atos", Keys.ENTER)
