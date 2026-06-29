from selenium.webdriver.common.by import By
import time


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://app.one2onemeet.com/auth/login")
        time.sleep(3)

    def login(self, username, password):
        self.driver.find_element(By.NAME, "username").send_keys("AE-0112")
        time.sleep(0.5)
        self.driver.find_element(By.NAME, "password").send_keys("cAZ0P*Os")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        print("Login clicked!")
