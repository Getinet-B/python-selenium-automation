from behave import given, when, then


@given('Open Target')
def open_target_main_page(context):
    context.app.tc_signin_page.open_target_main_page()


@when('click Sign In button')
def click_signin_button(context):
    context.app.tc_signin_page.click_signin_button()


@when('click Sign In button on side navigation menu')
def click_signin_side_navigation_menu(context):
    context.app.tc_signin_page.click_signin_side_navigation_menu()


@given('Open sign in page')
def open_signin_page(context):
    context.app.tc_signin_page.open_signin_page()


@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.tc_signin_page.get_current_window()


@when('Click on Target Terms and Conditions link')
def click_tc_link(context):
    context.app.tc_signin_page.click_tc_link()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.app.tc_signin_page.switch_to_new_window()


@then('Verify Terms and Conditions page is opened')
def verify_tc_opened(context):
    context.app.tc_signin_page.verify_tc_opened()


@then('close current page')
def close(context):
    context.app.target_app_page.close()


@then('Return to original window')
def return_to_original_window(context):
    context.app.tc_signin_page.switch_new_window_by_id(context.original_window)
