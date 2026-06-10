from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.search_field_name = "search"
        self.search_button_xpath = "//button[@class='btn btn-default btn-lg']"

    def enter_product_into_search_box(self, product_name):
        self.driver.find_element(By.NAME,self.search_field_name).send_keys(product_name)

    def click_search_button(self):
        self.driver.find_element(By.XPATH,self.search_button_xpath).click()

    def search_for_product(self, product_name):
        self.enter_product_into_search_box(product_name)
        self.click_search_button()