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
    
    webdriver.get('https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl')
    sleep(3)

    trend = webdriver.find_elements(By.XPATH, value= '/html/body/ytd-app/div[*]/ytd-page-manager/ytd-browse[*]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[*]/div[*]/ytd-shelf-renderer/div[*]/div[*]/ytd-expanded-shelf-contents-renderer/div/ytd-video-renderer[*]/div[1]/div/div[1]/div/h3/a/yt-formatted-string')
    link = webdriver.find_elements(By.XPATH, value= '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[*]/div[3]/ytd-shelf-renderer/div[1]/div[2]/ytd-expanded-shelf-contents-renderer/div/ytd-video-renderer[*]/div[*]/div/div[1]/div/h3/a')
    # sacando atributo href para crear lista de links mas adelante
    link = [ i.get_attribute("href") for i in link ]
    
    lista = []
    # recolectando nombre de videos
    for x in trend:
        x = x.text
        #print(x)
        lista.append(x)
        
        #print(lista)
    df = pd.DataFrame(lista, columns=["trend"])
    df["link"] = link
    df["top"] = 1
    cont = 0
    # agregando #top de video
    for trend in df["trend"]:
        df["top"].iloc[cont] = cont
        cont = cont + 1
    df["top"] = df["top"] +1    
    print(df)
    df.to_csv("./resultados/youtube.csv", index=False)



