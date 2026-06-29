from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import settings


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, settings.timeout)

    def open(self):
        self.driver.get(settings.login_url)
        return self

    def is_loaded(self):
        return self.wait.until(EC.presence_of_element_located((By.NAME, "username")))

    def username_field_is_visible(self):
        element = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        return element.is_displayed()

    def login(self, username, password):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        return self
