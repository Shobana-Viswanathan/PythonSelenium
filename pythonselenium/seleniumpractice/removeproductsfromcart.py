from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com/")

driver.find_element(By.XPATH,'//a[@href="/login"]').click()
driver.find_element(By.XPATH,'//input[@data-qa="login-email"]').send_keys("queen1@gmail.com")
driver.find_element(By.XPATH,'//input[@data-qa="login-password"]').send_keys("1234sho")
driver.find_element(By.XPATH,'//button[@data-qa="login-button"]').click()

driver.find_element(By.XPATH,'//a[@href="/products"]').click()

action = ActionChains(driver)

prod1 = driver.find_element(By.XPATH,"(//a[contains(@class,'add-to-cart')])[1]")
action.move_to_element(prod1).perform()
driver.execute_script("arguments[0].click();",prod1)
driver.execute_script("arguments[0].click();",WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//button[contains(.,'Continue Shopping')]"))))

prod2 = driver.find_element(By.XPATH,"(//a[contains(@class,'add-to-cart')])[3]")
action.move_to_element(prod2).perform()
driver.execute_script("arguments[0].click();",prod2)
driver.execute_script("arguments[0].click();",WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//button[contains(.,'Continue Shopping')]"))))

prod3 = driver.find_element(By.XPATH,"//p[text()='Sleeveless Dress']/following-sibling::a[@data-product-id='3']")
action.move_to_element(prod3).perform()
driver.execute_script("arguments[0].click();",prod3)

viewcart = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//u[text()='View Cart']")))

driver.execute_script("arguments[0].click();",viewcart)
product_name = input("Enter product name to remove: ")

delete_btn = driver.find_element( By.XPATH, f"//a[contains(text(),'{product_name}')]/ancestor::tr//a[@class='cart_quantity_delete']")

delete_btn.click()

print("Product deleted by successfully")