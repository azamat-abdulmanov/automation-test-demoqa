from pages.elements_page import TextBoxPage

URL = "https://demoqa.com/"


class TestElements:
    class TestTextBox:

        def test_test_box(self, driver):
            text_box_page = TextBoxPage(driver, URL)
            text_box_page.open()
            text_box_page.fill_all_fields()