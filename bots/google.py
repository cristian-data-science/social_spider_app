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
    #options.add_argument("--log-level=3")
    options.add_argument("--start-maximized")
    #options.add_argument('proxy-server=106.122.8.54:3128')
    #options.add_argument(r'--user-data-dir=C:\Users\suppo\AppData\Local\Google\Chrome\User Data\Default')

    webdriver = uc.Chrome(
        options=options,
    )
    
    webdriver.get('https://trends.google.es/trends/trendingsearches/daily?geo=CL')
    sleep(3)

    zz = webdriver.find_elements(By.XPATH, value= '/html/body/div[3]/div[2]/div/div[2]/div/div[1]/ng-include/div/div/div/div/md-list[*]/feed-item/ng-include/div/div/div[1]/div[2]/div[1]/div/span/a')
    zz = [ i.get_attribute("href") for i in zz ]
    xx = webdriver.find_elements(By.XPATH, value= '/html/body/div[3]/div[2]/div/div[2]/div/div[*]/ng-include/div/div/div/div/md-list[*]/feed-item/ng-include/div/div/div[1]')
    #xx = [ i.text for i in xx ]
    lista = []
    for x in xx:
        x = x.text
        x = x.split(sep='\n')
        x.pop(2)
        x.pop(4)
        x.pop(2)
        lista.append(x)
  
    df = pd.DataFrame(lista, columns=['top','trend','busqueda'])
    df["link"] = zz
    df["busqueda"] = df["busqueda"].str.replace("k+","000").str.replace("K","000")
    df["busqueda"] = df["busqueda"].str.replace("K+ ","000")
    df["busqueda"] = df["busqueda"].str.replace("M+","000000")
    df["busqueda"] = df["busqueda"].str.replace("+","")
    df["busqueda"] = df["busqueda"].str.replace(" ","")
    df["busqueda"] = df["busqueda"].astype(float).astype(int)
    print(df)
    df.to_csv("./resultados/google.csv", index=False)



