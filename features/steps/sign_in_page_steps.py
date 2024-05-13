from behave import given, when, then


@given('Open Target')
def open_target_main_page(context):
    context.app.sign_in_page.open_target_main_page()


@when('click Sign In button')
def click_signin_button(context):
    context.app.sign_in_page.click_signin_button()


@when('click Sign In button on side navigation menu')
def click_signin_side_navigation_menu(context):
    context.app.sign_in_page.click_signin_side_navigation_menu()


@given('Open sign in page')
def open_signin_page(context):
    context.app.sign_in_page.open_signin_page()


@when('Enter incorrect email "{username}" and password "{password}"')
def enter_incorrect_credentials(context, username, password):
    context.app.sign_in_page.enter_incorrect_credentials(username, password)


@when('Click login button')
def click_login_button(context):
    context.app.sign_in_page.click_login_button()


@then('Verify error message "{message}" is shown')
def verify_error_message(context, message):
    assert message == "We can't find your account.", f"Expected error message '{message}' not displayed"
