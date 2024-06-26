from base_page import BasePage
from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.FULL_NAME).text
        email = self.element_is_present(self.locators.FULL_NAME).text
        current_address = self.element_is_present(self.locators.CURRENT_ADDRESS).text
        permanent_address = self.element_is_present(self.locators.PERMANENT_ADDRESS).text

        return full_name, email, current_address, permanent_address
