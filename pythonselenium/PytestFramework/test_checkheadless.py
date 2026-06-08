import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
@pytest.mark.parametrize('browser',['chrome','firefox'])
@pytest.mark.parametrize('input_url',['https://www.flipkart.com/','https://www.amazon.in/'])
def test_url(browser,input_url):
    if browser == "chrome" :
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless=new")  
        web_driver = webdriver.Chrome(options=chrome_options)
    if browser == "firefox" :
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")    
        web_driver = webdriver.Firefox(options=firefox_options)
    web_driver.maximize_window()
    web_driver.get(input_url)
    print(web_driver.title)
    time.sleep(5)
    web_driver.close()
