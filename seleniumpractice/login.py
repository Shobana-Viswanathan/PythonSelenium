from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationexercise.com/")
login=driver.find_element(By.XPATH,'//a[@href="/login"]')
login.click()
email=driver.find_element(By.XPATH,'//input[@data-qa="login-email"]')
email.send_keys("queen1@gmail.com")
password=driver.find_element(By.XPATH,'//input[@data-qa="login-password"]')
password.send_keys("1234sho")
loginbtn=driver.find_element(By.XPATH,'//button[@data-qa="login-button"]')
loginbtn.click()
userName = driver.find_element(By.XPATH, "//ul[@class = 'nav navbar-nav']/descendant::a[text() = ' Logged in as ']")
print(userName.text)
checkuser = userName.text

if "Logged in as Girl" in checkuser:
    print("The Logged username is show")
else:
    print("The logged username is not show")
