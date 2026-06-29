from selenium.webdriver.common.by import By
import time


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://one2onemeet.com/")
        time.sleep(2)

    def scroll_down_and_back(self):
        for i in range(1, 10):
            self.driver.execute_script(f"window.scrollTo(0, {i * 300});")
            time.sleep(0.5)
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)
        print("Done scrolling!")

    def go_to_contact(self):
        self.driver.find_element(By.LINK_TEXT, "Contact").click()
        time.sleep(2)
