from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TargetAppPage(BasePage):
    PP_LINK = (By.XPATH, "//a[text()='Privacy policy']")

    def open_target_app(self):
        self.driver.get('https://www.target.com/c/target-app/')

    def click_pp_link(self):
        self.click(*self.PP_LINK)

    def verify_pp_opened(self):
        self.verify_partial_url('target-privacy-policy/')