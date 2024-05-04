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

#locator by ID
driver.find_element(By.ID, 'twotabsearchtextbox')

#locator by XPHAT
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")

#By multiple attributes
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon' and @type='text' and @name='field-keywords']")

#locator by text
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")

#By text and attributes
driver.find_element(By.XPATH, "//a[@class='nav-a  ' and text()='Best Sellers']")
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ' and @data-csa-c-slot-id='nav_cs_3']")

#any tag + by text and attributes 
driver.find_element(By.XPATH, "//*[text()='Best Sellers' and @class='nav-a  ' and @data-csa-c-slot-id='nav_cs_3']")

#contains()
driver.find_element(By.XPATH, "//select[contains(@class, 'search-dropdown')]")
driver.find_element(By.XPATH, "//*[contains(@class, 'search-dropdown')]")
driver.find_element(By.XPATH, "//*[contains(@class, 'search-dropdown') and ...]")
