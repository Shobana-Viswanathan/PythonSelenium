from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
btn = driver.find_element(By.XPATH,'//button[text()="Check this"]')
driver.execute_script("arguments[0].scrollIntoView()",btn)
btn.click()
print("Scroll into view used successfully")
