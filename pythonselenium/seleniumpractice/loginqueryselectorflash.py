from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationexercise.com/")
login = driver.find_element(By.XPATH, '//a[@href="/login"]')
login.click()
email = driver.execute_script("return document.querySelector('[data-qa=\"login-email\"]');")
email.send_keys("queen1@gmail.com")
password = driver.execute_script("return document.querySelector('[data-qa=\"login-password\"]');")
password.send_keys("1234sho")
loginbtn = driver.find_element(By.XPATH,'//button[@data-qa="login-button"]')
for i in range(2):
    driver.execute_script("arguments[0].style.background='yellow';""arguments[0].style.border='3px solid red';",loginbtn )
    time.sleep(0.3)
    driver.execute_script( "arguments[0].style.background='';""arguments[0].style.border='';",loginbtn)
    time.sleep(0.3)
driver.execute_script("arguments[0].click();",loginbtn)
print("Login button flashed and clicked successfully")










   


