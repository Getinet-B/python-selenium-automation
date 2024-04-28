from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
# #
# #
SEARCH_INPUT = (By.ID, 'search')
SEARCH_BTN = (By.CSS_SELECTOR, "button[data-test='@web/Search/SearchButton']")
HEADER_LINKS = (By.XPATH, "//div[@data-test='resultsHeading']")


@when('Search for {product}')
def expected_product(context, product):
   context.driver.find_element(*SEARCH_INPUT).send_keys(product)
   context.driver.find_element(*SEARCH_BTN).click()
   sleep(5)


@then(f'Verify search results are {expected_product}')
def verify_search_results(context, expected_product):
   actual_text = context.driver.find_element(*HEADER_LINKS).text
   assert expected_product in actual_text, f'Error! Text {expected_product} not found in {actual_text}'
