from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SigninPage(BasePage):
    SIGNIN_BTN = (By.XPATH, "//span[text()='Sign in']")
    SIDENAV_SIGNIN_BTN = (By.XPATH, "//*[@id='listaccountNav-signIn']")
    EMAIL_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.XPATH, "//span[text()='Sign in with password']")
    ERROR_MESSAGE = (By.XPATH, "//div[text()=\"We can't find your account.\"]")

    def __init__(self, driver):
        super().__init__(driver)

    def open_target_main_page(self):
        self.open('https://www.target.com/')

    def click_signin_button(self):
        self.click(*self.SIGNIN_BTN)

    def click_signin_side_navigation_menu(self):
        self.click(*self.SIDENAV_SIGNIN_BTN)

    def open_signin_page(self):
        self.driver.get('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin')

    def enter_incorrect_credentials(self, username, password):
        self.find_element(*self.EMAIL_INPUT).send_keys(username)
        self.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.click(*self.LOGIN_BUTTON)

    def verify_error_message_displayed(self):
        return self.wait_until_visible(*self.ERROR_MESSAGE)
