from selenium.webdriver.common.by import By
from core.selenium_wrapper import SeleniumWrapper

class SauceHomePage:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.ui = SeleniumWrapper(driver)

    def open(self, url):
        self.driver.get(url)

    def login(self, user, pwd):
        self.ui.enter_text(self.USERNAME, user)
        self.ui.enter_text(self.PASSWORD, pwd)
        self.ui.click(self.LOGIN_BTN)
