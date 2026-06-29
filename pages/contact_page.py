from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import settings


class ContactPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, settings.timeout)

    def open(self):
        self.driver.get(f"{settings.base_url}#contact")
        return self

    def is_loaded(self):
        return self.wait.until(
            lambda d: "contact" in d.page_source.lower() or d.current_url.lower().endswith("contact")
        )

    def company_name_field_is_visible(self):
        element = self.wait.until(EC.visibility_of_element_located((By.NAME, "company_name")))
        return element.is_displayed()

    def fill_form(self):
        self.driver.find_element(By.NAME, "company_name").send_keys("My Company")
        self.driver.find_element(By.NAME, "event_size").send_keys("500")
        self.driver.find_element(By.NAME, "contact_person").send_keys("John Doe")
        self.driver.find_element(By.NAME, "contact_email").send_keys("john@example.com")
        self.driver.find_element(By.NAME, "contact_number").send_keys("9800000000")
        self.driver.find_element(By.NAME, "comments").send_keys("Just testing the form!")
