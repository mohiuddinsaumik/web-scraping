import pandas as pd
import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

c_path = r"D:\chromedriver.exe"
service = Service(executable_path=c_path)
driver = webdriver.Chrome(service=service)

driver.get("https://uits.edu.bd/faculty-members-of-business-studies/")

t_data=[]

for i in range(1,15):
    t_name= driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div/div[2]/div/div/div/div["+str(i)+"]/div[2]/div[1]/h4/a').text
    t_designation = driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div/div[2]/div/div/div/div["+str(i)+"]/div[2]/div[1]/p').text
    t_phone = driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div/div[2]/div/div/div/div["+str(i)+"]/div[2]/div[2]/p[1]/span').text
    t_email = driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div/div[2]/div/div/div/div["+str(i)+"]/div[2]/div[2]/p[2]/span').text


    t_data.append([t_name, t_phone, t_email, t_designation])

df= pd.DataFrame(t_data, columns=["Name","Phone","email","Designation"])
df.to_csv("t_data.csv",index=False)