import pytest
import yaml
from core.driver_factory import DriverFactory

@pytest.fixture(scope="session")
def config():
    with open("config/config.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture
def driver(config):
    driver = DriverFactory.get_driver(config["browser"])
    yield driver
    driver.quit()

@pytest.fixture
def base_url(config):
    return config["base_url"]

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            driver.save_screenshot("failure.png")
