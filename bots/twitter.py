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
    
    webdriver.get('https://twitter.com/i/trends')
    sleep(4)
    xx = webdriver.find_elements(By.XPATH, value= '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[*]/section/div/div/div[*]/div/div/div')
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
    #df["tweets"] = df["tweets"].astype(float).astype(int)
    links = []
    for i in df["tendencia"]:
        links.append(f"https://twitter.com/search?q={i}&src=trend_click&vertical=trends")
        #print(f"https://twitter.com/search?q={i}&src=trend_click&vertical=trends")
    
    df["link"] = links
    df["link"] = df["link"].replace(" ","%20")
    print(df)
    #print(lista)
    df.to_csv("./resultados/twitter.csv", index=False)
    
