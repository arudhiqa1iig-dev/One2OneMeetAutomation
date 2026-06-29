from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import settings


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, settings.timeout)

    def open(self):
        self.driver.get(settings.base_url)
        return self

    def is_loaded(self):
        self.wait.until(EC.title_contains("One2One"))
        return "one2one" in self.driver.title.lower()

    def has_contact_link(self):
        contact_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Contact")))
        return contact_link.is_displayed()

    def scroll_down_and_back(self):
        for i in range(1, 10):
            self.driver.execute_script(f"window.scrollTo(0, {i * 300});")
        self.driver.execute_script("window.scrollTo(0, 0);")

    def go_to_contact(self):
        contact_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Contact")))
        contact_link.click()
        return self
