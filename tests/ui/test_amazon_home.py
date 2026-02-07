import allure
from pages.amazon_home_page import AmazonHomePage


@allure.title("Verify Amazon homepage loads successfully")
def test_amazon_homepage_load(driver):
    driver.get("https://www.amazon.in")

    home = AmazonHomePage(driver)

    assert home.ui.is_visible(home.SEARCH_BOX)
