import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://thinking-tester-contact-list.herokuapp.com/")
name=driver.find_element(By.ID,"email")
name.send_keys("shob@gmail.com")
password=driver.find_element(By.ID,"password")
password.send_keys("1234sho")
submit=driver.find_element(By.ID,"submit").click()
print("Login successfully")