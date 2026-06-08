from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("https://www.leafground.com/select.xhtml")
driver.maximize_window()

dropdown = Select(driver.find_element(By.XPATH, "(//select)[1]"))


for option in dropdown.options:
    print(option.text)


print(dropdown.first_selected_option.text)