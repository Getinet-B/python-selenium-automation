from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

COLOR_CHOICE = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
COLOR_SELECTED = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='StyledHeaderWrapperDiv']")


@given('Open target {product_num} page')
def open_page(context, product_num):
    context.driver.get(f'https://www.target.com/p/{product_num}')
    sleep(8)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ["dark khaki", "black/gum", "stone/grey", "white/gum"] #Add all available colors here
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_CHOICE)  # [webelement1, webelement2, webelement3]
    for color in colors:
        color.click()

        # Wait for the color selection to update
        WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(COLOR_SELECTED))
        selected_color = context.driver.find_element(*COLOR_SELECTED).text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'


@then('Verify user can click on colors')
def click_on_colors(context):
    second_expected_colors = ["Blue Tint", "Denim Blue", "Marine", "Raven"]
    exact_colors = []


    color_types = context.driver.find_elements(*COLOR_CHOICE)  # [webelement1, webelement2, webelement3]
    for color in color_types:
        color.click()

        # Wait for the color selection to update
        WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(COLOR_SELECTED))
        selected_color = context.driver.find_element(*COLOR_SELECTED).text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        exact_colors.append(selected_color)
        print(exact_colors)

    assert second_expected_colors == exact_colors, f'Expected {second_expected_colors} did not match actual {exact_colors}'