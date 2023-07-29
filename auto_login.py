import selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


c_path = r"D:\chromedriver.exe"
service = Service(executable_path=c_path)
driver = webdriver.Chrome(service=service)
driver.get("http://ucam.uits.edu.bd/Security/LogIn.aspx")
driver.maximize_window()


driver.find_element(By.ID, "logMain_UserName").send_keys("1000000001")
driver.find_element(By.NAME,"logMain$Password").send_keys("********")

# Login Button
driver.find_element(By.CLASS_NAME, "button").click()

time.sleep(40)
