from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://automationexercise.com")
print(driver.title)
reg=driver.find_element(By.XPATH,"//a[normalize-space()='Signup / Login']")
reg.click()
usrname=driver.find_element(By.XPATH,'//input[@placeholder="Name"]')
usrname.send_keys("Shobs")
email=driver.find_element(By.XPATH,"//input[@data-qa='signup-email']")
email.send_keys("abcd112@gmail.com")
driver.find_element(By.XPATH,"//button[normalize-space()='Signup']").click()
driver.find_element(By.XPATH,"//input[@id='id_gender2']").click()
password=driver.find_element(By.XPATH,"//input[@id='password']")
password.send_keys("1234sho")
fstname=driver.find_element(By.XPATH,'//input[@data-qa="first_name"]')
fstname.send_keys("Shob")
lstname=driver.find_element(By.XPATH,'//input[@data-qa="last_name"]')
lstname.send_keys("V")
address=driver.find_element(By.XPATH,"//input[@data-qa='address']")
address.send_keys("ABC,Street")
state=driver.find_element(By.XPATH,"//input[@data-qa='state']")
state.send_keys("TamilNadu")
city=driver.find_element(By.XPATH,'//input[@data-qa="city"]')
city.send_keys("Trichy")
zipcode=driver.find_element(By.XPATH,'//input[@data-qa="zipcode"]')
zipcode.send_keys("63501")
mob=driver.find_element(By.XPATH,'//input[@data-qa="mobile_number"]')
mob.send_keys("9876543210")
btn=driver.find_element(By.XPATH,'//button[@data-qa="create-account"]')
driver.execute_script("arguments[0].click();",btn)
txt=driver.find_element(By.XPATH,'//b[text()="Account Created!"]')
assert txt.text.lower() == "account created!"
print("Account created successfully")
continue_btn=driver.find_element(By.XPATH,'//a[@data-qa="continue-button"]')
driver.execute_script("arguments[0].click();",continue_btn)
userName = driver.find_element(By.XPATH, "//ul[@class = 'nav navbar-nav']/descendant::a[text() = ' Logged in as ']")
print(userName.text)
checkuser = userName.text
driver.find_element(By.XPATH,'//a[@href="/products"]').click()
wait=WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME,"features_items")))
action = ActionChains(driver)
prod1 = driver.find_element(By.XPATH,"(//a[contains(@class,'add-to-cart')])[1]")
action.move_to_element(prod1).perform()
driver.execute_script("arguments[0].click();", prod1)
cbtn = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//button[contains(.,'Continue Shopping')]")))
driver.execute_script("arguments[0].click();", cbtn)
checkout=driver.find_element(By.XPATH,'//a[text()="Proceed To Checkout"]')
checkout.click()
details=driver.find_element(By.XPATH,'(//li[@class="address_city address_state_name address_postcode"])[1]')
assert details.txt == "Trichy TamilNadu 63501"
delete=driver.find_element(By.XPATH, "//a[@href = '/delete_account']").click()
wait.until(EC.visibility_of_element_located,delete)
deleteSuc = driver.find_element(By.XPATH, "//p[text() = 'Your account has been permanently deleted!']")
print(deleteSuc.text)
driver.find_element(By.XPATH,'//a[@data-qa="continue-button"]')
print("Completed successfully")




















