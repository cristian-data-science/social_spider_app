import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd

if __name__ == '__main__':


    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("--log-level=3")
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-extensions")
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--disable-dev-shm-usage')
    #options.add_argument('proxy-server=106.122.8.54:3128')
    #options.add_argument(r'--user-data-dir=C:\Users\suppo\AppData\Local\Google\Chrome\User Data\Default')
    options.add_argument("--lang=es-ES")

    webdriver = uc.Chrome(
        options=options,
    )
    
    webdriver.get('https://www.tiktok.com/foryou?is_copy_url=1&is_from_webapp=v1&lang=es')
    sleep(3)

    trend = webdriver.find_elements(By.XPATH, value= '//*[@id="app"]/div[2]/div[1]/div/div[2]/div/div[1]/div[4]/div/a[*]/div/p')
    link = webdriver.find_elements(By.XPATH, value= '//*[@id="app"]/div[2]/div[1]/div/div[2]/div/div[1]/div[4]/div/a[*]')

    link = [ i.get_attribute("href") for i in link ]
    
    #zz = [ i.get_attribute("href") for i in zz ]
    lista = []
    for x in trend:
        x = x.text
        #print(x)
        lista.append(x)
    
    df = pd.DataFrame(lista, columns=["trend"])
    df["link"] = link
    print(df)
    df.to_csv("./resultados/tiktok.csv", index=False)



