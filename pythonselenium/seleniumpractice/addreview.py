from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/")
driver.maximize_window()
wait = WebDriverWait(driver,10)
login=driver.find_element(By.XPATH,'//a[@href="/login"]')
login.click()
email=driver.find_element(By.XPATH,'//input[@data-qa="login-email"]')
email.send_keys("queen1@gmail.com")
password=driver.find_element(By.XPATH,'//input[@data-qa="login-password"]')
password.send_keys("1234sho")
loginbtn=driver.find_element(By.XPATH,'//button[@data-qa="login-button"]')
loginbtn.click()
pro=driver.find_element(By.XPATH,"//a[@href='/products']")
driver.execute_script("arguments[0].click()",pro)
txt=wait.until(EC.visibility_of_element_located(By.XPATH,'//div[@class="features_items"]//child::h2[text()="All Products"]'))

assert txt.text == "All Products"
driver.find_element(By.XPATH,'//a[@href="/product_details/1"]').click()
rev=driver.find_element(By.XPATH,"Write Your Review")
assert rev.is_displayed()
name=driver.find_element(By.ID,"name")
email=driver.find_element(By.ID,"email")
name.send_keys("Shob")
email.send_keys("shi@gmail.com")
review=driver.find_element(By.NAME,"review")
review.send_keys("The product is too good.")
driver.find_element(By.XPATH,"//button[@id='button-review']")
res=driver.find_element(By.XPATH,'//span[text()="Thank you for your review."]')
assert res.text == "Thank you for your review."
print("Done")