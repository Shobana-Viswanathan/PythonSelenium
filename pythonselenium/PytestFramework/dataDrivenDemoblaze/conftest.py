import pytest
import read_config
from selenium import webdriver

@pytest.fixture()
def setup_and_teardown(request):

    browser = read_config.get_config("basic_info", "browser")
    app_url = read_config.get_config("basic_info", "url")

    if browser == "chrome":
        driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(app_url)
    request.cls.driver = driver
    yield driver
    driver.quit()
    



