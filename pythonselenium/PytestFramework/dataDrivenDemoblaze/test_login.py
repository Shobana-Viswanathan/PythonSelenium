import pytest
import read_config
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_validlogin(self) :
        self.driver.find_element(By.XPATH,"//a[@id='login2']").click()
        username=self.driver.find_element(By.XPATH,"//input[@id='loginusername']")
        user=read_config.get_config("validcredentials","username")
        username.send_keys(user)
        password=self.driver.find_element(By.XPATH,"//input[@id='loginpassword']")
        pswd=read_config.get_config("validcredentials","password")
        password.send_keys(pswd)
        self.driver.find_element(By.XPATH,"//button[@onclick='logIn()']").click()
        print("Login Successfully done")
