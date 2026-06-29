from selenium import webdriver
from pages.home_page import HomePage
from pages.contact_page import ContactPage
from pages.login_page import LoginPage



driver = webdriver.Chrome()
driver.maximize_window()

home = HomePage(driver)
home.open()
home.scroll_down_and_back()
home.go_to_contact()

contact = ContactPage(driver)
contact.fill_form()

login = LoginPage(driver)
login.open()
login.login("AE-0112", "cAZ0P*Os")

input("Press Enter to close browser...")
driver.quit()
