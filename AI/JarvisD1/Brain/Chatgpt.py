# pip install selenium

# Importing Important Modules like Selenium, Time, Warning etc

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium. webdriver.common.by import By
import warnings

warnings.simplefilter("ignore")

Link = "https://gpt4login.com/use-chatgpt-online-free/"


# Setting Up The Driver & Opening The Website :-

chrome_driver_path = 'chromedriver.exe'
chrome_options = Options()
chrome_options.headless = True
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
driver.maximize_window()
driver.get(Link)