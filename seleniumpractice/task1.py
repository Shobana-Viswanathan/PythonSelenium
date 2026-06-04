import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.com/")

res = driver.title

search = driver.find_element(By.XPATH, "//textarea[@jsname='yZiJbe']")
search.send_keys("Selenium")
search.send_keys(Keys.ENTER)
print(res)

time.sleep(5)
driver.quit()