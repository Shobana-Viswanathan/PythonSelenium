from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/browser-windows")
driver.find_element(By.ID, "messageWindowButton").click()
driver.switch_to.window(driver.window_handles[1])
print("Handled successfully")





