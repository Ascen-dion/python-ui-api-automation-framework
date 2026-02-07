from core.selenium_wrapper import SeleniumWrapper

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.ui = SeleniumWrapper(driver)

    def open(self, url):
        self.driver.get(url)
