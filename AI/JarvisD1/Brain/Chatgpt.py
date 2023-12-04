# pip install selenium

# Importing Important Modules like Selenium, Time, Warning etc

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium. webdriver.common.by import By
import warnings

warnings.simplefilter("ignore")

# Link = "https://gpt4login.com/use-chatgpt-online-free/"
Link = "https://chatgpt.com/"


# Setting Up The Driver & Opening The Website :-

chrome_options = Options()
chrome_options.headless = True
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(Link)

# File Operations :- Writing, Reading

def FileReader():
    File = open("Brain\\Chatnumber.txt","r")
    Data = File.read()
    File.close()
    return Data

def FileWriter(Data):
    File = open("Brain\\Chatnumber.txt","w")
    File.write(Data)
    File.close()
    
# Sending The Query To The Website :-

def ChatGPTBrain(Query):
    Query = str(Query)
    driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[2]/div/textarea").send_keys(Query)
    sleep(1)
    driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[2]/button/span").click()
    Data = str(FileReader())

# Getting Replies :- 

    while True:

        sleep(0.5)
        
        try:
            AnswerXpath = f"/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[1]/div[{Data}]/span[2]"
            Answer = driver.find_element(by=By.XPATH,value=AnswerXpath).is_displayed()
            if str(Answer)=="True":
                break

        except:
            pass