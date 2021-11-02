from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service

""" ser = Service("C:\Driver\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser)
driver.get("http://demo.guru99.com/test/newtours/")
print(driver.title)
driver.close() 
#new line
"""
#added remotely
# New branch created
ser1 = Service("C:\Driver\geckodriver-v0.30.0-win64/geckodriver.exe")
driver1 = webdriver.Firefox(service=ser1)
driver1.get("http://www.google.co.in")
print(driver1.title)
driver1.close()
