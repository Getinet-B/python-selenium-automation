from pages.base_page import BasePage
from selenium.webdriver.common.by import By
#from pages.cart_page import CartPage
from pages.header import Header, SignInPage
#from pages.help_page import HelpPage
from pages.main_page import MainPage
from pages.sign_in_page import SigninPage
from pages.search_result_page import SearchResultsPage
from pages.target_app_page import TargetAppPage
from pages.target_help import TargetHelpPage
from pages.tc_signin_page import TermsConditionSigninPage


class Application:
    def __init__(self, driver):
        self.base_page = BasePage(driver)
        #self.cart_page = CartPage(driver)
        self.header = Header(driver)
        #self.help_page = HelpPage(driver)
        self.main_page = MainPage(driver)
        self.search_result_page = SearchResultsPage(driver)
        self.sign_in_page = SigninPage(driver)
        self.target_app_page = TargetAppPage(driver)
        self.target_help = TargetHelpPage(driver)
        self.tc_signin_page = TermsConditionSigninPage(driver)
        self.email_input_locator = (By.ID, 'username')
        self.password_input_locator = (By.ID, 'password')
        self.sign_in_button_locator = (By.CSS_SELECTOR, 'button[data-test="SignInSubmitButton"]')

