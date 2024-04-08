from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target home page')
def open_target(context):
    context.driver.get('https://www.target.com/')

@when("click on 'Cart icon'")
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "use[href='/icons/assets/glyph/Cart.svg#Cart']").click()
    sleep(6)

@then('Verify cart is empty')
def verify_cart_empty_message(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    assert 'Your cart is empty' in actual_text, f'Error! Text Your cart is empty not in {actual_text}'