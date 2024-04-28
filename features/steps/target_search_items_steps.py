from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


LISTINGS = (By.CSS_SELECTOR, "div[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
ITEM_IMG = (By.CSS_SELECTOR, "[class*='ProductCardImage']")
ITEM_TITLE = (By.CSS_SELECTOR, "a[data-test='product-title']")


@given('Open main page')
def open_target_home(context):
    context.driver.get('https://www.target.com/')


@then('Verify that every product has a name and image')
def verify_name_image(context):

    context.driver.execute_script("window.scrollBy(0, 2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0, 2000)", "")

    top_four_items = context.driver.find_elements(*LISTINGS)[:4]

    for item in top_four_items:
        context.wait.until(
            EC.presence_of_element_located(ITEM_TITLE),
            message='Title did not appear.'
        )
        title = item.find_element(*ITEM_TITLE).text
        print(title)
        assert title != '', 'Item title is not shown'
        image = item.find_element(*ITEM_IMG)
        assert image != '', 'Item image should not be empty'
