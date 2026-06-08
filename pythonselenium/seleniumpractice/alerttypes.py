from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)
simple = driver.find_element(By.XPATH,"//input[@id='alert1']")
simple.click()
alert = driver.switch_to.alert

print("Simple Alert:",alert.text)
alert.accept()
prompt=driver.find_element(By.XPATH,'//input[@id="prompt"]')
prompt.click()
alert = driver.switch_to.alert

alert.send_keys("Shob")
alert.accept()
print("Prompt alert handled")
confirm = driver.find_element(By.XPATH,'//input[@id="confirm"]')
confirm.click()
alert = driver.switch_to.alert

alert.accept()
print("Confirm alert handled")