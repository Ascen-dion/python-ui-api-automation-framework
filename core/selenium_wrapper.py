import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumWrapper:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator, timeout=30):
        with allure.step(f"Click element: {locator}"):
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()

    def enter_text(self, locator, text, timeout=30):
        with allure.step(f"Enter text '{text}' into element: {locator}"):
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            element.clear()
            element.send_keys(text)

    def is_visible(self, locator, timeout=30):
        with allure.step(f"Verify element is visible: {locator}"):
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
    
    def get_text(self, by, locator, description="Get text"):
        with allure.step(f"{description}: {locator}"):
            return self.driver.find_element(by, locator).text
        
