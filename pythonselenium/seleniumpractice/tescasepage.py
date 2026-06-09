from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://automationexercise.com/")
driver.maximize_window()
print(driver.title)

btn=driver.find_element(By.XPATH,"//div[@class='item active']//button[@type='button'][normalize-space()='Test Cases']")
driver.execute_script("arguments[0].click()",btn)
txt=driver.find_element(By.XPATH,'//b[normalize-space()="Test Cases"]')
print(txt.text)
 