import time
from datetime import date, timedelta, datetime
import unittest
from time import sleep
from datetime import date, timedelta



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import pandas as pd

import sys
sys.path.append("variables")
#from variables import var as v


class funciones_globales():
    
    def __init__(self, driver):
        self.driver = driver

    
    def recolect(self):
        self.driver.get("https://www.nombrerutyfirma.com/nombre")
        driver = self.driver
        sleep(20)

       

     