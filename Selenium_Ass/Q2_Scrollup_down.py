from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.get("http://automationexercise.com")
driver.maximize_window()
driver.implicitly_wait(10)
print(driver.title)
element=driver.find_element(By.XPATH,'//div[@class="single-widget"]/h2')
driver.execute_script("arguments[0].scrollIntoView();",element)

ele = driver.find_element( By.XPATH,'(//h2[text()="Full-Fledged practice website for Automation Engineers"])[1]')
actions=ActionChains(driver)
actions.scroll_to_element(ele).perform()
print("Success")
