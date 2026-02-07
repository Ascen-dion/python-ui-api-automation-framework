import allure
from core.selenium_wrapper import SeleniumWrapper


class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.ui = SeleniumWrapper(driver)

    @allure.step("Open base URL")
    def open(self, path=""):
        url = self.base_url + path
        self.driver.get(url)
