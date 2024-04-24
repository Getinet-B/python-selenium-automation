from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC



SEARCH_ITEM = (By.ID, 'search')
SEARCH_BTN = (By.CSS_SELECTOR, "button[data-test='@web/Search/SearchButton']")
LISTINGS = (By.CSS_SELECTOR, "div[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
ITEM_IMG = (By.CSS_SELECTOR, "[class*='ProductCardImage']")
ITEM_TITLE = (By.CSS_SELECTOR, "a[data-test='product-title']")


@given('Open main page')
def open_target_home(context):
    context.driver.get('https://www.target.com/')


@when('Search for {ring_doorbell_camera}')
def search_for_item(context, ring_doorbell_camera):
    context.driver.find_element(*SEARCH_ITEM).send_keys(ring_doorbell_camera)
    context.wait.until(
        EC.presence_of_element_located(SEARCH_BTN),
        message='Search button did not disappear.'
    )
    context.driver.find_element(*SEARCH_BTN).click()


@then('Verify that every product has a name and image')
def verify_name_image(context):
    top_five_items = context.driver.find_elements(*LISTINGS)[:4]

    for item in top_five_items:
        # Wait for the item title element to be present
        context.wait.until(
            EC.presence_of_element_located(ITEM_TITLE),
            message='Title did not appear.'
        )
        title = item.find_element(*ITEM_TITLE).text
        print(title)
        assert title, 'Item title is not shown'

        # Wait for the item image element to be present
        context.wait.until(
            EC.presence_of_element_located(ITEM_IMG),
            message='Image did not appear.'
        )
        image = item.find_element(*ITEM_IMG).get_attribute('src')
        assert image != '', 'Item image should not be empty'
