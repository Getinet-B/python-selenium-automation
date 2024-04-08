from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target page')
def open_target(context):
    context.driver.get('https://www.target.com/')

@when("click on 'Sign In'")
def click_signin(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
    sleep(6)

@when("click on 'Sign In' from navigation menu")
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//*[@id='listaccountNav-signIn']").click()
    sleep(6)

@then('Verify Sign In form opened')
def verify_sign_in_opens(context):
    actual_text = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    assert 'Sign into your Target account' in actual_text, f'Error! Text Sign into your Target account not in {actual_text}'