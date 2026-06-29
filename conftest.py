import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

from config import settings
from utils import configure_logging, take_screenshot


@pytest.fixture
def driver(request):
    logger = configure_logging()
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    if settings.headless or os.getenv("CI"):
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(
        options=chrome_options,
        service=webdriver.chrome.service.Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install()),
    )
    driver.implicitly_wait(2)
    logger.info("Started Chrome driver")

    yield driver

    if request.node.rep_call.failed:
        screenshot_path = take_screenshot(driver, request.node.name)
        logger.error("Test failed. Screenshot saved to %s", screenshot_path)

    driver.quit()
    logger.info("Closed Chrome driver")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
