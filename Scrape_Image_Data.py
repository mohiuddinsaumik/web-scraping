import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

c_path = r"D:\chromedriver.exe"
service = Service(executable_path=c_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.daraz.com.bd/men-muslimin-shirts/?spm=a2a0e.home.cate_4_3.3.2d4612f7YivCqv")
driver.maximize_window()


data = []

for i in range(1, 40):
    prd_title = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div/div/div[1]/div[2]/div["+str(i)+"]/div/div/div[2]/div[2]/a').text
    prd_link = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div/div/div[1]/div[2]/div["+str(i)+"]/div/div/div[2]/div[2]/a').get_attribute('href')
    prd_img = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div/div/div[1]/div[2]/div["+str(i)+"]/div/div/div[1]/div[1]/a/img').get_attribute('src')
    response = requests.get(prd_img)

    data.append([prd_title, prd_link, prd_img])


# Saving data to a CSV file
df = pd.DataFrame(data, columns=["Title", "Link", "Image URL"])
df.to_csv("data.csv", index=False)
