from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

class DriverFactory:

    @staticmethod
    def get_driver(browser="chrome"):
        browser = browser.lower()

        if browser == "chrome":
            options = ChromeOptions()
            options.add_argument("--start-maximized")
            return webdriver.Chrome(options=options)

        if browser == "firefox":
            options = FirefoxOptions()
            return webdriver.Firefox(options=options)

        if browser == "edge":
            options = EdgeOptions()
            return webdriver.Edge(options=options)

        raise Exception(f"Unsupported browser: {browser}")
