from time import sleep
import allure
from pages.saucedemo_login_page import SauceDemoLoginPage


@allure.title("SauceDemo login test")
def test_login_success(driver, base_url):
    page = SauceDemoLoginPage(driver, base_url)
    page.open()
    page.login("standard_user", "secret_sauce")
    sleep(2)  # Just for demo purposes; avoid in real tests 
    page.verify_home_loaded()


@allure.title("SauceDemo invalid login test")
def test_login_invalid_user(driver, base_url):
    page = SauceDemoLoginPage(driver, base_url)

    page.open()
    page.login("locked_out_user", "secret_sauce")

    page.verify_login_error()
