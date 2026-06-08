from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
actions = ActionChains(driver)
#Scroll fixed pixels
actions.scroll_by_amount(0, 500).perform()#scroll down
#scroll up scroll_by_amount(0,-500)
print("Scroll by amount is done")



