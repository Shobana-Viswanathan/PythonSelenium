from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.leafground.com/select.xhtml")
driver.maximize_window()
dropdown = driver.find_element(By.XPATH,"//h5[text()='Which is your favorite UI Automation tool?']/following::select[1]")
select = Select(dropdown)
select.select_by_index(1)
print("Selected by index done")
