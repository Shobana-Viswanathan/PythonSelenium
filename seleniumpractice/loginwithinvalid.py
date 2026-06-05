from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://automationexercise.com/")
login=driver.find_element(By.XPATH,'//a[@href="/login"]')
login.click()
email=driver.find_element(By.XPATH,'//input[@data-qa="login-email"]')
email.send_keys("que1@gmail.com")
password=driver.find_element(By.XPATH,'//input[@data-qa="login-password"]')
password.send_keys("1234sho")
loginbtn=driver.find_element(By.XPATH,'//button[@data-qa="login-button"]')
loginbtn.click()
expected = "Your email or password is incorrect!"

error_msg = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Your email or password is incorrect!']") ))

if error_msg.text == expected :
    print("Success!")
else :
    print("No")