from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AmazonHomePage(BasePage):

    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")

    def search(self, product):
        self.ui.enter_text(self.SEARCH_BOX, product)
        self.ui.click(self.SEARCH_BUTTON)

    def verify_results_loaded(self):
        assert "s?k=" in self.driver.current_url
