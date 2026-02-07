import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SauceDemoLoginPage(BasePage):

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")

    @allure.step("Login with username: {username}")
    def login(self, username, password):
        self.ui.enter_text(self.USERNAME, username)
        self.ui.enter_text(self.PASSWORD, password)
        self.ui.click(self.LOGIN_BTN)

    @allure.step("Verify inventory page loaded")
    def verify_home_loaded(self):
        assert self.ui.is_visible(self.INVENTORY_CONTAINER)
