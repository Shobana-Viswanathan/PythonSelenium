from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Chrome()
driver.get("https://www.hyrtutorials.com/p/add-padding-to-containers.html")
driver.maximize_window()

lastname = driver.find_element(By.XPATH, "//div[@id='content-wrapper']//input[2]")
lastname.send_keys("V")

driver.find_element(locate_with(By.TAG_NAME, "input").above(lastname)).send_keys("Shobana")

email = driver.find_element(locate_with(By.TAG_NAME, "input").below(lastname))
email.send_keys("shob@gmail.com")

password = driver.find_element(locate_with(By.TAG_NAME, "input").below(email))
password.send_keys("Shob@123")

repeatpassword = driver.find_element(locate_with(By.TAG_NAME, "input").below(password))
repeatpassword.send_keys("Shob@123")

clearbtn = driver.find_element( By.XPATH,"//button[normalize-space()='Clear']")

register_btn = driver.find_element(locate_with(By.TAG_NAME, "button").to_left_of(clearbtn))

register_btn.click()

print("Registered Successfully")

driver.quit()