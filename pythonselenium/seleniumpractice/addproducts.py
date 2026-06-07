from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://automationexercise.com/")
print(driver.title)

driver.find_element(By.XPATH,'//a[@href="/login"]').click()

WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,'//input[@data-qa="login-email"]'))
)

driver.find_element(By.XPATH,'//input[@data-qa="login-email"]').send_keys("queen1@gmail.com")
driver.find_element(By.XPATH,'//input[@data-qa="login-password"]').send_keys("1234sho")
driver.find_element(By.XPATH,'//button[@data-qa="login-button"]').click()

print(driver.title)

driver.find_element(By.XPATH,'//a[@href="/products"]').click()

WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.CLASS_NAME,"features_items"))
)

action = ActionChains(driver)


prod1 = driver.find_element(By.XPATH,"(//a[contains(@class,'add-to-cart')])[1]")
action.move_to_element(prod1).perform()
driver.execute_script("arguments[0].click();", prod1)

cbtn = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,"//button[contains(.,'Continue Shopping')]"))
)
driver.execute_script("arguments[0].click();", cbtn)


prod2 = driver.find_element(By.XPATH,"(//a[contains(@class,'add-to-cart')])[3]")
action.move_to_element(prod2).perform()
driver.execute_script("arguments[0].click();", prod2)


viewcart = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//u[text()='View Cart']"))
)
driver.execute_script("arguments[0].click();", viewcart)


cartview = driver.find_elements(By.XPATH,'//table[@id="cart_info_table"]/tbody/tr')

if len(cartview) == 2:
    print("Products added successfully")
else:
    print("Products not added")


price1 = driver.find_element(By.XPATH,'//tr[@id="product-1"]//td[@class="cart_price"]/p')
print("Price1 :", price1.text)

qty1 = driver.find_element(By.XPATH,'//tr[@id="product-1"]//td[@class="cart_quantity"]/button')
print("Quantity1 :", qty1.text)

total1 = driver.find_element(By.XPATH,'//tr[@id="product-1"]//td[@class="cart_total"]/p')
print("Total1 :", total1.text)


price2 = driver.find_element(By.XPATH,'//tr[@id="product-2"]//td[@class="cart_price"]/p')
print("Price2 :", price2.text)

qty2 = driver.find_element(By.XPATH,'//tr[@id="product-2"]//td[@class="cart_quantity"]/button')
print("Quantity2 :", qty2.text)

total2 = driver.find_element(By.XPATH,'//tr[@id="product-2"]//td[@class="cart_total"]/p')
print("Total2 :", total2.text)

print("Success")

driver.quit()