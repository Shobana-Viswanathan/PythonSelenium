import read_config
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
def setup_function(function):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")

def teardown_function(function):
    driver.quit()

def test_validproduct():
    search=driver.find_element(By.NAME, value="search")
    pro1=read_config.get_config("search_item","valid")
    search.send_keys(pro1)
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
    assert driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()

def test_invalidproduct():
    search=driver.find_element(By.NAME, value="search")
    pro2=read_config.get_config("search_item","invalid")
    search.send_keys(pro2)
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
    excepted_text = "There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(excepted_text)

def test_noproduct():
    search=driver.find_element(By.NAME, value="search")
    pro3=read_config.get_config("search_item","empty")
    search.send_keys(pro3)
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
    excepted_text = "There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(excepted_text)