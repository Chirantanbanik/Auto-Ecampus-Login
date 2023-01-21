from selenium import webdriver
from getpass import getpass
import time
from selenium.webdriver.common.by import By

username = input("Enter in your Username: ")
password = getpass("Enter your password: ")


driver = webdriver.Chrome("C:\Drivers\WebDriver\\chromedriver.exe")
driver.get("https://ecm.smtech.in/ecm/")
time.sleep(5)
searchbox = driver.find_element(by=By.XPATH,value='//*[@id="TxtUserName"]').send_keys(username) 
searchpassword = driver.find_element(by=By.XPATH,value='//*[@id="TxtPassword"]').send_keys(password)
searchbutton = driver.find_element(by=By.XPATH,value='//*[@id="btnLogin"]').click()
print("Sucessfully loggedin!")




