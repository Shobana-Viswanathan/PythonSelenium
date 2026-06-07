from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")
driver.maximize_window()

clickme = driver.find_element(By.ID, "alertButton")
clickme.click()   

alert = driver.switch_to.alert

print("Alert handled successfully:", alert.text)

alert.accept()