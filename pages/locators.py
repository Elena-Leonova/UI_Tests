from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#app > header > div > ul > li:nth-child(1) > a > span")
    REGISTRATION_LINK = (By.CSS_SELECTOR, "#app > header > div > ul > li:nth-child(2) > a")
    FILTER_BY_TYPE = (By.ID, "typesSelector")
    CHOOSE_CAT = (By.ID, "pv_id_2_1")
    FILTER_PET_NAME = (By.ID, "petName")


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")


class RegistrationPageLocators:
    REG_EMAIL = (By.ID, "login")
    REG_PASSWORD = (By.CSS_SELECTOR, "#password > input")
    REG_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#confirm_password > input")
    REG_BTN = (By.CLASS_NAME, "p-button-label")


class ProfilePageLocators:
    NEW_PET_LINK = (By.CSS_SELECTOR,
                    "#app > main > div > div > div.p-dataview-header > div > div:nth-child(1) > button")

    EDIT_LINK = (By.CSS_SELECTOR, "#app > main > div > div > div.p-dataview-content > div > div:nth-child(1) >"
                                  " div > div.product-list-action > button:nth-child(1) > span.p-button-label")
    DELETE_BUTTON_FIRST_PET = (By.CSS_SELECTOR, "#app > main > div > div > div.p-dataview-content > div > div:nth"
                                                "-child(1) > div > div.product-list-action > button.p-button."
                                                "p-component.p-button-danger")
    CONFIRM_DELETE_YES = (By.CSS_SELECTOR, "button[aria-label='Yes'] span[class='p-button-label']")

    CONFIRM_DELETE_NO = (By.CSS_SELECTOR, "button[aria-label='No'] span[class='p-button-label']")

    DELETE_ALL_PETS = (By.CSS_SELECTOR, "#app > main > div > div > div.p-dataview-header >"
                                        " div > div:nth-child(2) > button")


class CreateNewPetPageLocators:
    CREATE_NAME = (By.ID, "name")
    CREATE_AGE = (By.CSS_SELECTOR, "#age > input")
    CREATE_TYPE = (By.ID, "typeSelector")
    CHOOSE_TYPE_DOG = (By.ID, 'pv_id_4_0')
    CREATE_GENDER = (By.ID, "genderSelector")
    CHOOSE_GENDER_FEMALE = (By.ID, "pv_id_5_1")
    CREATE_SUBMIT_BTN = (By.CSS_SELECTOR, "#app > main > div > div > form > div > div.p-card-body > div.p-card-footer >"
                         " button.p-button.p-component.p-button-success")
    PROFILE_LINK = (By.CLASS_NAME, "p-menuitem-text")
