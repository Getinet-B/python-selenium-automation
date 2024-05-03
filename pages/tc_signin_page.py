from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TermsConditionSigninPage(BasePage):
    TC_LINK = (By.XPATH, "//a[text()='Target terms and conditions']")

    def open_sign_in_page(self):
        self.driver.get('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin')