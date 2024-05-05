from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TermsConditionSigninPage(BasePage):
    SIGNIN_BTN = (By.XPATH, "//span[text()='Sign in']")
    SIDENAV_SIGNIN_BTN = (By.XPATH, "//*[@id='listaccountNav-signIn']")
    TC_LINK = (By.XPATH, "//a[text()='Target terms and conditions']")

    def open_target_main_page(self):
        self.open('https://www.target.com/')

    def click_signin_button(self):
        self.click(*self.SIGNIN_BTN)

    def click_signin_side_navigation_menu(self):
        self.click(*self.SIDENAV_SIGNIN_BTN)

    def open_signin_page(self):
        self.driver.get('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin')

    def click_tc_link(self):
        self.click(*self.TC_LINK)

    def verify_tc_opened(self):
        self.verify_partial_url('terms-conditions/')