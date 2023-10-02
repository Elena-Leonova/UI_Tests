from .base_page import BasePage
from .locators import CreateNewPetPageLocators


class CreateNewPetPage(BasePage):
    def go_to_name(self):
        name = self.browser.find_element(*CreateNewPetPageLocators.CREATE_NAME)
        name.send_keys("Koko")

    def go_to_age(self):
        age = self.browser.find_element(*CreateNewPetPageLocators.CREATE_AGE)
        age.send_keys("5")

    def go_to_type(self):
        go_to_type = self.browser.find_element(*CreateNewPetPageLocators.CREATE_TYPE)
        go_to_type.click()

    def choose_type_dog(self):
        choose_type = self.browser.find_element(*CreateNewPetPageLocators.CHOOSE_TYPE_DOG)
        choose_type.click()

    def go_to_gender(self):
        go_to_gender = self.browser.find_element(*CreateNewPetPageLocators.CREATE_GENDER)
        go_to_gender.click()

    def choose_gender_female(self):
        choose_gender_female = self.browser.find_element(*CreateNewPetPageLocators.CHOOSE_GENDER_FEMALE)
        choose_gender_female.click()

    def submit_btn(self):
        submit_btn = self.browser.find_element(*CreateNewPetPageLocators.CREATE_SUBMIT_BTN)
        submit_btn.submit()

    def go_to_profile_link(self):
        go_to_profile_link = self.browser.find_element(*CreateNewPetPageLocators.PROFILE_LINK)
        go_to_profile_link.click()
