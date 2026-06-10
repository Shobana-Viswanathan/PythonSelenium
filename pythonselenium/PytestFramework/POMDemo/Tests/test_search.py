import pytest
from Utilities import excelReader
import Utilities.logCreater

from Pages.Homepage import HomePage
from Pages.Searchpage import SearchPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:

    logger = Utilities.logCreater.log_creator()

  
    def test_validproduct(self):

        home_page = HomePage(self.driver)
        search_data = excelReader.get_data("TestData/SearchData.xlsx","Search")
        valid_product = search_data[0]
        home_page.search_for_product(valid_product)
        self.logger.info("Valid product searched")
        search_page = SearchPage(self.driver)
        assert search_page.display_status_of_valid_product()
        self.logger.info("Valid product displayed")
    def test_invalidproduct(self):
        home_page = HomePage(self.driver)
        search_data = excelReader.get_data("TestData/SearchData.xlsx","Search")
        invalid_product = search_data[1]
        home_page.search_for_product(invalid_product)
        self.logger.info("Invalid product searched")
        search_page = SearchPage(self.driver)

        expected = "There is no product that matches the search criteria."

        assert search_page.get_no_product_message() == expected
        self.logger.info("Appropriate error message displayed")






    




