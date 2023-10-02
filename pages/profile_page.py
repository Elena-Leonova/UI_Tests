from pages.base_page import BasePage
from .locators import ProfilePageLocators


class ProfilePage(BasePage):
    def go_to_new_pet(self):
        go_to_new_pet = self.browser.find_element(*ProfilePageLocators.NEW_PET_LINK)
        go_to_new_pet.click()

    def go_to_edit(self):
        go_to_edit = self.browser.find_element(*ProfilePageLocators.EDIT_LINK)
        go_to_edit.click()

    def delete_exist_pet(self):
        go_to_delete_first_pet = self.browser.find_element(*ProfilePageLocators.DELETE_BUTTON_FIRST_PET)
        go_to_delete_first_pet.click()

    def confirm_yes_button(self):
        go_to_yes = self.browser.find_element(*ProfilePageLocators.CONFIRM_DELETE_YES)
        go_to_yes.click()

    def confirm_no_button(self):
        go_to_no = self.browser.find_element(*ProfilePageLocators.CONFIRM_DELETE_NO)
        go_to_no.click()

    def delete_all_pets(self):
        go_to_delete = self.browser.find_element(*ProfilePageLocators.DELETE_ALL_PETS)
        go_to_delete.click()


