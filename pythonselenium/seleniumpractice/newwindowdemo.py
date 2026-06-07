from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")
driver.maximize_window()
driver.find_element(By.ID,"windowButton").click()
driver.switch_to.window(driver.window_handles[1])
text = driver.find_element(By.ID, "sampleHeading").text
print("Text displayed:", text)