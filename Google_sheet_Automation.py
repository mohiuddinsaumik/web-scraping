from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import oauth2client
from oauth2client.service_account import ServiceAccountCredentials

import google_oauth
import gspread


# Provide the path to the ChromeDriver executable
driver_path = r"D:\chromedriver.exe"

# Initialize the ChromeDriver service
service = Service(executable_path=driver_path)

# Create a new instance of the ChromeDriver
driver = webdriver.Chrome(service=service)

# Now you can use the 'driver' object to automate browser interactions
driver.get("https://uits.edu.bd/faculty-members-of-cse/")


scopes=[
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

Credentials = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\Lenovo\\PycharmProjects\\automation2\\auth.json')

file = gspread.authorize(credentials=Credentials)

spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1UZ_ibQfkVcti7beXMefTZ6Q0nLjtR1A5GtdIimmkAKc'
spreadsheet = file.open_by_url(spreadsheet_url)
sheet = spreadsheet.sheet1



for i in range(1,10):
    name = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div/div[2]/div/div/div/div["+str(i)+"]/div[2]/div[1]/h4/a").text
    designation = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div/div[2]/div/div/div/div["+str(i)+"]/div[2]/div[1]/p").text
    print(name)
    print(designation)

    sheet.update_acell('A' + str(i + 1), name)
    sheet.update_acell('B' + str(i + 1), designation)















