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

# Amazon logo locator by XPATH
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
driver.find_element(By.XPATH, "//i[@role='img']")

# Sign in locator using XPATH
driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")

# Email or mobile phone number using XPATH locator
driver.find_element(By.XPATH, "//label[@for='ap_email']")
driver.find_element(By.XPATH, "//label[@class='a-form-label']")

# Email field locator by ID & XPATH
driver.find_element(By.ID, 'ap_email')
driver.find_element(By.XPATH, "//input[@type='email' and @name='email']")

# Continue button by ID & XPATH
driver.find_element(By.ID, 'continue')
driver.find_element(By.XPATH, "//input[@aria-labelledby='continue-announce']")
driver.find_element(By.XPATH, "//input[@class='a-button-input']")
driver.find_element(By.XPATH, "//input[@type='submit']")

# Conditions of use link by text using XPATH
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

# Privacy Notice link by text using XPATH
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

# Need help link by XPATH
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# Forgot your password link locator by ID
driver.find_element(By.ID, 'auth-fpp-link-bottom')

# Other issues with Sign-In link locator by ID
driver.find_element(By.ID, 'ap-other-signin-issues-link')

# Buying for work? using XPATH locator
driver.find_element(By.XPATH, "//div[@class='a-section a-spacing-micro']")

# New to Amazon? using XPATH locator
driver.find_element(By.XPATH, "//h5[@aria-level='5']")

# Create your Amazon account button
driver.find_element(By.ID, 'createAccountSubmit')
driver.find_element(By.XPATH, "//a[@class='a-button-text']")
