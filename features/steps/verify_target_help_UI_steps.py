from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


TARGET_HELP_TITLE = (By.CSS_SELECTOR, "h2[style*='color: #333']")
SEARCH_BAR = (By.CSS_SELECTOR, "input[title='search help']")
SEARCH_ICON = (By.CSS_SELECTOR, "input[alt='search']")
CUSTOMER_ASST_MENU = (By.CSS_SELECTOR, "div[class='grid_6']")
INFORMATION_MENU = (By.CSS_SELECTOR, "div[class='grid_4 boxSmallr txtAC bigbox2']")
BROWSE_HELP_PAGES = (By.XPATH, "//h2[text()='Browse all Help pages']")


@given('Open Target help page')
def open_target(context):
    context.driver.get('https://help.target.com/help')
    sleep(3)

@then("Verify 'Target Help' title is shown")
def verify_header_shown(context):
    context.driver.find_element(*TARGET_HELP_TITLE)


@then("Verify Search Bar is shown")
def verify_search_bar(context):
    context.driver.find_element(*SEARCH_BAR)


@then("Verify Search Icon is shown")
def verify_search_icon(context):
    context.driver.find_element(*SEARCH_ICON)
    sleep(3)


@then("Verify customer menu has {expected_containers} options")
def verify_customer_menu_options(context, expected_containers):  #expected_containers = 7
    expected_containers = int(expected_containers)
    options = context.driver.find_elements(*CUSTOMER_ASST_MENU)
    assert len(options) == expected_containers, f'Expected {expected_containers} options but got {len(options)}'


@then("Verify information menu has {expected_elements} box")
def verify_information_menu_options(context, expected_elements): #expected_element = 2
    expected_elements = int(expected_elements)
    box = context.driver.find_elements(*INFORMATION_MENU)
    assert len(box) == expected_elements, f'Expected {expected_elements} box but got {len(box)}'


@when("Verify 'Browse all Help pages' is shown")
def verify_browse_all_help_pages(context):
    context.driver.find_element(*BROWSE_HELP_PAGES)
    sleep(3)