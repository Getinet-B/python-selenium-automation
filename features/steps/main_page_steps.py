from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.header import Header
from behave import given, when, then
from selenium import webdriver


SEARCH_INPUT = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
HEADER = (By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")
HEADER_LINKS = (By.CSS_SELECTOR, "a[id*='utilityNav']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyledHeading']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")


@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')
    context.app.main_page.open_main()


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()  # always clicks on 1st Add to cart btn
    # Add multiple:
    # add_cart_btns = context.driver.find_elements(*ADD_TO_CART_BTN)
    # for btn in add_cart_btns[:5]:
    #     btn.click() # => will click on the first 5 buttons 1 by 1
    # add_cart_btns[4].click() # => will only click on the 5th Add to cart btn


@when('Store product name')
def store_product_name(context):
    context.wait.until(
        EC.presence_of_element_located(SIDE_NAV_PRODUCT_NAME),
        message='Product name not present on the page'
    )
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
    context.wait.until(
        EC.invisibility_of_element_located(SIDE_NAV_ADD_TO_CART_BTN),
        message='Side nav, Add to Cart button did not disappear'
    )


@then('Verify header in shown')
def verify_header_shown(context):
    context.driver.find_element(*HEADER)


@then('Verify header has {expected_amount} links')
def verify_header_links(context, expected_amount): # expected_amount = '5'
    expected_amount = int(expected_amount)   # '5' (str) => 5 (int)
    links = context.driver.find_elements(*HEADER_LINKS)
    assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'


@when('click Sign In Icon')
def click_sign_in(context):
    context.app.sign_in_page.click_sign_in()


@when('click Sign In from side navigation menu')
def nav_menu_click_sign_in(context):
    context.app.sign_in_page.nav_menu_click_sign_in()


@when('Input "{email}" and "{password}" on SignIn page')
def input_email_pw(context, email, password):
    context.app.sign_in_page.input_email_pw(email, password)


@when('click Sign in to log in')
def click_signin(context):
    context.app.sign_in_page.click_signin()

