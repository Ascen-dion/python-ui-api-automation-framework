
import allure
from pages.amazon_home_page import AmazonHomePage

@allure.feature("Amazon Search")
@allure.story("Search Product")
def test_search_laptop(driver, base_url):
    amazon = AmazonHomePage(driver)
    amazon.open(base_url)
    amazon.search("laptop")
    amazon.verify_results_loaded()
