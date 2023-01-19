from selenium import webdriver
from getpass import getpass

username = input("Enter in your Username: ")
password = getpass("Enter your password: ")


driver = webdriver.Chrome("C:\Drivers\WebDriver\\chromedriver.exe")
driver.get("https://ecm.smtech.in/ecm/")
searchbox = driver.find_element_by_xpath('//*[@id="TxtUserName"]').send_keys(username)
searchpassword = driver.find_element_by_xpath('//*[@id="TxtPassword"]').send_keys(password)
searchbutton = driver.find_element_by_xpath('//*[@id="btnLogin"]').click()
searchbox.submit()


