from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from time import sleep


class SearchResultsPage(BasePage):
    SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    sleep(4)

    def verify_search_results(self, expected_item):
        actual_text = self.find_element(*self.SEARCH_RESULT_HEADER).text
        assert expected_item in actual_text, f'Error! Text {expected_item} not in {actual_text}'

