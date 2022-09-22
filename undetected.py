import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date, timedelta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import pandas as pd
from time import sleep





if __name__ == '__main__':

    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("--start-maximized")
    #options.add_argument("--window-size=1920,1080")
    options.add_argument("--log-level=3")
    #options.add_argument('proxy-server=106.122.8.54:3128')
    #options.add_argument(r'--user-data-dir=C:\Users\suppo\AppData\Local\Google\Chrome\User Data\Default')

    webdriver = uc.Chrome(options=options,)
    webdriver.get('https://www.nombrerutyfirma.com/')
    sleep(4)
    df_cust = pd.read_excel("clientes.xlsx", sheet_name="Export")
    df_cust_list = df_cust["CUSTOMERACCOUNT"].to_list()
    print(len(df_cust_list))
   
    df = pd.DataFrame(columns=["name", "sex", "address", "city"])
    for rut in df_cust_list:
        webdriver.get('https://www.nombrerutyfirma.com/')
        sleep(2)
        rut_b = webdriver.find_element(By.LINK_TEXT, value='RUT')
        rut_b.click()
        div_rut = webdriver.find_element(By.XPATH, value='//*[@id="formato-live"]/div/input')
        div_rut.click()
        div_rut.send_keys(rut)
        
        buscar_b = webdriver.find_element(By.XPATH, value='//*[@id="formato-live"]/div/span/button').click()
        try:
            name = webdriver.find_element(By.XPATH, value= '/html/body/div[2]/div/table/tbody/tr/td[1]')
            sex = webdriver.find_element(By.XPATH, value= '/html/body/div[2]/div/table/tbody/tr/td[3]')
            address = webdriver.find_element(By.XPATH, value= '/html/body/div[2]/div/table/tbody/tr/td[4]')
            city = webdriver.find_element(By.XPATH, value= '/html/body/div[2]/div/table/tbody/tr/td[5]')

        except:
            print("no encontrado")
        try:    
            lista = [name.text, sex.text, address.text, city.text]
        #df["name"] = df["name"].append(name.text)    
            print(lista)
        except:
            print(f"No se pudo imprimir el rut: {rut}")    

    sleep(30)
