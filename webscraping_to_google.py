import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import lxml
#import bs4
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

# Need to setup google sheet by using 
creds = ServiceAccountCredentials.from_json_keyfile_name("creds2.json", scope)

client = gspread.authorize(creds)
sheet = client.open("Plants").sheet1  # Open the spreadsheet
data = sheet.get_all_records()

driver = webdriver.Chrome(executable_path='/Users/mack/Downloads/chromedriver3')
driver.get("http://adafruit.com")
time.sleep(5)

search_tab = driver.find_element_by_xpath('//*[@id="search"]')
search_tab.click()
search_tab.send_keys('4243')
search_tab.submit()
time.sleep(5)

product = driver.find_element_by_xpath("//h1[@class='products_name']")
availability = driver.find_element_by_xpath("//div[@class='oos-header']").text
product = driver.find_element_by_xpath("//h1[@class='products_name']").text
product2 = driver.find_element_by_xpath("//span[@class='hidden-xs-inline'][2]").text
price = driver.find_element_by_xpath("//div[@id='prod-right-side']/div[@id='prod-price']/span").text
availability = driver.find_element_by_xpath("//div[@id='prod-stock']/div[@class='prod-oos-box']/div[@class='oos-header']")

now = datetime.datetime.now()
now_format = now.strftime("%Y-%m-%d %H:%M:%S")
insertRow = [now_format,product, price, availability.text]
sheet.insert_row(insertRow, 2) 
print(now_format)
print(price)
