import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd



options = webdriver.ChromeOptions()
    #options.headless = True
    #options.add_argument("--log-level=3")
    #options.add_argument('proxy-server=106.122.8.54:3128')
    #options.add_argument(r'--user-data-dir=C:\Users\suppo\AppData\Local\Google\Chrome\User Data\Default')
webdriver = uc.Chrome(options=options,)


def tt(): 
    webdriver.get('https://twitter.com/i/trends')
            
if __name__ == '__main__':
    tt