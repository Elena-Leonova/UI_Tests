from .base_page import BasePage
from .locators import RegistrationPageLocators


class RegistrationPage(BasePage):

    def go_to_reg_login(self):
        reg_login = self.browser.find_element(*RegistrationPageLocators.REG_EMAIL)
        reg_login.send_keys("sasha@gmail.com")

    def go_to_reg_pass(self):
        reg_password = self.browser.find_element(*RegistrationPageLocators.REG_PASSWORD)
        reg_password.send_keys("2589")

    def go_to_conf_reg_pass(self):
        conf_reg_password = self.browser.find_element(*RegistrationPageLocators.REG_CONFIRM_PASSWORD)
        conf_reg_password.send_keys("2589")

    def submit_button(self):
        reg_button = self.browser.find_element(*RegistrationPageLocators.REG_BTN)
        reg_button.submit()
