from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.ID, 'search')
SEARCH_BTN = (By.CSS_SELECTOR, "button[data-test='@web/Search/SearchButton']")
HEADER_LINKS = (By.XPATH, "//div[@data-test='resultsHeading']")


@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Search for {item}')
def expected_product(context, item):
    context.driver.find_element(*SEARCH_INPUT).send_keys(item)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(5)


@then('Verify search results are shown for {expected_product}')
def verify_search_results(context, expected_product):
    actual_text = context.driver.find_element(*HEADER_LINKS).text
    assert expected_product in actual_text, f'Error! Text {expected_product} not found in {actual_text}'
