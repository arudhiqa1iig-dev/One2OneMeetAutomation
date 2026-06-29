from selenium.webdriver.common.by import By
import time


class ContactPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self):
        self.driver.find_element(By.NAME, "company_name").send_keys("My Company")
        time.sleep(0.5)
        self.driver.find_element(By.NAME, "event_size").send_keys("500")
        time.sleep(0.5)
        self.driver.find_element(By.NAME, "contact_person").send_keys("John Doe")
        time.sleep(0.5)
        self.driver.find_element(By.NAME, "contact_email").send_keys("john@example.com")
        time.sleep(0.5)
        self.driver.find_element(By.NAME, "contact_number").send_keys("9800000000")
        time.sleep(0.5)
        self.driver.find_element(By.NAME, "comments").send_keys("Just testing the form!")
        time.sleep(0.5)
        print("Contact form filled! NOT submitting.")
