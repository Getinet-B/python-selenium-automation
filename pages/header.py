from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Header(BasePage):
    SEARCH_INPUT = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test = '@web/Search/SearchButton'] ")

    def search_product(self, item):
        self.input_text('item', *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)
