from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
element = driver.find_element(By.XPATH,"//button[text()='Check this']")
origin = ScrollOrigin.from_element(element)
actions = ActionChains(driver)
#Scroll starting from a specific element
actions.scroll_from_origin(origin, 0, 300).perform()
print("Scroll by origin is done")

