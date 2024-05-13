from behave import given, when, then


@given('Open Help page for Print a receipt')
def open_target_help_receipt(context):
    context.app.target_help.open_target_help_receipt()


@when('Select Help topic {option}')
def select_topic(context, option):
    context.app.target_help.select_topic(option)


@then('Verify help "Drive Up & Order Pickup" page opened')
def verify_order_pickup_page_open(context):
    context.app.target_help.verify_gift_card_page_open()


@then('Verify help  page Print a receipt opened')
def verify_receipt_page_open(context):
    context.app.target_help.verify_receipt_page_open()


@then('Verify help {header} page opened')
def verify_target_help_header(context, header):
    context.app.target_help.verify_target_help_header(header)
