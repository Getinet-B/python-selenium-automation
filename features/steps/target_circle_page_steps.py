from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


CIRCLE_PAGE = (By.CSS_SELECTOR, "image[href*='LogoTargetCircle']")
BENEFIT_CELLS = (By.CSS_SELECTOR, "div[class*='CellItemContainer']")
SEARCH_INPUT = (By.CSS_SELECTOR, "#search")
SEARCH_BTN = (By.CSS_SELECTOR, "button[data-test='@web/Search/SearchButton']")
ADD_BUTTON = (By.CSS_SELECTOR, "button[class*='ButtonPrimary']")
SIDE_ADD_BTN = (By.CSS_SELECTOR, "button[aria-label*='Add to cart']")
CHECK_CART = (By.CSS_SELECTOR, "button[data-test*='protectYourPurchasesButton']")
VIEW_CART = (By.CSS_SELECTOR, "a[data-test*='viewCartButton']")
VERIFY_ITEM = (By.XPATH, "//h2[text()='Order summary']")


@given('Open Target Circle page')
def open_target_circle_page(context):
    context.driver.get('https://www.target.com/circle')
    sleep(3)

@then('Verify the right circle page')
def verify_right_page(context):
    context.wait.until(
        EC.presence_of_element_located(CIRCLE_PAGE),
        message='The right Circle page is not present.'
    )
    context.driver.find_element(*CIRCLE_PAGE)


@then('Verify benefit cells has {expected_total} cells')
def verify_benefit_cells(context, expected_total):
    expected_total = int(expected_total)
    context.wait.until(
        EC.presence_of_element_located(BENEFIT_CELLS),
        message='The benefit cells does not have the expected total number of cells.'
    )
    cells = context.driver.find_elements(*BENEFIT_CELLS)
    print(cells)
    assert len(cells) == expected_total, f'Expected {expected_total} cells but got {len(cells)}'


@then("Search for 'air fryer'")
def search_air_fryer(context):
    context.wait.until(
        EC.presence_of_element_located(SEARCH_INPUT),
        message="'air fryer' is not present"
    )
    context.driver.find_element(*SEARCH_INPUT).send_keys('air_fryer')
    context.wait.until(
        EC.presence_of_element_located(SEARCH_BTN),
        message='Search button did not disappear'
    )
    context.driver.find_element(*SEARCH_BTN).click()


@then("add 'air fryer' to cart")
def add_to_cart(context):
    context.wait.until(
        EC.presence_of_element_located(ADD_BUTTON),
        message='Add to Cart button did not disappear'
    )
    context.driver.find_element(*ADD_BUTTON).click()


@then('add to cart from the side menu')
def add_cart_side_menu(context):
    context.wait.until(
        EC.presence_of_element_located(SIDE_ADD_BTN),
        message='Side nav, Add to Cart button did not disappear'
    )
    context.driver.find_element(*SIDE_ADD_BTN).click()
    context.driver.find_element(*CHECK_CART).click()
    context.wait.until(
        EC.presence_of_element_located(VIEW_CART),
        message='View cart button did not disappear'
    )
    context.driver.find_element(*VIEW_CART).click()


@when('Verify purchased item is in cart')
def verify_air_fryer_added(context):
    context.wait.until(
        EC.presence_of_element_located(VERIFY_ITEM),
        message='Verify item is not in cart'
    )
    actual_text = context.driver.find_element(*VERIFY_ITEM).text
    print(actual_text)
    assert 'Order summary' in actual_text, f'Error! Text Order summary not in {actual_text}'
