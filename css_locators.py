from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# CSS locators for 'amazon' logo
driver.find_element(By.CSS_SELECTOR, "i[class*='a-icon-logo']")
driver.find_element(By.CSS_SELECTOR, "[aria-label='Amazon']")
driver.find_element(By.CSS_SELECTOR, "i[role='img']")

# CSS locators for 'Creat account' header
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

# CSS locators for 'Your name' section
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")
driver.find_element(By.CSS_SELECTOR, "input[type='text'][autocomplete='name'][placeholder='First and last name']")
driver.find_element(By.CSS_SELECTOR, "[name='customerName']")
driver.find_element(By.CSS_SELECTOR, "input.a-input-text.a-span12.auth-autofocus")

# CSS locators for 'Mobile number or email' section
driver.find_element(By.CSS_SELECTOR, "input#ap_email")
driver.find_element(By.CSS_SELECTOR, "input[type='email'][autocomplete='email'][name='email']")
driver.find_element(By.CSS_SELECTOR, "input.a-input-text.a-span12.a-spacing-micro")
driver.find_element(By.CSS_SELECTOR, "[data-validation-id='email']")

# CSS locators for 'Password' section
driver.find_element(By.CSS_SELECTOR, "#ap_password")
driver.find_element(By.CSS_SELECTOR, "input[autocomplete='new-password'][placeholder='At least 6 characters'][type='password']")
driver.find_element(By.CSS_SELECTOR, "input[name='password']")
driver.find_element(By.CSS_SELECTOR, "input.auth-require-password-validation")

# CSS locators for 'Passwords must be at least 6 characters' section
driver.find_element(By.CSS_SELECTOR, "div.a-alert")

# CSS locators for 'Re-enter password' section
driver.find_element(By.CSS_SELECTOR, "input#ap_password_check")
driver.find_element(By.CSS_SELECTOR, "input[name='passwordCheck'][type='password']")

# CSS locators for 'Continue' button
driver.find_element(By.CSS_SELECTOR, "#continue")
driver.find_element(By.CSS_SELECTOR, "input.a-button-input")
driver.find_element(By.CSS_SELECTOR, "[type='submit']")
driver.find_element(By.CSS_SELECTOR, "input[aria-labelledby='auth-continue-announce']")

# CSS locator for 'Conditions of Use' link
driver.find_element(By.CSS_SELECTOR, "a[href*='ref=ap_register_notification_condition_of_use']")

# CSS locator for 'Privacy Notice' link
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice']")

# CSS locator for 'Create a free business account' link
driver.find_element(By.CSS_SELECTOR, "a#ab-enhanced-registration-link")

# CSS locator for 'Already have an account? Sign in' link
driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis")
