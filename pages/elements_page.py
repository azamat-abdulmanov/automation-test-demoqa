from base_page import BasePage
from locators.elements_page_locators import TextBoxPageLocators


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys("Azamat")
        self.element_is_visible(self.locators.EMAIL).send_keys("ewer@mail.ru")
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys("Do this with facker")
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys("Do this with facker")
        self.element_is_visible(self.locators.SUBMIT).click()

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.FULL_NAME).text
        email = self.element_is_present(self.locators.FULL_NAME).text
        current_address = self.element_is_present(self.locators.CURRENT_ADDRESS).text
        permanent_address = self.element_is_present(self.locators.PERMANENT_ADDRESS).text

        return full_name, email, current_address, permanent_address
