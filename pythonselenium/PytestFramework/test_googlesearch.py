import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('search_item',[('selenium'),('pytest'),('selenium locators')])
def test_search(search_item):
    driver=webdriver.Chrome()
    driver.get("https://www.google.co.in/index.html")
    driver.find_element(By.XPATH,'//textarea[@class="gLFyf"]').send_keys(search_item)
    time.sleep(6)
    driver.quit()
    