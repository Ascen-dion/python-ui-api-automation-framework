from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


class DriverFactory:

    @staticmethod
    def get_driver(browser="chrome", execution="local", remote_url=None):
        browser = browser.lower()

        if execution == "remote":
            if browser == "chrome":
                options = ChromeOptions()
                options.add_argument("--headless=new")
                options.add_argument("--window-size=1920,1080")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--disable-gpu")

                return webdriver.Remote(
                    command_executor=remote_url,
                    options=options
                )

        # Local execution
        if browser == "chrome":
            options = ChromeOptions()
            options.add_argument("--start-maximized")
            return webdriver.Chrome(options=options)

        if browser == "firefox":
            return webdriver.Firefox()

        if browser == "edge":
            return webdriver.Edge()

        raise Exception(f"Unsupported browser: {browser}")
