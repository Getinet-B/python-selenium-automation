from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class TargetHelpPage(BasePage):
    HEADER_RECEIPT = (By.XPATH, "//h1[text()=' Print a receipt']")
    HEADER_ORDER_PICKUP = (By.XPATH, "//h1[text()=' Drive Up & Order Pickup']")
    HEADER = (By.XPATH, "//h1[text()=' {HEADER_STR}']")
    TOPIC_SELECTION = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")

    # Dynamic locators:
    def _get_locator(self, text):  # use _ if you don't want the method to be used outside of this class
        # HEADER = (By.XPATH, "//h1[text()=' {HEADER_STR}']") =>
        # (By.XPATH, "//h1[text()=' Returns']")
        return [self.HEADER[0], self.HEADER[1].replace('{HEADER_STR}', text)]

    def open_target_help_receipt(self):
        self.open('https://help.target.com/help/SubCategoryArticle?childcat=Print+a+receipt&parentcat=Orders+%26+Purchases&searchQuery=')

    def select_topic(self, option):
        topic_dd = self.find_element(*self.TOPIC_SELECTION)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(topic_dd))
        select = Select(topic_dd)
        select.select_by_value(option)

    def verify_receipt_page_open(self):
        self.wait_until_visible(*self.HEADER_RECEIPT)

    def verify_order_pickup_page_open(self):
        self.wait_until_visible(*self.HEADER_ORDER_PICKUP)

    def verify_target_help_header(self, header):
        locator = self._get_locator(header)
        self.wait_until_visible(*locator)
