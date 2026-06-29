import logging
import os
from datetime import datetime

from selenium.webdriver.remote.webdriver import WebDriver


def configure_logging() -> logging.Logger:
    logger = logging.getLogger("qa_framework")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        logger.addHandler(handler)
    return logger


def take_screenshot(driver: WebDriver, name: str) -> str:
    screenshots_dir = "artifacts/screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(screenshots_dir, f"{name}_{timestamp}.png")
    driver.save_screenshot(path)
    return path
