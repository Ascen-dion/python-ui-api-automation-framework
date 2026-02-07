import allure
from pages.amazon_home_page import AmazonHomePage


@allure.title("Verify Amazon homepage loads successfully")
def test_amazon_homepage_load(driver,base_url):
    home = AmazonHomePage(driver)
    home.open(base_url)
    assert home.ui.is_visible(home.SEARCH_BOX)
