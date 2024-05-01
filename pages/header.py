from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class Header(BasePage):
    SEARCH_INPUT = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test = '@web/Search/SearchButton'] ")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button[id='addToCartButtonOrTextIdFor13397813']")
    SIDENAV_ADD_CART_BTN = (By.CSS_SELECTOR, "button[data-test='orderPickupButton']")
    CLICK_ON_CART = (By.CSS_SELECTOR, "use[href='/icons/assets/glyph/Cart.svg#Cart']")

    def search_product(self, item):
        self.input_text('item', *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)


class CartPage(BasePage):
    CLICK_ON_CART = (By.CSS_SELECTOR, "use[href='/icons/assets/glyph/Cart.svg#Cart']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button[id='addToCartButtonOrTextIdFor13397813']")
    SIDENAV_ADD_CART_BTN = (By.CSS_SELECTOR, "button[data-test='orderPickupButton']")

    # def click_cart(self):
    #     self.wait_until_clickable_click(*self.CLICK_ON_CART)
    #     self.save_screenshot('clicked_cart')

    def add_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BTN),
            'Add to cart button not clickable'
        ).click()

    def sidenav_add_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SIDENAV_ADD_CART_BTN),
            'Side Nav Add To Cart not Clickable'
        ).click()


class SignInPage(BasePage):
    email_input_locator = (By.XPATH, "//input[@inputmode='email']")
    password_input_locator = (By.XPATH, "//input[@id='password']")
    sign_in_button_locator = (By.XPATH, "//button[@id='login']")
    CLICK_SIGNIN_ICON = (By.CSS_SELECTOR, "span[class*='LinkText-sc-1e1g60c']")
    ACCOUNT_NAV_SIGNIN = (By.XPATH, "//*[@id='listaccountNav-signIn']")
    SIGNIN_ICON = (By.CSS_SELECTOR, "span[class*='LinkText']")
    SIDENAV_BTN = (By.XPATH, "//*[@id='listaccountNav-signIn']")
    SIGNIN_NAME = (By.CSS_SELECTOR, "span[class*='dZfgoT']")
    email = 'getbogale@zoo.com'
    password = '********'

    def sign_in(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SIGNIN_ICON),
                'SignIn button not clickable'
        ).click()

    def sidenav_sign_in(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SIDENAV_BTN),
            'Sidenav button not clickable'
        ).click()

    def click_sign_in(self):
        self.driver.find_element(*self.CLICK_SIGNIN_ICON).click()

    def nav_menu_click_sign_in(self):
        self.driver.find_element(*self.ACCOUNT_NAV_SIGNIN).click()

    def input_email_pw(self, email, password):
        sign_in_page = SignInPage(self.driver)
        sign_in_page.login(email, password)

    def click_signin(self):
        pass  # This step is covered in the SignInPage.login method

    def login(self, email, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.email_input_locator)
        ).send_keys(email)
        self.driver.find_element(*self.password_input_locator).send_keys(password)
        self.driver.find_element(*self.sign_in_button_locator).click()

    def verify_login(self):
        assert self.driver.find_element(*self.SIGNIN_NAME).is_displayed() is False


