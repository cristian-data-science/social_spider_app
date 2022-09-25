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
        self.driver = webdriver


    def tweet_trends(self, url):   
        webdriver.get(url)
        sleep(2)
        xx = webdriver.find_elements(By.XPATH, value= '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/section/div/div/div[*]/div/div/div')
        lista = []
        for x in xx:
            linea = x.text  
            linea = linea.split(sep='\n')
            if len(linea) == 2:
                linea.append("1000")       
            lista.append(linea)    
        df = pd.DataFrame(lista, columns=["identificador","tendencia","tweets"])
        #print(df)
        df["tweets"] = df["tweets"].str.replace(".","").str.replace("Tweets","").str.replace(",1 mil","100").str.replace(",1 mil","100").str.replace(",2 mil","200").str.replace(",3 mil","300").str.replace(",4 mil","400").str.replace(",5 mil","500").str.replace(",6 mil","600").str.replace(",7 mil","700").str.replace(",8 mil","800").str.replace(",9 mil","900").str.replace("mil","000").str.replace(" ","")
        df["tweets"] = df["tweets"].str.strip()
        df["tweets"] = df["tweets"].astype(int)
        print(df)
        df.to_csv("twitter.csv", index=False)

       

     