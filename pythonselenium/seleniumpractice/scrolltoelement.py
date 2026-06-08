from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
checkbox = driver.find_element(By.XPATH,"//button[text()='Check this']")
actions = ActionChains(driver)
#Scroll until element is visible
actions.scroll_to_element(checkbox).perform()
print("Scroll to element done")



